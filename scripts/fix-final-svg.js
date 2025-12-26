// fix-final-svg.js - 修复期末冲刺题目的SVG映射
const fs = require('fs');
const path = require('path');

// 期末冲刺SVG映射
const finalSvgMap = {
  'final-quiz-1': 'final-1-number-line.svg',
  'final-quiz-2': 'final-2-cube.svg',
  'final-quiz-4': 'final-4-triangles.svg',
  'final-quiz-12': 'final-12-angle.svg',
  'final-quiz-15': 'final-15-number-line.svg',
  'final-quiz-16': 'final-16-figure1.svg'
};

const baseUrl = 'https://wangxiao13078-art.github.io/myazhou/svg/';

// 读取 problems.js
const problemsPath = path.join(__dirname, '../apps/miniprogram/data/problems.js');
let content = fs.readFileSync(problemsPath, 'utf-8');

// 更新每个期末冲刺题目
for (const [problemId, svgFile] of Object.entries(finalSvgMap)) {
  const newUrl = baseUrl + svgFile;
  
  // 使用简单的字符串替换
  // 查找模式：'final-quiz-X': {...svgUrl: null,...}
  const searchPattern = `'${problemId}'`;
  const idx = content.indexOf(searchPattern);
  
  if (idx !== -1) {
    // 找到该题目块中的 svgUrl
    const blockStart = idx;
    const blockEnd = content.indexOf('}', blockStart + 100);
    let block = content.substring(blockStart, blockEnd + 1);
    
    // 替换 svgUrl
    const oldBlock = block;
    block = block.replace(/svgUrl:\s*(null|'[^']*')/, `svgUrl: '${newUrl}'`);
    
    if (oldBlock !== block) {
      content = content.substring(0, blockStart) + block + content.substring(blockEnd + 1);
      console.log('更新: ' + problemId + ' -> ' + svgFile);
    }
  }
}

fs.writeFileSync(problemsPath, content);
console.log('\n期末冲刺图形映射完成！');

