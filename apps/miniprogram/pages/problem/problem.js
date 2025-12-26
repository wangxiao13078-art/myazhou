// problem.js - 题目详情页逻辑
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
    svgPath: ''
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
    console.log('原始内容前100字符:', problem.content.substring(0, 100))

    // 处理数学公式 - 转换为纯文本
    const contentText = mathUtils.renderMath(problem.content)
    console.log('转换后内容前100字符:', contentText.substring(0, 100))
    const stepTexts = problem.steps.map(step => mathUtils.renderMath(step.content))
    const formulaTexts = problem.steps.map(step => 
      step.formula ? mathUtils.formatFormula(step.formula) : ''
    )

    // 获取针对训练
    const trainings = problems.getTrainingsByTechnique(id)
    console.log('针对训练数量:', trainings.length)

    // 处理SVG路径 - 使用相对路径
    let svgPath = ''
    if (problem.svgUrl) {
      // svgUrl格式: /images/svg/xxx.svg
      // 转换为相对路径: ../../images/svg/xxx.svg
      svgPath = problem.svgUrl.replace('/images/', '../../images/')
      console.log('SVG路径:', svgPath)
    }

    this.setData({
      problemId: id,
      problem: problem,
      contentText: contentText,
      stepTexts: stepTexts,
      formulaTexts: formulaTexts,
      trainings: trainings,
      hasNext: trainings.length > 0,
      svgPath: svgPath
    })

    // 设置导航栏标题
    wx.setNavigationBarTitle({
      title: problem.title.length > 15 ? problem.title.substring(0, 15) + '...' : problem.title
    })
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
  }
})
