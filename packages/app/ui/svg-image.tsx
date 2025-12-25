import React from 'react'
import { YStack, Image } from 'tamagui'

interface SvgImageProps {
  name: string
  width?: number
  height?: number
}

// SVG文件名映射（不包含路径前缀）
// 现在使用每道题专属的 SVG 文件
const svgFileNames: Record<string, string> = {
  // ========== 专题一 ==========
  't1-example': 't1_example.svg',
  't1-train-1': 't1_train_1.svg',
  't1-train-2': 't1_train_2.svg',
  't1-train': 't1_train.svg',
  
  // ========== 专题二 ==========
  't2-example': 't2_example.svg',
  't2-train-1': 't2_train_1.svg',
  't2-train': 't2_train.svg',
  
  // ========== 专题三 ==========
  't3-example': 't3_example.svg',
  't3-train-1': 't3_train_1.svg',
  't3-train': 't3_train.svg',
  
  // ========== 专题四 ==========
  't4-example': 't4_example.svg',
  't4-train-1': 't4_train_1.svg',
  't4-train': 't4_train.svg',
  
  // ========== 专题五 ==========
  't5-example': 't5_example.svg',
  't5-train-1': 't5_train_1.svg',
  't5-train-2': 't5_train_2.svg',
  't5-train': 't5_train.svg',
  
  // ========== 专题六 ==========
  't6-example': 't6_example.svg',
  't6-train-1': 't6_train_1.svg',
  't6-train-2': 't6_train_2.svg',
  
  // ========== 专题七 ==========
  't7-example': 't7_example.svg',
  't7-train-1': 't7_train_1.svg',
  't7-train-2': 't7_train_2.svg',
  
  // ========== 专题八 ==========
  't8-example': 't8_example.svg',
  't8-train-1': 't8_train_1.svg',
  
  // ========== 专题九 ==========
  't9-example': 't9_example.svg',
  't9-train-1': 't9_train_1.svg',
  't9-train-2': 't9_train_2.svg',
  
  // ========== 专题十 ==========
  't10-example': 't10_example.svg',
  't10-train-1': 't10_train_1.svg',
  
  // ========== 专题十一 ==========
  't11-example': 't11_example.svg',
  't11-train-1': 't11_train_1.svg',
  
  // ========== 专题十二 ==========
  't12-example': 't12_example.svg',
  't12-train-1': 't12_train_1.svg',
  't12-train-2': 't12_train_2.svg',
  't12-train': 't12_train.svg',
  
  // ========== 专题十三 ==========
  't13-example': 't13_example.svg',
  't13-train-1': 't13_train_1.svg',
  't13-train-2': 't13_train_2.svg',
  't13-train': 't13_train.svg',
  
  // ========== 专题十六 ==========
  't16-example': 't16_example.svg',
  't16-train-1': 't16_train_1.svg',
  
  // ========== 专题十七 ==========
  't17-example': 't17_example.svg',
  't17-train-1': 't17_train_1.svg',
  
  // ========== 专题十八 ==========
  't18-example': 't18_example.svg',
  't18-train-1': 't18_train_1.svg',
  
  // ========== 专题十九 ==========
  't19-example': 't19_example.svg',
  't19-train-1': 't19_train_1.svg',
  't19-train': 't19_train.svg',
  
  // ========== 专题二十 ==========
  't20-example': 't20_example.svg',
  't20-train-1': 't20_train_1.svg',
  
  // ========== 专题二十一 ==========
  't21-example': 't21_example.svg',
  't21-train-1': 't21_train_1.svg',
  
  // ========== 专题二十二 ==========
  't22-example': 't22_example.svg',
  't22-train-1': 't22_train_1.svg',
  't22-train': 't22_train.svg',
  
  // ========== 专题二十三 ==========
  't23-example': 't23_example.svg',
  't23-train-1': 't23_train_1.svg',
  't23-train': 't23_train.svg',
  
  // ========== 专题二十四 ==========
  't24-example': 't24_example.svg',
  't24-train-1': 't24_train_1.svg',
  
  // ========== 专题二十五 ==========
  't25-example': 't25_example.svg',
  't25-train-1': 't25_train_1.svg',
  
  // ========== 专题二十六 ==========
  't26-example': 't26_example.svg',
  't26-train-1': 't26_train_1.svg',
  
  // ========== 专题二十七 ==========
  't27-example': 't27_example.svg',
  't27-train-1': 't27_train_1.svg',
  't27-train': 't27_train.svg',
  
  // ========== 辅助数轴图形 ==========
  'numberline-t1-1': 'numberline_t1_1.svg',
  'numberline-t1-2': 'numberline_t1_2.svg',
  'numberline-t2': 'numberline_t2.svg',
  'numberline-t3': 'numberline_t3.svg',
  'numberline-t4': 'numberline_t4.svg',
  'numberline-t5': 'numberline_t5.svg',
  'triangle-t2': 'triangle_t2.svg',
  
  // ========== 通用图形（保留） ==========
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
  'area-square': 'area-square.svg',
  'chess-pattern': 'chess-pattern.svg',
  'house-plan': 'house-plan.svg',
  'cube': 'cube.svg',
  'matchstick-1': 'matchstick-1.svg',
  'matchstick-2': 'matchstick-2.svg',
  'matchstick-3': 'matchstick-3.svg',
  'matchstick-4': 'matchstick-4.svg',
  'polygon-3': 'polygon-3.svg',
  'polygon-4': 'polygon-4.svg',
  'polygon-5': 'polygon-5.svg',
  'polygon-6': 'polygon-6.svg',
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
  
  // ========== 期末冲刺练图形 ==========
  'final-number-line-1': 'final-number-line-1.svg',
  'final-cube': 'final-cube.svg',
  'final-triangles': 'final-triangles.svg',
  'final-angle-12': 'final-angle-12.svg',
  'final-number-line-15': 'final-number-line-15.svg',
  'final-segment-16': 'final-segment-16.svg',
  'final-angle-16-2': 'final-angle-16-2.svg',
  'final-angle-16-3': 'final-angle-16-3.svg',
}

// 题目ID到SVG的映射 - 现在使用每道题专属的图形
export const problemSvgMap: Record<string, string[]> = {
  // ========== 专题一：有理数 ==========
  't1-example': ['t1-example'],
  't1-train-1': ['t1-train-1'],
  't1-train-2': ['t1-train-2'],
  't1-train-3': ['numberline-t1-1'],
  't1-train-4': ['numberline-t1-2'],
  't1-train-5': ['moving-points'],
  't1-train-6': ['number-line-basic'],
  't1-train-7': ['number-line-ab'],
  
  // t2 规律探究
  't2-example': ['t2-example'],
  't2-train-1': ['t2-train-1'],
  't2-train-2': ['number-line-ab'],
  't2-train-3': ['circle-numbers'],
  
  // t3 比较大小
  't3-example': ['t3-example'],
  't3-train-1': ['t3-train-1'],
  't3-train-2': ['number-line-ab'],
  't3-train-3': ['number-line-ab'],
  
  // t4 绝对值
  't4-example': ['t4-example'],
  't4-train-1': ['t4-train-1'],
  
  // t5 几何意义
  't5-example': ['t5-example'],
  't5-train-1': ['t5-train-1'],
  't5-train-2': ['t5-train-2'],
  
  // t6 新定义
  't6-example': ['t6-example'],
  't6-train-1': ['t6-train-1'],
  't6-train-2': ['t6-train-2'],
  
  // t7 实际应用
  't7-example': ['t7-example'],
  't7-train-1': ['t7-train-1'],
  't7-train-2': ['t7-train-2'],
  
  // ========== 专题二：有理数的运算 ==========
  // t8 拼凑法
  't8-example': ['t8-example'],
  't8-train-1': ['t8-train-1'],
  
  // t9 裂项法
  't9-example': ['t9-example'],
  't9-train-1': ['t9-train-1'],
  't9-train-2': ['t9-train-2'],
  
  // t10 倒数法
  't10-example': ['t10-example'],
  't10-train-1': ['t10-train-1'],
  
  // t11 混合运算
  't11-example': ['t11-example'],
  't11-train-1': ['t11-train-1'],
  
  // t12 折叠问题
  't12-example': ['t12-example'],
  't12-train-1': ['t12-train-1'],
  't12-train-2': ['t12-train-2'],
  
  // t13 动点问题
  't13-example': ['t13-example'],
  't13-train-1': ['t13-train-1'],
  't13-train-2': ['t13-train-2'],
  
  // ========== 专题三：代数式 ==========
  // t16 用字母表示数
  't16-example': ['t16-example'],
  't16-train-1': ['t16-train-1'],
  
  // t17 直接求值
  't17-example': ['t17-example'],
  't17-train-1': ['t17-train-1'],
  
  // t18 整体思想
  't18-example': ['t18-example'],
  't18-train-1': ['t18-train-1'],
  
  // t19 规律探究
  't19-example': ['t19-example'],
  't19-train-1': ['t19-train-1'],
  
  // t20 新定义
  't20-example': ['t20-example'],
  't20-train-1': ['t20-train-1'],
  
  // ========== 专题四：整式的加减 ==========
  // t21 整体思想
  't21-example': ['t21-example'],
  't21-train-1': ['t21-train-1'],
  
  // t22 数轴化简
  't22-example': ['t22-example'],
  't22-train-1': ['t22-train-1'],
  
  // t23 分类讨论
  't23-example': ['t23-example'],
  't23-train-1': ['t23-train-1'],
  
  // t24 围棋规律
  't24-example': ['t24-example'],
  't24-train-1': ['t24-train-1'],
  
  // ========== 专题五：一元一次方程 ==========
  // t25 整体思想
  't25-example': ['t25-example'],
  't25-train-1': ['t25-train-1'],
  
  // t26 裂项相消
  't26-example': ['t26-example'],
  't26-train-1': ['t26-train-1'],
  
  // t27 分类讨论
  't27-example': ['t27-example'],
  't27-train-1': ['t27-train-1'],
  
  // ========== 专题六：几何图形初步 ==========
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
  't35-train-1': ['number-line-ab'],
  't35-train-2': ['number-line-ab'],
  't35-train-3': ['number-line-ab'],
  't35-train-4': ['segment-abc'],
  't36-example': ['rays-abcde'],
  't36-train-1': ['angle-bisector'],
  't36-train-2': ['rays-abcde'],
  't37-example': ['rotating-angle'],
  't37-train-1': ['angle-bisector'],
  't37-train-2': ['rotating-angle'],
  't37-train-3': ['rotating-angle'],
  
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
  'z3-quiz-4': ['circle-numbers'],
  'z3-quiz-5': ['area-square'],
  'z3-quiz-6': ['matchstick-1'],
  'z3-quiz-7': ['matchstick-2'],
  'z3-quiz-8': ['polygon-3'],
  'z3-quiz-9': ['chess-pattern'],
  
  // ========== 专题集训四 ==========
  'z4-quiz-1': ['number-line-ab'],
  'z4-quiz-2': ['number-line-ab'],
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
  'z6-quiz-2': ['segment-abc'],
  'z6-quiz-4': ['segment-abc'],
  'z6-quiz-6': ['angle-aob-150'],
  'z6-quiz-7': ['angle-bisector'],
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
  
  if (!fileName) {
    console.warn(`SVG not found: ${name}`)
    return null
  }
  
  // 直接硬编码 GitHub Pages 路径
  const src = '/myazhou/svg/' + fileName
  
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
