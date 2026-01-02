import { z } from 'zod'

export const WhiteboardStepSchema = z.object({
  id: z.string(),
  type: z.enum([
    'text',      // 普通文字
    'math',      // 数学公式 (LaTeX)
    'line',      // 直线
    'arrow',     // 箭头
    'rect',      // 矩形
    'circle',    // 圆形
    'arc',       // 弧线
    'highlight', // 高亮框
  ]),
  x: z.number(),
  y: z.number(),
  // 终点坐标 (用于线条、箭头)
  x2: z.number().optional(),
  y2: z.number().optional(),
  // 尺寸 (用于矩形、圆形)
  width: z.number().optional(),
  height: z.number().optional(),
  radius: z.number().optional(),
  // 内容 (用于文字、公式)
  content: z.string().optional(),
  // 样式
  color: z.string().optional(),
  strokeWidth: z.number().optional(),
  fill: z.string().optional(),
  // 动画
  duration: z.number().optional(),
})

export const SolutionSchema = z.object({
  title: z.string(),
  steps: z.array(z.object({
    explanation: z.string(),
    drawings: z.array(WhiteboardStepSchema)
  })),
  finalAnswer: z.string()
})

export type WhiteboardStep = z.infer<typeof WhiteboardStepSchema>
export type Solution = z.infer<typeof SolutionSchema>
