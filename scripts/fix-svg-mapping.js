// fix-svg-mapping.js - 修正题目的SVG映射
const fs = require('fs');
const path = require('path');

// 读取可用的SVG文件
const svgDir = path.join(__dirname, '../packages/svg_figures');
const svgFiles = fs.readdirSync(svgDir)
  .filter(f => f.endsWith('.svg'))
  .map(f => f.replace('.svg', ''));

console.log('可用SVG文件数:', svgFiles.length);

// 创建映射表：题目ID -> SVG文件名
const svgMapping = {};
const baseUrl = 'https://wangxiao13078-art.github.io/myazhou/svg/';

for (const svg of svgFiles) {
  // t1_example -> t1-example
  const problemId = svg.replace(/_/g, '-');
  svgMapping[problemId] = svg + '.svg';
}

// 读取 problems.js
const problemsPath = path.join(__dirname, '../apps/miniprogram/data/problems.js');
let problemsContent = fs.readFileSync(problemsPath, 'utf-8');

// 统计
let updated = 0;
let notFound = [];

// 遍历所有题目ID，更新svgUrl
const problemIdRegex = /'([t\d]+-(?:example|train-?\d*))'/g;
let match;
const problemIds = new Set();

while ((match = problemIdRegex.exec(problemsContent)) !== null) {
  problemIds.add(match[1]);
}

console.log('题目ID数:', problemIds.size);

// 更新每个题目的svgUrl
for (const problemId of problemIds) {
  const svgFile = svgMapping[problemId];
  
  if (svgFile) {
    const newUrl = baseUrl + svgFile;
    // 查找并替换该题目的svgUrl
    const regex = new RegExp(
      `('${problemId}':\\s*\\{[^}]*svgUrl:\\s*)([^,]+)(,)`,
      'g'
    );
    
    const oldContent = problemsContent;
    problemsContent = problemsContent.replace(regex, (match, before, oldUrl, after) => {
      updated++;
      return before + "'" + newUrl + "'" + after;
    });
  } else {
    // 检查是否有类似的文件
    const baseName = problemId.replace(/-train-?\d*$/, '').replace(/-example$/, '');
    const possibleFiles = svgFiles.filter(f => f.startsWith(baseName.replace(/-/g, '_')));
    if (possibleFiles.length === 0) {
      notFound.push(problemId);
    }
  }
}

// 写回文件
fs.writeFileSync(problemsPath, problemsContent);

console.log('');
console.log('更新完成!');
console.log('更新的题目数:', updated);
console.log('');
console.log('没有找到对应SVG的题目:');
notFound.forEach(id => console.log('  -', id));

