// problem.js - 题目详情页逻辑（增强版）
const problems = require('../../data/problems.js')
const mathUtils = require('../../utils/math.js')

Page({
  data: {
    problemId: '',
    problem: null,
    contentText: '',
    stepTexts: [],
    formulaTexts: [],
    unlockedSteps: {},
    trainings: [],
    hasNext: false,
    svgPath: '',
    figures: []  // 多图形支持
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

    // 处理SVG路径 - 使用相对路径
    let svgPath = ''
    if (problem.svgUrl) {
      svgPath = problem.svgUrl.replace('/images/', '/images/')
      console.log('SVG路径:', svgPath)
    }

    // 处理多图形（如果题目有多张图）
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

  /**
   * 提取题目中的多个图形
   */
  extractFigures(problem) {
    const figures = []
    
    // 检查是否有额外图形
    if (problem.figures && Array.isArray(problem.figures)) {
      problem.figures.forEach((fig, index) => {
        figures.push({
          src: fig.url.replace('/images/', '/images/'),
          label: fig.label || `图${index + 1}`
        })
      })
    }
    
    // 从内容中提取图形引用
    const content = problem.content || ''
    const figurePattern = /\[图(\d+)[：:]([^\]]+)\]/g
    let match
    while ((match = figurePattern.exec(content)) !== null) {
      const figNum = match[1]
      const figDesc = match[2]
      // 查找对应的SVG
      const svgName = `${problem.id.replace(/-/g, '_')}_fig${figNum}.svg`
      figures.push({
        src: `/images/svg/${svgName}`,
        label: `图${figNum}`
      })
    }
    
    return figures
  },

  // 切换步骤展示
  toggleStep(e) {
    const index = e.currentTarget.dataset.index
    const key = `unlockedSteps.${index}`
    this.setData({
      [key]: !this.data.unlockedSteps[index]
    })
  },

  // 跳转到训练题
  goToTraining(e) {
    const id = e.currentTarget.dataset.id
    wx.navigateTo({
      url: `/pages/problem/problem?id=${id}`
    })
  },

  // 下一题
  nextProblem() {
    if (this.data.trainings.length > 0) {
      wx.navigateTo({
        url: `/pages/problem/problem?id=${this.data.trainings[0].id}`
      })
    }
  },

  // 返回
  goBack() {
    wx.navigateBack()
  },

  // 加入错题本
  addToWrongBook() {
    wx.showToast({
      title: '已加入错题本',
      icon: 'success'
    })
  },

  // SVG加载成功
  onSvgLoad(e) {
    console.log('SVG加载成功:', this.data.svgPath)
  },

  // SVG加载失败
  onSvgError(e) {
    console.error('SVG加载失败:', this.data.svgPath, e.detail)
    // 隐藏图形卡片
    this.setData({ svgPath: '' })
  }
})
