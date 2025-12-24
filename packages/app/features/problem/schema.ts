import { z } from 'zod'

export const MathStepSchema = z.object({
  title: z.string(),
  content: z.string(),
  formula: z.string().optional(),
})

export const ProblemSchema = z.object({
  id: z.string(),
  grade: z.enum(['7', '8', '9']),
  semester: z.enum(['up', 'down']),
  category: z.string(),
  title: z.string(),
  difficulty: z.number().min(1).max(5),
  tags: z.array(z.string()),
  content: z.string(),
  steps: z.array(MathStepSchema),
  methodName: z.string().optional(), // 对应《一本》里的"方法"
  images: z.array(z.string()).optional(), // 题目配图路径（数轴、几何图形等）
  pageNumber: z.number().optional(), // 原书页码，方便查找
})

export type Problem = z.infer<typeof ProblemSchema>
export type MathStep = z.infer<typeof MathStepSchema>


