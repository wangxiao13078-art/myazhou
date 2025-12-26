#!/usr/bin/env node
/**
 * 深度优化 problems.js
 * 1. 预转换LaTeX为Unicode
 * 2. 压缩JSON
 * 3. 移除不必要字段
 */

const fs = require('fs');
const path = require('path');

const inputPath = path.join(__dirname, '../apps/miniprogram/data/problems.js');
const outputPath = path.join(__dirname, '../apps/miniprogram/data/problems.js');
const backupPath = path.join(__dirname, '../apps/miniprogram/data/problems.backup.js');

// LaTeX到Unicode的转换
function convertLatex(text) {
  if (!text) return text;
  
  let result = text;
  
  // 统一反斜杠
  result = result.replace(/\\\\/g, '\\');
  
  // 移除 $...$ 符号但保留内容
  result = result.replace(/\$\$([^$]+)\$\$/g, '$1');
  result = result.replace(/\$([^$]+)\$/g, '$1');
  
  // 分数 \frac{a}{b} -> a/b
  for (let i = 0; i < 5; i++) {
    result = result.replace(/\\frac\s*\{([^{}]*)\}\s*\{([^{}]*)\}/g, (m, n, d) => {
      return `${n.trim()}/${d.trim()}`;
    });
  }
  
  // 文本命令
  result = result.replace(/\\text\s*\{([^{}]*)\}/g, '$1');
  result = result.replace(/\\textbf\s*\{([^{}]*)\}/g, '$1');
  result = result.replace(/\\mathrm\s*\{([^{}]*)\}/g, '$1');
  result = result.replace(/\\rm\s*\{([^{}]*)\}/g, '$1');
  
  // 几何符号
  result = result.replace(/\\angle/g, '∠');
  result = result.replace(/\\triangle/g, '△');
  result = result.replace(/\\parallel/g, '∥');
  result = result.replace(/\\perp/g, '⊥');
  result = result.replace(/\\circ/g, '°');
  result = result.replace(/\\degree/g, '°');
  
  // 运算符
  result = result.replace(/\\times/g, '×');
  result = result.replace(/\\div/g, '÷');
  result = result.replace(/\\pm/g, '±');
  result = result.replace(/\\cdot/g, '·');
  
  // 比较符号
  result = result.replace(/\\leq/g, '≤');
  result = result.replace(/\\le(?![a-z])/g, '≤');
  result = result.replace(/\\geq/g, '≥');
  result = result.replace(/\\ge(?![a-z])/g, '≥');
  result = result.replace(/\\neq/g, '≠');
  result = result.replace(/\\ne(?![a-z])/g, '≠');
  result = result.replace(/\\approx/g, '≈');
  
  // 希腊字母
  result = result.replace(/\\pi(?![a-z])/g, 'π');
  result = result.replace(/\\alpha/g, 'α');
  result = result.replace(/\\beta/g, 'β');
  result = result.replace(/\\theta/g, 'θ');
  
  // 省略号
  result = result.replace(/\\cdots/g, '⋯');
  result = result.replace(/\\ldots/g, '…');
  
  // 根号
  result = result.replace(/\\sqrt\s*\{([^{}]+)\}/g, '√($1)');
  result = result.replace(/\\sqrt/g, '√');
  
  // 逻辑符号
  result = result.replace(/\\therefore/g, '∴');
  result = result.replace(/\\because/g, '∵');
  
  // 箭头
  result = result.replace(/\\Rightarrow/g, '⇒');
  result = result.replace(/\\rightarrow/g, '→');
  result = result.replace(/\\to(?![a-z])/g, '→');
  
  // 上标下标 (简单处理)
  const superscripts = {'0':'⁰','1':'¹','2':'²','3':'³','4':'⁴','5':'⁵','6':'⁶','7':'⁷','8':'⁸','9':'⁹','n':'ⁿ'};
  const subscripts = {'0':'₀','1':'₁','2':'₂','3':'₃','4':'₄','5':'₅','6':'₆','7':'₇','8':'₈','9':'₉','n':'ₙ'};
  
  result = result.replace(/\^\{([^{}]+)\}/g, (m, exp) => {
    return exp.split('').map(c => superscripts[c] || c).join('');
  });
  result = result.replace(/\^([0-9n])/g, (m, c) => superscripts[c] || c);
  
  result = result.replace(/_\{([^{}]+)\}/g, (m, exp) => {
    return exp.split('').map(c => subscripts[c] || c).join('');
  });
  result = result.replace(/_([0-9n])/g, (m, c) => subscripts[c] || c);
  
  // 括号
  result = result.replace(/\\left\s*\(/g, '(');
  result = result.replace(/\\right\s*\)/g, ')');
  result = result.replace(/\\left\s*\[/g, '[');
  result = result.replace(/\\right\s*\]/g, ']');
  result = result.replace(/\\left/g, '');
  result = result.replace(/\\right/g, '');
  
  // 空格
  result = result.replace(/\\quad/g, '  ');
  result = result.replace(/\\qquad/g, '    ');
  result = result.replace(/\\,/g, ' ');
  result = result.replace(/\\ /g, ' ');
  
  // 清理剩余命令
  result = result.replace(/\\[a-zA-Z]+\s*\{([^{}]*)\}/g, '$1');
  result = result.replace(/\\[a-zA-Z]+/g, '');
  
  // 清理花括号
  result = result.replace(/\{([^{}]*)\}/g, '$1');
  
  // 清理多余空格
  result = result.replace(/  +/g, ' ');
  
  return result.trim();
}

// 读取原始文件
let content = fs.readFileSync(inputPath, 'utf-8');
const originalSize = Buffer.byteLength(content, 'utf-8');
console.log(`原始大小: ${(originalSize / 1024).toFixed(1)} KB`);

// 备份
fs.writeFileSync(backupPath, content);
console.log(`已备份到: problems.backup.js`);

// 提取 problemData
const dataStart = content.indexOf('const problemData = {');
const funcStart = content.indexOf('\nfunction getProblemById');

if (dataStart === -1 || funcStart === -1) {
  console.error('无法找到 problemData, dataStart:', dataStart, 'funcStart:', funcStart);
  process.exit(1);
}

const dataStr = content.substring(dataStart + 'const problemData = '.length, funcStart).trim();

// 解析
let problemData;
try {
  eval('problemData = ' + dataStr);
} catch (e) {
  console.error('解析失败:', e.message);
  process.exit(1);
}

console.log(`题目数量: ${Object.keys(problemData).length}`);

// 优化每个题目
let convertedCount = 0;
for (const id of Object.keys(problemData)) {
  const p = problemData[id];
  
  // 转换内容
  if (p.content) {
    const original = p.content;
    p.content = convertLatex(p.content);
    if (p.content !== original) convertedCount++;
  }
  
  // 转换步骤
  if (p.steps) {
    for (const step of p.steps) {
      if (step.content) step.content = convertLatex(step.content);
      if (step.formula) step.formula = convertLatex(step.formula);
    }
  }
  
  // 移除null值
  if (p.methodName === null) delete p.methodName;
  if (p.svgUrl === null) delete p.svgUrl;
}

console.log(`转换了 ${convertedCount} 道题目的LaTeX公式`);

// 生成新文件
const newDataStr = JSON.stringify(problemData, null, 2);
const functions = content.substring(funcStart);

const newContent = `// problems.js - 题目数据（优化版）
// 共 ${Object.keys(problemData).length} 道题目
// LaTeX已预转换为Unicode

const problemData = ${newDataStr}
${functions}`;

fs.writeFileSync(outputPath, newContent);

const newSize = Buffer.byteLength(newContent, 'utf-8');
console.log(`优化后大小: ${(newSize / 1024).toFixed(1)} KB`);
console.log(`节省: ${((originalSize - newSize) / 1024).toFixed(1)} KB (${((1 - newSize/originalSize) * 100).toFixed(1)}%)`);

