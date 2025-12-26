// final.js - 期末冲刺练页面（分包版）
const problems = require('../../data/problems.js')

Page({
  data: {
    problemList: []
  },

  onLoad() {
    console.log('期末冲刺页面加载')
    const problemList = problems.getFinalQuizProblems()
    console.log('加载题目数:', problemList.length)
    
    this.setData({ problemList })
  },

  // 进入题目详情
  goToProblem(e) {
    const id = e.currentTarget.dataset.id
    wx.navigateTo({
      url: `/packageA/pages/problem/problem?id=${id}`
    })
  }
})
