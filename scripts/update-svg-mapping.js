// update-svg-mapping.js - 更新题目的SVG映射
const fs = require('fs');
const path = require('path');

// 读取所有可用的SVG文件
const svgDir = path.join(__dirname, '../packages/svg_figures');
const svgFiles = fs.readdirSync(svgDir).filter(f => f.endsWith('.svg'));
console.log('找到SVG文件:', svgFiles.length);

// 创建SVG文件名映射（将文件名转换为题目ID格式）
// 例如：t1_example.svg -> t1-example
const svgMap = {};
for (const file of svgFiles) {
  // 提取基础名称（去掉.svg）
  const baseName = file.replace('.svg', '');
  
  // 转换下划线为连字符
  const problemIdFormat = baseName.replace(/_/g, '-');
  
  svgMap[problemIdFormat] = file;
  
  // 也添加一些特殊映射
  if (baseName.startsWith('numberline_t')) {
    // numberline_t1_1 -> 可能对应 t1-train-1
    const match = baseName.match(/numberline_t(\d+)_?(\d*)/);
    if (match) {
      const tNum = match[1];
      const trainNum = match[2];
      if (trainNum) {
        svgMap[`t${tNum}-train-${trainNum}`] = file;
      } else {
        svgMap[`t${tNum}-example`] = file;
      }
    }
  }
}

// 期末冲刺特殊映射
const finalMapping = {
  'final-quiz-1': 'final-1-number-line.svg',
  'final-quiz-2': 'final-2-cube.svg',
  'final-quiz-4': 'final-4-triangles.svg',
  'final-quiz-11': 'final-11-segment.svg',
  'final-quiz-12': 'final-12-angle.svg',
  'final-quiz-15': 'final-15-number-line.svg',
  'final-quiz-16': 'final-16-figure1.svg'
};

// 基础URL
const baseUrl = 'https://wangxiao13078-art.github.io/myazhou/svg/';

// 读取problems.js
const problemsPath = path.join(__dirname, '../apps/miniprogram/data/problems.js');
const problemsModule = require(problemsPath);
const problemData = problemsModule.problemData;

console.log('题目总数:', Object.keys(problemData).length);

// 更新每个题目的svgUrl
let updatedCount = 0;
let withSvgCount = 0;
const noSvgProblems = [];

for (const [problemId, problem] of Object.entries(problemData)) {
  let svgFile = null;
  
  // 1. 检查期末冲刺映射
  if (finalMapping[problemId]) {
    svgFile = finalMapping[problemId];
  }
  // 2. 检查直接匹配
  else if (svgMap[problemId]) {
    svgFile = svgMap[problemId];
  }
  // 3. 尝试将problemId转换为SVG文件名格式
  else {
    const possibleFileName = problemId.replace(/-/g, '_') + '.svg';
    if (svgFiles.includes(possibleFileName)) {
      svgFile = possibleFileName;
    }
  }
  
  if (svgFile) {
    const newUrl = baseUrl + svgFile;
    if (problem.svgUrl !== newUrl) {
      problem.svgUrl = newUrl;
      updatedCount++;
    }
    withSvgCount++;
  } else {
    if (problem.svgUrl) {
      // 检查现有的svgUrl是否有效
      const existingSvg = problem.svgUrl.split('/').pop();
      if (!svgFiles.includes(existingSvg)) {
        problem.svgUrl = null;
        updatedCount++;
      } else {
        withSvgCount++;
      }
    }
    noSvgProblems.push(problemId);
  }
}

// 重新生成problems.js
const newProblemsContent = `// problems.js - 题目数据（自动生成）
// 共 ${Object.keys(problemData).length} 道题目

const problemData = ${JSON.stringify(problemData, null, 2)};

/**
 * 根据ID获取题目
 */
function getProblemById(id) {
  return problemData[id];
}

/**
 * 获取某个考法下的例题
 */
function getExampleByTechnique(techniqueId) {
  const exampleId = techniqueId + '-example';
  return problemData[exampleId];
}

/**
 * 获取某个考法下的针对训练
 */
function getTrainingsByTechnique(techniqueId) {
  const trainings = [];
  let i = 1;
  while (true) {
    const trainingId = techniqueId + '-train-' + i;
    if (problemData[trainingId]) {
      trainings.push(problemData[trainingId]);
      i++;
    } else {
      break;
    }
  }
  return trainings;
}

/**
 * 获取某个专题集训的题目
 */
function getQuizProblems(quizId) {
  const problems = [];
  let i = 1;
  while (true) {
    const problemId = quizId + '-quiz-' + i;
    if (problemData[problemId]) {
      problems.push(problemData[problemId]);
      i++;
    } else {
      break;
    }
  }
  return problems;
}

/**
 * 获取期末冲刺练题目
 */
function getFinalQuizProblems() {
  const problems = [];
  for (let i = 1; i <= 16; i++) {
    const quizId = 'final-quiz-' + i;
    if (problemData[quizId]) {
      problems.push(problemData[quizId]);
    }
  }
  return problems;
}

/**
 * 获取所有题目ID
 */
function getAllProblemIds() {
  return Object.keys(problemData);
}

module.exports = {
  problemData,
  getProblemById,
  getExampleByTechnique,
  getTrainingsByTechnique,
  getQuizProblems,
  getFinalQuizProblems,
  getAllProblemIds
};
`;

fs.writeFileSync(problemsPath, newProblemsContent);

console.log('\n=== 更新完成 ===');
console.log('更新的题目数:', updatedCount);
console.log('有SVG的题目:', withSvgCount);
console.log('无SVG的题目:', noSvgProblems.length);

// 按专题分组统计无SVG的题目
const noSvgByChapter = {};
for (const id of noSvgProblems) {
  const match = id.match(/t(\d+)/);
  if (match) {
    const tNum = parseInt(match[1]);
    let chapter;
    if (tNum <= 7) chapter = '专题一';
    else if (tNum <= 10) chapter = '专题二';
    else if (tNum <= 20) chapter = '专题三';
    else if (tNum <= 24) chapter = '专题四';
    else if (tNum <= 31 || (tNum >= 38 && tNum <= 44)) chapter = '专题五';
    else if (tNum <= 37) chapter = '专题六';
    else chapter = '其他';
    
    if (!noSvgByChapter[chapter]) noSvgByChapter[chapter] = [];
    noSvgByChapter[chapter].push(id);
  } else if (id.startsWith('z')) {
    const chapter = '专题集训';
    if (!noSvgByChapter[chapter]) noSvgByChapter[chapter] = [];
    noSvgByChapter[chapter].push(id);
  } else if (id.startsWith('final')) {
    const chapter = '期末冲刺';
    if (!noSvgByChapter[chapter]) noSvgByChapter[chapter] = [];
    noSvgByChapter[chapter].push(id);
  }
}

console.log('\n无SVG题目分布:');
for (const [chapter, problems] of Object.entries(noSvgByChapter)) {
  console.log(`${chapter}: ${problems.length}题`);
}

