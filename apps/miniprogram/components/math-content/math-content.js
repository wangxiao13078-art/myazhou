// math-content.js - 数学内容渲染组件
const mathUtils = require('../../utils/math.js')

Component({
  properties: {
    // 原始内容（可包含LaTeX）
    content: {
      type: String,
      value: '',
      observer: 'processContent'
    },
    // 是否启用富文本模式（支持内嵌图形）
    richMode: {
      type: Boolean,
      value: false
    },
    // 是否可选择
    selectable: {
      type: Boolean,
      value: true
    },
    // 图片基础路径
    imagePath: {
      type: String,
      value: '../../images/svg/'
    }
  },

  data: {
    displayText: '',
    contentParts: []
  },

  lifetimes: {
    attached() {
      this.processContent()
    }
  },

  methods: {
    /**
     * 处理内容
     */
    processContent() {
      const content = this.properties.content
      if (!content) {
        this.setData({ displayText: '', contentParts: [] })
        return
      }

      if (this.properties.richMode) {
        this.processRichContent(content)
      } else {
        this.processSimpleContent(content)
      }
    },

    /**
     * 简单模式：直接转换文本
     */
    processSimpleContent(content) {
      const displayText = mathUtils.renderMath(content)
      this.setData({ displayText })
    },

    /**
     * 富文本模式：解析图片和特殊格式
     */
    processRichContent(content) {
      const parts = []
      let text = content

      // 处理图片引用 [图:xxx.svg] 或 [图形:xxx]
      const imagePattern = /\[图[:：]([^\]]+)\]/g
      let lastIndex = 0
      let match

      while ((match = imagePattern.exec(content)) !== null) {
        // 添加图片前的文本
        if (match.index > lastIndex) {
          const textBefore = content.substring(lastIndex, match.index)
          if (textBefore.trim()) {
            parts.push({
              type: 'text',
              content: mathUtils.renderMath(textBefore)
            })
          }
        }

        // 添加图片
        const imageName = match[1].trim()
        let imageSrc = imageName
        if (!imageName.startsWith('/') && !imageName.startsWith('http')) {
          imageSrc = this.properties.imagePath + imageName
        }
        parts.push({
          type: 'image',
          src: imageSrc,
          caption: ''
        })

        lastIndex = match.index + match[0].length
      }

      // 添加剩余文本
      if (lastIndex < content.length) {
        const remainingText = content.substring(lastIndex)
        if (remainingText.trim()) {
          parts.push({
            type: 'text',
            content: mathUtils.renderMath(remainingText)
          })
        }
      }

      // 如果没有特殊格式，作为普通文本处理
      if (parts.length === 0) {
        parts.push({
          type: 'text',
          content: mathUtils.renderMath(content)
        })
      }

      this.setData({ contentParts: parts })
    },

    /**
     * 解析分数（可选：转换为结构化数据用于特殊渲染）
     */
    parseFractions(text) {
      const fractionPattern = /\\frac\s*\{([^{}]+)\}\s*\{([^{}]+)\}/g
      const parts = []
      let lastIndex = 0
      let match

      while ((match = fractionPattern.exec(text)) !== null) {
        if (match.index > lastIndex) {
          parts.push({
            type: 'text',
            content: text.substring(lastIndex, match.index)
          })
        }
        parts.push({
          type: 'fraction',
          numerator: match[1],
          denominator: match[2]
        })
        lastIndex = match.index + match[0].length
      }

      if (lastIndex < text.length) {
        parts.push({
          type: 'text',
          content: text.substring(lastIndex)
        })
      }

      return parts
    }
  }
})

