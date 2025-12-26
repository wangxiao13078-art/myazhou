// quiz.js - 专题集训页逻辑
const problems = require('../../data/problems.js')

Page({
  data: {
    quizList: [],
    finalQuizList: [],
    currentQuiz: null,
    showQuizDetail: false
  },

  onLoad(options) {
    console.log('quiz页面加载')
    
    // 加载专题集训数据
    const quizList = [
      { id: 'z1', name: '专题一集训', icon: '📊', color: '#3B82F6' },
      { id: 'z2', name: '专题二集训', icon: '🔢', color: '#10B981' },
      { id: 'z3', name: '专题三集训', icon: '📐', color: '#F59E0B' },
      { id: 'z4', name: '专题四集训', icon: '➕', color: '#EF4444' },
      { id: 'z5', name: '专题五集训', icon: '⚖️', color: '#8B5CF6' },
      { id: 'z6', name: '专题六集训', icon: '📏', color: '#EC4899' }
    ]

    // 计算每个集训的题目数
    for (const quiz of quizList) {
      const quizProblems = problems.getQuizProblems(quiz.id)
      quiz.count = quizProblems.length
      quiz.problems = quizProblems
    }

    // 加载期末冲刺数据
    const finalQuizList = problems.getFinalQuizProblems()
    console.log('期末冲刺题目数:', finalQuizList.length)

    this.setData({
      quizList,
      finalQuizList
    })
  },

  // 显示专题集训题目列表
  showQuizProblems(e) {
    const id = e.currentTarget.dataset.id
    const quiz = this.data.quizList.find(q => q.id === id)
    
    if (quiz) {
      this.setData({
        currentQuiz: quiz,
        showQuizDetail: true
      })
    }
  },

  // 隐藏题目列表
  hideQuizDetail() {
    this.setData({
      showQuizDetail: false,
      currentQuiz: null
    })
  },

  // 开始做题（分包路径）
  startProblem(e) {
    const id = e.currentTarget.dataset.id
    wx.navigateTo({
      url: `/packageA/pages/problem/problem?id=${id}`
    })
  },

  // 开始期末冲刺（分包路径）
  startFinalQuiz() {
    wx.navigateTo({
      url: '/packageA/pages/final/final'
    })
  }
})
