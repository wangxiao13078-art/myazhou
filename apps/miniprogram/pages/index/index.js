// index.js - 首页逻辑
const chapters = require('../../data/chapters.js')

Page({
  data: {
    chapters: []
  },

  onLoad() {
    this.setData({
      chapters: chapters.chapterList
    })
  },

  // 跳转到专题页面
  goToChapter(e) {
    const id = e.currentTarget.dataset.id
    wx.navigateTo({
      url: `/pages/chapter/chapter?id=${id}`
    })
  },

  // 跳转到期末冲刺练（独立页面）
  goToFinalQuiz() {
    wx.navigateTo({
      url: '/pages/final/final'
    })
  },

  // 跳转到专题集训
  goToQuiz() {
    wx.switchTab({
      url: '/pages/quiz/quiz'
    })
  }
})
