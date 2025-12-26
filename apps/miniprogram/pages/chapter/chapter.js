// chapter.js - 专题详情页逻辑
const chapters = require('../../data/chapters.js')
const problems = require('../../data/problems.js')

Page({
  data: {
    chapterId: 1,
    chapter: null,
    techniquesWithCount: []
  },

  onLoad(options) {
    const id = parseInt(options.id) || 1
    const chapter = chapters.chapterList.find(c => c.id === id)
    
    if (!chapter) {
      wx.showToast({
        title: '专题不存在',
        icon: 'error'
      })
      return
    }

    // 为每个考法添加训练题数量
    const techniquesWithCount = chapter.techniques.map(tech => {
      // 注意：getTrainingsByTechnique 期望的参数是 techniqueId (如 t8)，不是 t8-example
      const trainings = problems.getTrainingsByTechnique(tech.id)
      return {
        ...tech,
        trainCount: trainings.length
      }
    })
    
    this.setData({
      chapterId: id,
      chapter: chapter,
      techniquesWithCount: techniquesWithCount
    })

    // 设置导航栏标题
    wx.setNavigationBarTitle({
      title: chapter.name
    })

    // 设置导航栏颜色
    wx.setNavigationBarColor({
      frontColor: '#ffffff',
      backgroundColor: chapter.color
    })
  },

  // 跳转到题目详情（分包路径）
  goToProblem(e) {
    const id = e.currentTarget.dataset.id
    wx.navigateTo({
      url: `/packageA/pages/problem/problem?id=${id}-example`
    })
  },

  // 跳转到专题集训
  goToQuiz() {
    const quizId = 'z' + this.data.chapterId
    const quizProblems = problems.getQuizProblems(quizId)
    
    if (quizProblems.length === 0) {
      wx.showToast({
        title: '暂无集训题目',
        icon: 'none'
      })
      return
    }

    // 直接跳转到第一题（分包路径）
    wx.navigateTo({
      url: `/packageA/pages/problem/problem?id=${quizId}-quiz-1`
    })
  }
})
