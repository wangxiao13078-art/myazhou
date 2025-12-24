import { GetServerSideProps } from 'next'
import { ProblemDetailScreen } from 'app/features/problem/detail-screen'
import { getProblemById } from 'app/features/problem/mock-data'
import { Problem } from 'app/features/problem/schema'

interface ProblemPageProps {
  problem: Problem
  id: string
}

export default function ProblemPage({ problem, id }: ProblemPageProps) {
  // 使用 key 属性强制在 id 变化时重新渲染组件
  return <ProblemDetailScreen key={id} problem={problem} />
}

export const getServerSideProps: GetServerSideProps<ProblemPageProps> = async (context) => {
  const { id } = context.params as { id: string }
  const problem = getProblemById(id || 't1')
  
  return {
    props: {
      problem,
      id,
    },
  }
}
