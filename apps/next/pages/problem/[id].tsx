import { GetStaticProps, GetStaticPaths } from 'next'
import { ProblemDetailScreen } from 'app/features/problem/detail-screen'
import { getProblemById, getAllProblemIds } from 'app/features/problem/mock-data'
import { Problem } from 'app/features/problem/schema'

interface ProblemPageProps {
  problem: Problem
  id: string
}

export default function ProblemPage({ problem, id }: ProblemPageProps) {
  // 使用 key 属性强制在 id 变化时重新渲染组件
  return <ProblemDetailScreen key={id} problem={problem} />
}

export const getStaticPaths: GetStaticPaths = async () => {
  const ids = getAllProblemIds()
  
  // 添加技术考法 ID（t1, t2, ...）
  const techniqueIds = []
  for (let i = 1; i <= 27; i++) {
    techniqueIds.push(`t${i}`)
  }
  
  // 添加期末冲刺 ID
  const finalIds = []
  for (let i = 1; i <= 16; i++) {
    finalIds.push(`final-quiz-${i}`)
  }
  
  const allIds = [...ids, ...techniqueIds, ...finalIds]
  
  return {
    paths: allIds.map(id => ({ params: { id } })),
    fallback: false,
  }
}

export const getStaticProps: GetStaticProps<ProblemPageProps> = async (context) => {
  const { id } = context.params as { id: string }
  const problem = getProblemById(id || 't1')
  
  return {
    props: {
      problem,
      id,
    },
  }
}
