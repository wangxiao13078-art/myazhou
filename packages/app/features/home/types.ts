import { z } from 'zod'

export const TechniqueSchema = z.object({
  id: z.string(),
  title: z.string(), // 如：考法1：数轴上两点间的距离
  methodName: z.string(), // 如：数形结合法
})

export const ChapterSchema = z.object({
  id: z.string(),
  title: z.string(), // 如：第一章 有理数
  techniques: z.array(TechniqueSchema),
})

export type Technique = z.infer<typeof TechniqueSchema>
export type Chapter = z.infer<typeof ChapterSchema>



