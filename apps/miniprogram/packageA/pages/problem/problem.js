// problem.js - 题目详情页逻辑（分包版）
const problems = require('../../data/problems.js')

Page({
  data: {
    problemId: '',
    problem: null,
    unlockedSteps: {},
    trainings: [],
    hasNext: false,
    svgPath: '',
    figures: []
  },

  onLoad(options) {
    const id = options.id || 't1-example'
    console.log('加载题目:', id)
    
    const problem = problems.getProblemById(id)
    
    if (!problem) {
      console.error('题目不存在:', id)
      wx.showToast({
        title: '题目不存在: ' + id,
        icon: 'none',
        duration: 2000
      })
      return
    }

    console.log('题目数据:', problem.title)

    // 获取针对训练
    const trainings = problems.getTrainingsByTechnique(id)
    console.log('针对训练数量:', trainings.length)

    // 处理SVG路径 - 分包访问主包图片
    let svgPath = ''
    if (problem.svgUrl) {
      // 分包访问主包资源需要完整路径
      svgPath = problem.svgUrl
      console.log('SVG路径:', svgPath)
    }

    // 处理多图形
    const figures = this.extractFigures(problem)

    this.setData({
      problemId: id,
      problem: problem,
      trainings: trainings,
      hasNext: trainings.length > 0,
      svgPath: svgPath,
      figures: figures
    })

    // 设置导航栏标题
    wx.setNavigationBarTitle({
      title: problem.title.length > 15 ? problem.title.substring(0, 15) + '...' : problem.title
    })
  },

  extractFigures(problem) {
    const figures = []
    
    if (problem.figures && Array.isArray(problem.figures)) {
      problem.figures.forEach((fig, index) => {
        figures.push({
          src: fig.url,
          label: fig.label || `图${index + 1}`
        })
      })
    }
    
    return figures
  },

  toggleStep(e) {
    const index = e.currentTarget.dataset.index
    const key = `unlockedSteps.${index}`
    this.setData({
      [key]: !this.data.unlockedSteps[index]
    })
  },

  goToTraining(e) {
    const id = e.currentTarget.dataset.id
    wx.navigateTo({
      url: `/packageA/pages/problem/problem?id=${id}`
    })
  },

  nextProblem() {
    if (this.data.trainings.length > 0) {
      wx.navigateTo({
        url: `/packageA/pages/problem/problem?id=${this.data.trainings[0].id}`
      })
    }
  },

  goBack() {
    wx.navigateBack()
  },

  addToWrongBook() {
    wx.showToast({
      title: '已加入错题本',
      icon: 'success'
    })
  },

  onSvgLoad(e) {
    console.log('SVG加载成功:', this.data.svgPath)
  },

  onSvgError(e) {
    console.error('SVG加载失败:', this.data.svgPath, e.detail)
    this.setData({ svgPath: '' })
  }
})
