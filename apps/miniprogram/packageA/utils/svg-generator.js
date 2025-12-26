// svg-generator.js - SVG几何图形生成器
// 用于动态生成数轴、线段、角度等几何图形

/**
 * 生成数轴SVG
 * @param {Object} options - 配置选项
 * @param {number} options.min - 数轴最小值
 * @param {number} options.max - 数轴最大值
 * @param {Array} options.points - 标记点数组 [{value, label, color}]
 * @param {number} options.width - SVG宽度
 * @param {number} options.height - SVG高度
 */
function generateNumberLine(options = {}) {
  const {
    min = -5,
    max = 5,
    points = [],
    width = 400,
    height = 80,
    showTicks = true,
    showArrow = true
  } = options

  const margin = 40
  const lineY = height / 2
  const range = max - min
  const scale = (width - 2 * margin) / range

  const valueToX = (val) => margin + (val - min) * scale

  let svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}">\n`
  
  // 背景
  svg += `  <rect width="${width}" height="${height}" fill="none"/>\n`

  // 主轴线
  svg += `  <line x1="${margin - 10}" y1="${lineY}" x2="${width - margin + 10}" y2="${lineY}" stroke="#333" stroke-width="2"/>\n`

  // 箭头
  if (showArrow) {
    svg += `  <polygon points="${width - margin + 10},${lineY} ${width - margin},${lineY - 5} ${width - margin},${lineY + 5}" fill="#333"/>\n`
  }

  // 刻度线和数字
  if (showTicks) {
    for (let i = min; i <= max; i++) {
      const x = valueToX(i)
      svg += `  <line x1="${x}" y1="${lineY - 5}" x2="${x}" y2="${lineY + 5}" stroke="#333" stroke-width="1.5"/>\n`
      svg += `  <text x="${x}" y="${lineY + 20}" font-family="Arial" font-size="12" text-anchor="middle">${i}</text>\n`
    }
  }

  // 原点标记
  const originX = valueToX(0)
  if (min <= 0 && max >= 0) {
    svg += `  <text x="${originX}" y="${lineY + 32}" font-family="Arial" font-size="11" text-anchor="middle" fill="#666">O</text>\n`
  }

  // 标记点
  points.forEach((point, index) => {
    const x = valueToX(point.value)
    const color = point.color || '#2196F3'
    const label = point.label || ''
    
    svg += `  <circle cx="${x}" cy="${lineY}" r="4" fill="${color}"/>\n`
    if (label) {
      const labelY = index % 2 === 0 ? lineY - 12 : lineY + 28
      svg += `  <text x="${x}" y="${labelY}" font-family="Arial" font-size="13" text-anchor="middle" fill="${color}">${label}</text>\n`
    }
  })

  svg += `</svg>`
  return svg
}

/**
 * 生成线段图SVG
 * @param {Object} options - 配置选项
 * @param {Array} options.points - 点数组 [{name, position, color}] position: 0-100
 * @param {number} options.width - SVG宽度
 * @param {number} options.height - SVG高度
 */
function generateSegment(options = {}) {
  const {
    points = [
      { name: 'A', position: 0 },
      { name: 'B', position: 100 }
    ],
    width = 400,
    height = 80,
    showLength = false,
    lengthLabels = []
  } = options

  const margin = 40
  const lineY = height / 2
  const lineLength = width - 2 * margin

  const posToX = (pos) => margin + (pos / 100) * lineLength

  let svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}">\n`

  // 主线段
  const startX = posToX(Math.min(...points.map(p => p.position)))
  const endX = posToX(Math.max(...points.map(p => p.position)))
  svg += `  <line x1="${startX}" y1="${lineY}" x2="${endX}" y2="${lineY}" stroke="#333" stroke-width="2"/>\n`

  // 点和标签
  points.forEach((point, index) => {
    const x = posToX(point.position)
    const color = point.color || (index === 0 || index === points.length - 1 ? '#333' : '#2196F3')
    const isEndpoint = point.position === 0 || point.position === 100
    
    svg += `  <circle cx="${x}" cy="${lineY}" r="${isEndpoint ? 4 : 3}" fill="${color}"/>\n`
    svg += `  <text x="${x}" y="${lineY + 22}" font-family="Arial" font-size="14" text-anchor="middle" fill="${color}">${point.name}</text>\n`
  })

  // 长度标签
  lengthLabels.forEach(label => {
    const x1 = posToX(label.from)
    const x2 = posToX(label.to)
    const midX = (x1 + x2) / 2
    const y = lineY - 15
    
    svg += `  <line x1="${x1}" y1="${y}" x2="${x2}" y2="${y}" stroke="#666" stroke-width="1" marker-start="url(#arrowLeft)" marker-end="url(#arrowRight)"/>\n`
    svg += `  <text x="${midX}" y="${y - 5}" font-family="Arial" font-size="11" text-anchor="middle" fill="#666">${label.text}</text>\n`
  })

  svg += `</svg>`
  return svg
}

/**
 * 生成角度图SVG
 * @param {Object} options - 配置选项
 */
function generateAngle(options = {}) {
  const {
    rays = [],  // [{angle, label, color}] 角度为从正x轴逆时针计算
    vertex = { x: 150, y: 150, label: 'O' },
    width = 300,
    height = 200,
    showArc = true,
    arcRadius = 30
  } = options

  const rayLength = 100

  // 计算射线端点
  const getRayEnd = (angleDeg) => {
    const angleRad = (angleDeg * Math.PI) / 180
    return {
      x: vertex.x + rayLength * Math.cos(angleRad),
      y: vertex.y - rayLength * Math.sin(angleRad)  // SVG y轴向下
    }
  }

  let svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}">\n`

  // 顶点
  svg += `  <circle cx="${vertex.x}" cy="${vertex.y}" r="4" fill="#333"/>\n`
  svg += `  <text x="${vertex.x}" y="${vertex.y + 20}" font-family="Arial" font-size="14" text-anchor="middle">${vertex.label}</text>\n`

  // 射线
  rays.forEach((ray, index) => {
    const end = getRayEnd(ray.angle)
    const color = ray.color || '#333'
    
    svg += `  <line x1="${vertex.x}" y1="${vertex.y}" x2="${end.x}" y2="${end.y}" stroke="${color}" stroke-width="2"/>\n`
    
    // 射线标签
    const labelDist = rayLength + 15
    const labelAngleRad = (ray.angle * Math.PI) / 180
    const labelX = vertex.x + labelDist * Math.cos(labelAngleRad)
    const labelY = vertex.y - labelDist * Math.sin(labelAngleRad)
    svg += `  <text x="${labelX}" y="${labelY}" font-family="Arial" font-size="14" text-anchor="middle" fill="${color}">${ray.label}</text>\n`
  })

  // 角度弧线
  if (showArc && rays.length >= 2) {
    const angle1 = Math.min(rays[0].angle, rays[1].angle)
    const angle2 = Math.max(rays[0].angle, rays[1].angle)
    const startAngle = -angle2 * Math.PI / 180  // SVG arc 从正x轴顺时针
    const endAngle = -angle1 * Math.PI / 180
    
    const startX = vertex.x + arcRadius * Math.cos(startAngle)
    const startY = vertex.y + arcRadius * Math.sin(startAngle)
    const endX = vertex.x + arcRadius * Math.cos(endAngle)
    const endY = vertex.y + arcRadius * Math.sin(endAngle)
    
    const largeArc = (angle2 - angle1) > 180 ? 1 : 0
    
    svg += `  <path d="M ${startX} ${startY} A ${arcRadius} ${arcRadius} 0 ${largeArc} 1 ${endX} ${endY}" fill="none" stroke="#2196F3" stroke-width="1.5"/>\n`
  }

  svg += `</svg>`
  return svg
}

/**
 * 生成角平分线图SVG
 */
function generateAngleBisector(options = {}) {
  const {
    mainAngle = 120,  // 主角度大小
    numBisectors = 1, // 平分线数量
    labels = { vertex: 'O', rays: ['A', 'B'], bisectors: ['C'] },
    width = 300,
    height = 200
  } = options

  const vertex = { x: 150, y: 150 }
  const rayLength = 100

  const getRayEnd = (angleDeg) => {
    const angleRad = (angleDeg * Math.PI) / 180
    return {
      x: vertex.x + rayLength * Math.cos(angleRad),
      y: vertex.y - rayLength * Math.sin(angleRad)
    }
  }

  let svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}">\n`

  // 顶点
  svg += `  <circle cx="${vertex.x}" cy="${vertex.y}" r="4" fill="#333"/>\n`
  svg += `  <text x="${vertex.x}" y="${vertex.y + 20}" font-family="Arial" font-size="14" text-anchor="middle">${labels.vertex}</text>\n`

  // 主射线1 (0度)
  const end1 = getRayEnd(0)
  svg += `  <line x1="${vertex.x}" y1="${vertex.y}" x2="${end1.x}" y2="${end1.y}" stroke="#333" stroke-width="2"/>\n`
  svg += `  <text x="${end1.x + 10}" y="${end1.y}" font-family="Arial" font-size="14">${labels.rays[0]}</text>\n`

  // 主射线2 (mainAngle度)
  const end2 = getRayEnd(mainAngle)
  svg += `  <line x1="${vertex.x}" y1="${vertex.y}" x2="${end2.x}" y2="${end2.y}" stroke="#333" stroke-width="2"/>\n`
  svg += `  <text x="${end2.x - 5}" y="${end2.y - 10}" font-family="Arial" font-size="14">${labels.rays[1]}</text>\n`

  // 平分线
  const bisectorAngle = mainAngle / 2
  const endB = getRayEnd(bisectorAngle)
  svg += `  <line x1="${vertex.x}" y1="${vertex.y}" x2="${endB.x}" y2="${endB.y}" stroke="#2196F3" stroke-width="2" stroke-dasharray="5,3"/>\n`
  svg += `  <text x="${endB.x + 5}" y="${endB.y - 5}" font-family="Arial" font-size="14" fill="#2196F3">${labels.bisectors[0]}</text>\n`

  // 角度弧
  svg += `  <path d="M ${vertex.x + 30} ${vertex.y} A 30 30 0 0 0 ${vertex.x + 30 * Math.cos(mainAngle * Math.PI / 180)} ${vertex.y - 30 * Math.sin(mainAngle * Math.PI / 180)}" fill="none" stroke="#666" stroke-width="1"/>\n`

  svg += `</svg>`
  return svg
}

/**
 * 生成圆和数轴组合图（圆滚动）
 */
function generateCircleOnNumberLine(options = {}) {
  const {
    circleCenter = 0,
    radius = 1,
    min = -5,
    max = 5,
    markedPoint = { angle: 180, label: 'A' },
    width = 400,
    height = 120
  } = options

  const margin = 40
  const lineY = height - 30
  const range = max - min
  const scale = (width - 2 * margin) / range
  const scaledRadius = radius * scale

  const valueToX = (val) => margin + (val - min) * scale
  const centerX = valueToX(circleCenter)
  const circleY = lineY - scaledRadius

  let svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}">\n`

  // 数轴
  svg += `  <line x1="${margin - 10}" y1="${lineY}" x2="${width - margin + 10}" y2="${lineY}" stroke="#333" stroke-width="2"/>\n`
  svg += `  <polygon points="${width - margin + 10},${lineY} ${width - margin},${lineY - 4} ${width - margin},${lineY + 4}" fill="#333"/>\n`

  // 刻度
  for (let i = min; i <= max; i++) {
    const x = valueToX(i)
    svg += `  <line x1="${x}" y1="${lineY - 4}" x2="${x}" y2="${lineY + 4}" stroke="#333" stroke-width="1.5"/>\n`
    svg += `  <text x="${x}" y="${lineY + 18}" font-family="Arial" font-size="11" text-anchor="middle">${i}</text>\n`
  }

  // 圆
  svg += `  <circle cx="${centerX}" cy="${circleY}" r="${scaledRadius}" fill="none" stroke="#2196F3" stroke-width="2"/>\n`

  // 圆上的标记点
  const markedAngleRad = (markedPoint.angle * Math.PI) / 180
  const markedX = centerX + scaledRadius * Math.cos(markedAngleRad)
  const markedY = circleY - scaledRadius * Math.sin(markedAngleRad)
  svg += `  <circle cx="${markedX}" cy="${markedY}" r="4" fill="#E91E63"/>\n`
  svg += `  <text x="${markedX}" y="${markedY - 8}" font-family="Arial" font-size="12" text-anchor="middle" fill="#E91E63">${markedPoint.label}</text>\n`

  svg += `</svg>`
  return svg
}

/**
 * 生成三角形SVG
 */
function generateTriangle(options = {}) {
  const {
    vertices = [
      { x: 150, y: 30, label: 'A' },
      { x: 50, y: 170, label: 'B' },
      { x: 250, y: 170, label: 'C' }
    ],
    width = 300,
    height = 200,
    showAngles = false,
    showSides = false
  } = options

  let svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}">\n`

  // 三角形边
  const points = vertices.map(v => `${v.x},${v.y}`).join(' ')
  svg += `  <polygon points="${points}" fill="none" stroke="#333" stroke-width="2"/>\n`

  // 顶点标签
  vertices.forEach((v, i) => {
    const offsetY = v.y < height / 2 ? -10 : 20
    const offsetX = v.x < width / 2 ? -10 : (v.x > width / 2 ? 10 : 0)
    svg += `  <circle cx="${v.x}" cy="${v.y}" r="3" fill="#333"/>\n`
    svg += `  <text x="${v.x + offsetX}" y="${v.y + offsetY}" font-family="Arial" font-size="14" text-anchor="middle">${v.label}</text>\n`
  })

  svg += `</svg>`
  return svg
}

/**
 * 根据题型自动生成对应的SVG
 * @param {string} type - 图形类型
 * @param {Object} data - 图形数据
 */
function generateSvgByType(type, data = {}) {
  switch (type) {
    case 'numberline':
    case '数轴':
      return generateNumberLine(data)
    
    case 'segment':
    case '线段':
      return generateSegment(data)
    
    case 'angle':
    case '角':
    case '角度':
      return generateAngle(data)
    
    case 'bisector':
    case '角平分线':
      return generateAngleBisector(data)
    
    case 'circle-numberline':
    case '圆滚动':
      return generateCircleOnNumberLine(data)
    
    case 'triangle':
    case '三角形':
      return generateTriangle(data)
    
    default:
      return null
  }
}

/**
 * 从题目文本中提取图形参数
 * 用于自动生成图形
 */
function extractFigureParams(content) {
  const params = {
    type: null,
    data: {}
  }

  // 检测数轴相关
  if (content.includes('数轴') || content.includes('表示的数')) {
    params.type = 'numberline'
    
    // 提取数值
    const numbers = content.match(/-?\d+/g)
    if (numbers) {
      const numList = numbers.map(n => parseInt(n))
      params.data.min = Math.min(...numList, -5)
      params.data.max = Math.max(...numList, 5)
    }
    
    // 提取点
    const pointPattern = /点\s*([A-Z])\s*(?:表示的数)?(?:为|是)?\s*(-?\d+)/g
    let match
    params.data.points = []
    while ((match = pointPattern.exec(content)) !== null) {
      params.data.points.push({
        label: match[1],
        value: parseInt(match[2])
      })
    }
  }
  
  // 检测线段相关
  else if (content.includes('线段') && (content.includes('中点') || content.includes('CM') || content.includes('AB'))) {
    params.type = 'segment'
    
    // 提取点名
    const pointNames = content.match(/点\s*([A-Z])/g)
    if (pointNames) {
      const names = pointNames.map(p => p.replace('点', '').trim())
      params.data.points = names.map((name, i) => ({
        name: name,
        position: (i / (names.length - 1)) * 100
      }))
    }
  }
  
  // 检测角度相关
  else if (content.includes('∠') || content.includes('角') || content.includes('平分线')) {
    params.type = 'angle'
    
    // 提取角度值
    const angleMatch = content.match(/(\d+)\s*°/)
    if (angleMatch) {
      params.data.mainAngle = parseInt(angleMatch[1])
    }
  }

  return params
}

module.exports = {
  generateNumberLine,
  generateSegment,
  generateAngle,
  generateAngleBisector,
  generateCircleOnNumberLine,
  generateTriangle,
  generateSvgByType,
  extractFigureParams
}

