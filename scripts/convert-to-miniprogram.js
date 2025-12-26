#!/usr/bin/env node
/**
 * 将 Next.js 项目的题目数据转换为小程序格式
 */

const fs = require('fs')
const path = require('path')

// 读取原始 mock-data.ts 文件
const mockDataPath = path.join(__dirname, '../packages/app/features/problem/mock-data.ts')
const mockDataContent = fs.readFileSync(mockDataPath, 'utf-8')

// 读取 SVG 映射文件
const svgImagePath = path.join(__dirname, '../packages/app/ui/svg-image.tsx')
const svgImageContent = fs.readFileSync(svgImagePath, 'utf-8')

// 解析 problemSvgMap
const problemSvgMap = {}
const svgMapRegex = /'([^']+)':\s*\[([^\]]+)\]/g
let svgMatch
while ((svgMatch = svgMapRegex.exec(svgImageContent)) !== null) {
  const key = svgMatch[1]
  const values = svgMatch[2].match(/'([^']+)'/g)?.map(v => v.replace(/'/g, '')) || []
  if (values.length > 0) {
    problemSvgMap[key] = values
  }
}

// 解析 svgFileNames
const svgFileNames = {}
const svgFileRegex = /'([^']+)':\s*'([^']+\.svg)'/g
let fileMatch
while ((fileMatch = svgFileRegex.exec(svgImageContent)) !== null) {
  svgFileNames[fileMatch[1]] = fileMatch[2]
}

console.log(`SVG映射: ${Object.keys(problemSvgMap).length} 条`)
console.log(`SVG文件名: ${Object.keys(svgFileNames).length} 条`)

// 获取 SVG URL
function getSvgUrl(problemId) {
  const svgNames = problemSvgMap[problemId] || []
  if (svgNames.length === 0) return null
  
  const svgName = svgNames[0]
  const fileName = svgFileNames[svgName] || svgName.replace(/-/g, '_') + '.svg'
  return `https://wangxiao13078-art.github.io/myazhou/svg/${fileName}`
}

// 使用更简单的方法：按题目ID分割内容
const problems = {}

// 找到所有题目ID和它们的位置
const idRegex = /'(t\d+-(?:example|train-\d+)|z\d+-quiz-\d+|final-quiz-\d+)':\s*\{/g
const idMatches = []
let idMatch
while ((idMatch = idRegex.exec(mockDataContent)) !== null) {
  idMatches.push({
    id: idMatch[1],
    start: idMatch.index
  })
}

console.log(`找到 ${idMatches.length} 个题目ID`)

// 提取每个题目的数据
for (let i = 0; i < idMatches.length; i++) {
  const current = idMatches[i]
  const nextStart = i + 1 < idMatches.length ? idMatches[i + 1].start : mockDataContent.length
  const block = mockDataContent.slice(current.start, nextStart)
  
  try {
    // 提取标题
    const titleMatch = block.match(/title:\s*['"]([^'"]+)['"]/)
    const title = titleMatch ? titleMatch[1] : current.id
    
    // 提取难度
    const diffMatch = block.match(/difficulty:\s*(\d+)/)
    const difficulty = diffMatch ? parseInt(diffMatch[1]) : 3
    
    // 提取标签
    const tagsMatch = block.match(/tags:\s*\[([^\]]+)\]/)
    const tags = tagsMatch 
      ? tagsMatch[1].match(/['"]([^'"]+)['"]/g)?.map(t => t.replace(/['"]/g, '')) || []
      : []
    
    // 提取方法名
    const methodMatch = block.match(/methodName:\s*['"]([^'"]+)['"]/)
    const methodName = methodMatch ? methodMatch[1] : null
    
    // 提取内容（使用反引号）
    const contentMatch = block.match(/content:\s*`([\s\S]*?)`/)
    const content = contentMatch ? contentMatch[1].trim() : ''
    
    // 提取步骤 - 改进的解析方法
    const steps = []
    
    // 找到steps数组的开始
    const stepsStartMatch = block.match(/steps:\s*\[/)
    if (stepsStartMatch) {
      const stepsStart = stepsStartMatch.index + stepsStartMatch[0].length
      
      // 找到匹配的结束括号
      let depth = 1
      let stepsEnd = stepsStart
      for (let j = stepsStart; j < block.length && depth > 0; j++) {
        if (block[j] === '[') depth++
        else if (block[j] === ']') depth--
        stepsEnd = j
      }
      
      const stepsContent = block.slice(stepsStart, stepsEnd)
      
      // 分割每个步骤对象 - 用 "}, {" 或 "},\n    {" 分割
      const stepObjects = stepsContent.split(/\}\s*,\s*\{/)
      
      for (let k = 0; k < stepObjects.length; k++) {
        let stepBlock = stepObjects[k]
        // 确保有花括号
        if (!stepBlock.trim().startsWith('{')) stepBlock = '{' + stepBlock
        if (!stepBlock.trim().endsWith('}')) stepBlock = stepBlock + '}'
        
        // 解析步骤标题
        const stepTitleMatch = stepBlock.match(/title:\s*['"]([^'"]+)['"]/)
        
        // 解析步骤内容 - 可能是单引号或反引号
        let stepContent = ''
        const stepContentBacktick = stepBlock.match(/content:\s*`([\s\S]*?)`/)
        if (stepContentBacktick) {
          stepContent = stepContentBacktick[1]
        } else {
          // 处理单引号包裹的内容（可能包含转义的引号）
          const stepContentQuote = stepBlock.match(/content:\s*'((?:[^'\\]|\\.)*)'/)
          if (stepContentQuote) {
            stepContent = stepContentQuote[1]
          }
        }
        
        // 解析公式
        let stepFormula = ''
        const stepFormulaBacktick = stepBlock.match(/formula:\s*`([\s\S]*?)`/)
        if (stepFormulaBacktick) {
          stepFormula = stepFormulaBacktick[1]
        } else {
          const stepFormulaQuote = stepBlock.match(/formula:\s*'((?:[^'\\]|\\.)*)'/)
          if (stepFormulaQuote) {
            stepFormula = stepFormulaQuote[1]
          }
        }
        
        if (stepTitleMatch) {
          steps.push({
            title: stepTitleMatch[1],
            content: stepContent.trim(),
            formula: stepFormula.trim()
          })
        }
      }
    }
    
    // 获取 SVG URL
    const svgUrl = getSvgUrl(current.id)
    
    problems[current.id] = {
      id: current.id,
      title,
      difficulty,
      tags,
      methodName,
      svgUrl,
      content,
      steps
    }
  } catch (err) {
    console.error(`解析 ${current.id} 失败:`, err.message)
  }
}

// 统计有步骤的题目
const withSteps = Object.values(problems).filter(p => p.steps.length > 0).length
console.log(`成功解析 ${Object.keys(problems).length} 道题目 (${withSteps} 道有解析步骤)`)

// 生成小程序数据文件
let output = `// problems.js - 题目数据（自动生成）
// 共 ${Object.keys(problems).length} 道题目

const problemData = {
`

// 转义函数
function escapeStr(str) {
  if (!str) return ''
  return str
    .replace(/\\/g, '\\\\')
    .replace(/'/g, "\\'")
    .replace(/\n/g, '\\n')
    .replace(/\r/g, '')
}

for (const [id, problem] of Object.entries(problems)) {
  const svgUrlStr = problem.svgUrl ? `'${problem.svgUrl}'` : 'null'
  const methodNameStr = problem.methodName ? `'${escapeStr(problem.methodName)}'` : 'null'
  const tagsStr = problem.tags.map(t => `'${escapeStr(t)}'`).join(', ')
  
  output += `  '${id}': {
    id: '${id}',
    title: '${escapeStr(problem.title)}',
    difficulty: ${problem.difficulty},
    tags: [${tagsStr}],
    methodName: ${methodNameStr},
    svgUrl: ${svgUrlStr},
    content: '${escapeStr(problem.content)}',
    steps: [
`
  
  for (const step of problem.steps) {
    output += `      { title: '${escapeStr(step.title)}', content: '${escapeStr(step.content)}', formula: '${escapeStr(step.formula)}' },
`
  }
  
  output += `    ]
  },
`
}

output += `}

/**
 * 根据ID获取题目
 */
function getProblemById(id) {
  return problemData[id] || null
}

/**
 * 获取某个考法的针对训练
 */
function getTrainingsByTechnique(exampleId) {
  const techId = exampleId.replace('-example', '')
  const trainings = []
  
  for (let i = 1; i <= 10; i++) {
    const trainId = techId + '-train-' + i
    if (problemData[trainId]) {
      trainings.push(problemData[trainId])
    }
  }
  
  return trainings
}

/**
 * 获取专题集训题目
 */
function getQuizProblems(quizType) {
  const problems = []
  for (let i = 1; i <= 20; i++) {
    const quizId = quizType + '-quiz-' + i
    if (problemData[quizId]) {
      problems.push(problemData[quizId])
    }
  }
  return problems
}

/**
 * 获取期末冲刺练题目
 */
function getFinalQuizProblems() {
  const problems = []
  for (let i = 1; i <= 20; i++) {
    const quizId = 'final-quiz-' + i
    if (problemData[quizId]) {
      problems.push(problemData[quizId])
    }
  }
  return problems
}

/**
 * 获取所有题目ID
 */
function getAllProblemIds() {
  return Object.keys(problemData)
}

module.exports = {
  problemData,
  getProblemById,
  getTrainingsByTechnique,
  getQuizProblems,
  getFinalQuizProblems,
  getAllProblemIds
}
`

// 写入文件
const outputPath = path.join(__dirname, '../apps/miniprogram/data/problems.js')
fs.writeFileSync(outputPath, output)
console.log(`已生成: ${outputPath}`)
