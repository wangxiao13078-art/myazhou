// problems.js - 主包精简版（只含索引）
// 完整题目数据在分包 packageA/data/problems.js

// 题目索引（只有ID，用于计数）
const problemIndex = {
  // 专题一：t1-t7
  t1: { example: 1, train: 7 },
  t2: { example: 1, train: 3 },
  t3: { example: 1, train: 3 },
  t4: { example: 1, train: 2 },
  t5: { example: 1, train: 6 },
  t6: { example: 1, train: 2 },
  t7: { example: 1, train: 2 },
  // 专题二：t8-t15
  t8: { example: 1, train: 1 },
  t9: { example: 1, train: 2 },
  t10: { example: 1, train: 1 },
  t11: { example: 1, train: 1 },
  t12: { example: 1, train: 2 },
  t13: { example: 1, train: 2 },
  t14: { example: 1, train: 1 },
  t15: { example: 1, train: 1 },
  // 专题三：t16-t20
  t16: { example: 1, train: 1 },
  t17: { example: 1, train: 1 },
  t18: { example: 1, train: 1 },
  t19: { example: 1, train: 3 },
  t20: { example: 1, train: 1 },
  // 专题四：t21-t24
  t21: { example: 1, train: 1 },
  t22: { example: 1, train: 1 },
  t23: { example: 1, train: 1 },
  t24: { example: 1, train: 1 },
  // 专题五：t25-t31, t38-t44
  t25: { example: 1, train: 1 },
  t26: { example: 1, train: 1 },
  t27: { example: 1, train: 1 },
  t28: { example: 1, train: 1 },
  t29: { example: 1, train: 1 },
  t30: { example: 1, train: 1 },
  t31: { example: 1, train: 1 },
  // 专题六：t32-t37
  t32: { example: 1, train: 2 },
  t33: { example: 1, train: 2 },
  t34: { example: 1, train: 2 },
  t35: { example: 1, train: 4 },
  t36: { example: 1, train: 2 },
  t37: { example: 1, train: 3 }
};

// 专题集训题目数
const quizCounts = {
  z1: 9,
  z2: 14,
  z3: 13,
  z4: 14,
  z5: 10,
  z6: 14
};

// 期末冲刺题目数
const finalCount = 16;

/**
 * 获取某个考法的针对训练（返回简单列表用于显示）
 */
function getTrainingsByTechnique(techniqueId) {
  // 处理 t1-example 形式
  const techId = techniqueId.replace('-example', '');
  const info = problemIndex[techId];
  if (!info) return [];
  
  const trainings = [];
  for (let i = 1; i <= info.train; i++) {
    trainings.push({
      id: techId + '-train-' + i,
      title: '针对训练' + i
    });
  }
  return trainings;
}

/**
 * 获取某个专题集训的题目列表
 */
function getQuizProblems(quizId) {
  const count = quizCounts[quizId] || 0;
  const problems = [];
  for (let i = 1; i <= count; i++) {
    problems.push({
      id: quizId + '-quiz-' + i,
      title: '第' + i + '题'
    });
  }
  return problems;
}

/**
 * 获取期末冲刺练题目列表
 */
function getFinalQuizProblems() {
  const problems = [];
  for (let i = 1; i <= finalCount; i++) {
    problems.push({
      id: 'final-quiz-' + i,
      title: '第' + i + '题'
    });
  }
  return problems;
}

module.exports = {
  getTrainingsByTechnique,
  getQuizProblems,
  getFinalQuizProblems
};

