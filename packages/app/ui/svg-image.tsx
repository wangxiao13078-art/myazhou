import React, { useState, useEffect } from 'react'
import { YStack, Image } from 'tamagui'

interface SvgImageProps {
  name: string
  width?: number
  height?: number
}

// 检测是否在 GitHub Pages 上运行
function getBasePath(): string {
  if (typeof window === 'undefined') return ''
  // 检查 URL 路径是否包含 /myazhou
  const path = window.location.pathname
  if (path.startsWith('/myazhou')) {
    return '/myazhou'
  }
  return ''
}

// SVG文件名映射（不包含路径前缀）
const svgFileNames: Record<string, string> = {
  // 数轴类型
  'number-line-basic': 'number-line-basic.svg',
  'number-line-circle': 'number-line-circle.svg',
  'number-line-ab': 'number-line-ab.svg',
  'number-line-ab-2': 'number-line-ab-2.svg',
  'number-line-ab-3': 'number-line-ab-3.svg',
  'number-line-abcd': 'number-line-abcd.svg',
  'triangle-flip': 'triangle-flip.svg',
  'moving-points': 'moving-points.svg',
  'circle-numbers': 'circle-numbers.svg',
  'folding-line': 'folding-line.svg',
  'jumping-point': 'jumping-point.svg',
  'two-circles': 'two-circles.svg',
  
  // 几何图形
  'area-square': 'area-square.svg',
  'chess-pattern': 'chess-pattern.svg',
  'house-plan': 'house-plan.svg',
  'cube': 'cube.svg',
  
  // 火柴棒
  'matchstick-1': 'matchstick-1.svg',
  'matchstick-2': 'matchstick-2.svg',
  'matchstick-3': 'matchstick-3.svg',
  'matchstick-4': 'matchstick-4.svg',
  
  // 正多边形
  'polygon-3': 'polygon-3.svg',
  'polygon-4': 'polygon-4.svg',
  'polygon-5': 'polygon-5.svg',
  'polygon-6': 'polygon-6.svg',
  
  // 角度和几何图形
  'angle-rays-5': 'angle-rays-5.svg',
  'angle-rays-4': 'angle-rays-4.svg',
  'angle-rays-3': 'angle-rays-3.svg',
  'angle-bisector': 'angle-bisector.svg',
  'rotating-angle': 'rotating-angle.svg',
  'segment-abc': 'segment-abc.svg',
  'segment-midpoints': 'segment-midpoints.svg',
  'triangle-lines': 'triangle-lines.svg',
  'angle-aob-150': 'angle-aob-150.svg',
  'angle-aob-120': 'angle-aob-120.svg',
  'rays-abcde': 'rays-abcde.svg',
  
  // 期末冲刺练图形
  'final-number-line-1': 'final-number-line-1.svg',
  'final-cube': 'final-cube.svg',
  'final-triangles': 'final-triangles.svg',
  'final-angle-12': 'final-angle-12.svg',
  'final-number-line-15': 'final-number-line-15.svg',
  'final-segment-16': 'final-segment-16.svg',
  'final-angle-16-2': 'final-angle-16-2.svg',
  'final-angle-16-3': 'final-angle-16-3.svg',
}

// 题目ID到SVG的映射
export const problemSvgMap: Record<string, string[]> = {
  // ========== 专题一 ==========
  // t1 数轴动点问题
  't1-example': ['number-line-circle'],
  't1-train-1': ['number-line-circle'],
  't1-train-2': ['number-line-ab'],
  't1-train-3': ['number-line-basic'],
  't1-train-4': ['number-line-basic'],
  't1-train-5': ['moving-points'],
  't1-train-6': ['number-line-basic'],
  't1-train-7': ['number-line-ab'],
  
  // t2 规律探究
  't2-example': ['triangle-flip'],
  't2-train-1': ['circle-numbers'],
  't2-train-2': ['number-line-ab'],
  't2-train-3': ['circle-numbers'],
  
  // t3 比较大小
  't3-example': ['number-line-ab'],
  't3-train-1': ['number-line-ab'],
  
  // t4 绝对值
  't4-example': ['number-line-ab'],
  't4-train-1': ['number-line-ab'],
  
  // t5 几何意义
  't5-example': ['number-line-ab'],
  't5-train-1': ['number-line-ab'],
  't5-train-2': ['number-line-ab'],
  
  // t7 实际应用
  't7-train-1': ['area-square'],
  
  // ========== 专题二 ==========
  // t12 折叠问题
  't12-example': ['folding-line'],
  't12-train-1': ['folding-line'],
  't12-train-2': ['folding-line'],
  
  // t13 动点问题
  't13-example': ['moving-points'],
  't13-train-1': ['number-line-ab'],
  't13-train-2': ['number-line-ab-2'],
  
  // t14 运算与绝对值
  't14-example': ['number-line-ab'],
  't14-train-1': ['number-line-ab'],
  
  // t15 新定义
  't15-example': ['number-line-ab'],
  
  // ========== 专题三 ==========
  // t16 面积问题
  't16-example': ['house-plan'],
  't16-train-1': ['area-square'],
  't16-train-2': ['area-square'],
  
  // t18 整体思想
  't18-example': ['area-square'],
  
  // t19 规律探究
  't19-example': ['area-square', 'cube'],
  't19-train-1': ['polygon-3'],
  't19-train-2': ['matchstick-2'],
  't19-train-3': ['polygon-5'],
  
  // t20 新定义
  't20-example': ['matchstick-1'],
  
  // ========== 专题四 ==========
  // t21 整体思想
  't21-example': ['number-line-ab'],
  't21-train-1': ['number-line-ab'],
  
  // t22 数轴化简
  't22-example': ['number-line-ab'],
  't22-train-1': ['number-line-ab'],
  
  // t23 分类讨论
  't23-example': ['number-line-abcd'],
  
  // t24 围棋规律
  't24-example': ['chess-pattern'],
  't24-train-1': ['chess-pattern'],
  't24-train-2': ['chess-pattern'],
  
  // ========== 专题五 ==========
  // t35 数形结合
  't35-train-1': ['number-line-ab'],
  't35-train-2': ['number-line-ab'],
  't35-train-3': ['number-line-ab'],
  't35-train-4': ['segment-abc'],
  
  // t36 角度整体
  't36-train-1': ['angle-bisector'],
  't36-train-2': ['rays-abcde'],
  
  // t37 方程思想
  't37-train-1': ['angle-bisector'],
  't37-train-2': ['rotating-angle'],
  't37-train-3': ['rotating-angle'],
  
  // ========== 专题六：几何 ==========
  't32-example': ['segment-midpoints'],
  't32-train-1': ['segment-abc'],
  't32-train-2': ['segment-abc'],
  't33-example': ['segment-abc'],
  't33-train-1': ['segment-abc'],
  't33-train-2': ['segment-abc'],
  't34-example': ['segment-abc'],
  't34-train-1': ['segment-abc'],
  't34-train-2': ['number-line-ab'],
  't35-example': ['segment-abc'],
  't36-example': ['rays-abcde'],
  't37-example': ['rotating-angle'],
  
  // ========== 专题集训一 ==========
  'z1-quiz-1': ['number-line-basic'],
  'z1-quiz-2': ['number-line-ab'],
  'z1-quiz-3': ['number-line-ab'],
  'z1-quiz-4': ['number-line-ab'],
  'z1-quiz-5': ['number-line-ab'],
  'z1-quiz-6': ['number-line-ab'],
  'z1-quiz-7': ['two-circles'],
  'z1-quiz-8': ['number-line-ab'],
  'z1-quiz-9': ['number-line-ab'],
  'z1-quiz-10': ['number-line-ab'],
  'z1-quiz-12': ['matchstick-2'],
  'z1-quiz-14': ['number-line-ab'],
  
  // ========== 专题集训二 ==========
  'z2-quiz-1': ['number-line-ab'],
  'z2-quiz-4': ['number-line-ab'],
  
  // ========== 专题集训三 ==========
  'z3-quiz-3': ['jumping-point'],
  'z3-quiz-5': ['area-square'],
  'z3-quiz-6': ['matchstick-1'],
  'z3-quiz-7': ['matchstick-2'],
  'z3-quiz-8': ['polygon-3'],
  'z3-quiz-9': ['chess-pattern'],
  
  // ========== 专题集训四 ==========
  'z4-quiz-3': ['number-line-ab'],
  'z4-quiz-5': ['number-line-abcd'],
  'z4-quiz-8': ['area-square'],
  'z4-quiz-9': ['polygon-4'],
  
  // ========== 专题集训五 ==========
  'z5-quiz-3': ['number-line-abcd'],
  'z5-quiz-7': ['area-square'],
  'z5-quiz-10': ['segment-abc'],
  'z5-quiz-13': ['rotating-angle'],
  
  // ========== 专题集训六 ==========
  'z6-quiz-4': ['segment-abc'],
  'z6-quiz-6': ['angle-aob-150'],
  'z6-quiz-8': ['triangle-lines'],
  'z6-quiz-9': ['angle-bisector'],
  'z6-quiz-10': ['segment-abc'],
  'z6-quiz-11': ['rotating-angle'],
  'z6-quiz-12': ['house-plan'],
  'z6-quiz-13': ['rotating-angle'],
  'z6-quiz-14': ['area-square'],
  
  // ========== 期末冲刺练 ==========
  'final-quiz-1': ['final-number-line-1'],
  'final-quiz-2': ['final-cube'],
  'final-quiz-4': ['final-triangles'],
  'final-quiz-12': ['final-angle-12'],
  'final-quiz-15': ['final-number-line-15'],
  'final-quiz-16': ['final-segment-16', 'final-angle-16-2', 'final-angle-16-3'],
}

export function SvgImage({ name, width = 400, height = 200 }: SvgImageProps) {
  const fileName = svgFileNames[name]
  const [src, setSrc] = useState<string | null>(null)
  
  useEffect(() => {
    if (fileName) {
      // 在客户端动态判断路径前缀
      const basePath = getBasePath()
      setSrc(basePath + '/svg/' + fileName)
    }
  }, [fileName])
  
  if (!fileName) {
    console.warn(`SVG not found: ${name}`)
    return null
  }
  
  // 等待客户端计算正确的 src
  if (!src) {
    return <YStack ai="center" my="$2" height={height} />
  }
  
  return (
    <YStack ai="center" my="$2">
      <Image
        source={{ uri: src, width, height }}
        width={width}
        height={height}
        resizeMode="contain"
      />
    </YStack>
  )
}

export function getProblemSvgs(problemId: string): string[] {
  return problemSvgMap[problemId] || []
}
