// update-local-svg.js - 更新题目的SVG为本地路径
const fs = require('fs');
const path = require('path');

// 读取所有可用的SVG文件
const svgDir = path.join(__dirname, '../apps/miniprogram/images/svg');
const svgFiles = fs.readdirSync(svgDir).filter(f => f.endsWith('.svg'));
console.log('找到本地SVG文件:', svgFiles.length);

// 读取problems.js
const problemsPath = path.join(__dirname, '../apps/miniprogram/data/problems.js');
const problemsModule = require(problemsPath);
const problemData = { ...problemsModule.problemData };

// 本地路径前缀
const localPrefix = '/images/svg/';

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

// 更新每个题目的svgUrl
let updatedCount = 0;
let withSvgCount = 0;

for (const [problemId, problem] of Object.entries(problemData)) {
  let svgFile = null;
  
  // 1. 检查期末冲刺映射
  if (finalMapping[problemId]) {
    svgFile = finalMapping[problemId];
  }
  // 2. 尝试将problemId转换为SVG文件名格式
  else {
    const possibleFileName = problemId.replace(/-/g, '_') + '.svg';
    if (svgFiles.includes(possibleFileName)) {
      svgFile = possibleFileName;
    }
  }
  
  if (svgFile && svgFiles.includes(svgFile)) {
    const newUrl = localPrefix + svgFile;
    if (problem.svgUrl !== newUrl) {
      problem.svgUrl = newUrl;
      updatedCount++;
    }
    withSvgCount++;
  } else {
    problem.svgUrl = null;
  }
}

// 重新生成problems.js
const newProblemsContent = `// problems.js - 题目数据（自动生成）
// 共 ${Object.keys(problemData).length} 道题目
// SVG使用本地路径

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
console.log('有本地SVG的题目:', withSvgCount);

