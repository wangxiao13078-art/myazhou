#!/usr/bin/env node
/**
 * 压缩 problems.js 文件
 * 移除多余空白，优化JSON结构
 */

const fs = require('fs');
const path = require('path');

const inputPath = path.join(__dirname, '../apps/miniprogram/data/problems.js');
const outputPath = path.join(__dirname, '../apps/miniprogram/data/problems.min.js');

// 读取原始文件
let content = fs.readFileSync(inputPath, 'utf-8');

// 提取 problemData 对象
const dataMatch = content.match(/const problemData = (\{[\s\S]*?\});/);
if (!dataMatch) {
  console.error('无法找到 problemData');
  process.exit(1);
}

// 解析JSON
let problemData;
try {
  // 使用 eval 因为是 JS 对象格式
  eval('problemData = ' + dataMatch[1]);
} catch (e) {
  console.error('解析失败:', e.message);
  process.exit(1);
}

// 统计原始大小
const originalSize = Buffer.byteLength(content, 'utf-8');
console.log(`原始大小: ${(originalSize / 1024).toFixed(1)} KB`);

// 优化：缩短字段名
const fieldMap = {
  'difficulty': 'd',
  'methodName': 'm',
  'svgUrl': 's',
  'content': 'c',
  'steps': 'st',
  'title': 't',
  'formula': 'f',
  'tags': 'tg'
};

// 压缩每个题目
const minifiedData = {};
for (const [id, problem] of Object.entries(problemData)) {
  const minProblem = {
    id: problem.id,
    t: problem.title,
    d: problem.difficulty,
    tg: problem.tags,
    m: problem.methodName,
    s: problem.svgUrl,
    c: problem.content,
    st: problem.steps ? problem.steps.map(step => ({
      t: step.title,
      c: step.content,
      f: step.formula || ''
    })) : []
  };
  minifiedData[id] = minProblem;
}

// 生成压缩后的JS
const minifiedJson = JSON.stringify(minifiedData);

// 添加解压映射函数
const outputContent = `// problems.min.js - 压缩版题目数据
// 字段映射: t=title, d=difficulty, tg=tags, m=methodName, s=svgUrl, c=content, st=steps, f=formula
const _pd=${minifiedJson};

// 展开函数
function _e(p){return{id:p.id,title:p.t,difficulty:p.d,tags:p.tg||[],methodName:p.m,svgUrl:p.s,content:p.c,steps:(p.st||[]).map(s=>({title:s.t,content:s.c,formula:s.f}))};}

// 获取题目
function getProblemById(id){const p=_pd[id];return p?_e(p):null;}

// 获取训练题
function getTrainingsByTechnique(exampleId){
  const prefix=exampleId.replace('-example','');
  return Object.keys(_pd).filter(k=>k.startsWith(prefix+'-train')).map(k=>_e(_pd[k]));
}

// 获取专题集训题目
function getQuizProblems(quizId){
  const prefix=quizId+'-quiz';
  return Object.keys(_pd).filter(k=>k.startsWith(prefix)).map(k=>_e(_pd[k]));
}

// 获取期末冲刺题目
function getFinalQuizProblems(){
  return Object.keys(_pd).filter(k=>k.startsWith('final-')).map(k=>_e(_pd[k]));
}

// 获取所有题目
function getAllProblems(){return Object.keys(_pd).map(k=>_e(_pd[k]));}

module.exports={getProblemById,getTrainingsByTechnique,getQuizProblems,getFinalQuizProblems,getAllProblems};
`;

// 写入压缩文件
fs.writeFileSync(outputPath, outputContent);

const newSize = Buffer.byteLength(outputContent, 'utf-8');
console.log(`压缩后大小: ${(newSize / 1024).toFixed(1)} KB`);
console.log(`节省: ${((originalSize - newSize) / 1024).toFixed(1)} KB (${((1 - newSize/originalSize) * 100).toFixed(1)}%)`);
console.log(`\n已生成: ${outputPath}`);

