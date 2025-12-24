import React from 'react'
import { YStack, XStack, Text, Card, ScrollView, H2, Theme } from 'tamagui'
import { ChevronRight, ClipboardList, Star } from '@tamagui/lucide-icons'
import { Header } from 'app/ui/header'
import { Link } from 'solito/link'
import { GetStaticProps, GetStaticPaths } from 'next'
import { problemData } from 'app/features/problem/mock-data'

interface QuizPageProps {
  quizId: string
  quizName: string
  problems: Array<{
    id: string
    title: string
    difficulty: number
  }>
}

export default function QuizPage({ quizId, quizName, problems }: QuizPageProps) {
  return (
    <YStack f={1} backgroundColor="$background">
      <Header title={quizName} showBack />
      <ScrollView>
        <YStack p="$4" space="$4" maxWidth={800} alignSelf="center" width="100%">
          {/* 标题 */}
          <YStack space="$2" ai="center" py="$4">
            <XStack ai="center" space="$2">
              <ClipboardList size={28} color="$blue10" />
              <H2 color="$color">{quizName}</H2>
            </XStack>
            <Text color="$gray10" fontSize="$3">共 {problems.length} 道综合练习题</Text>
          </YStack>

          {/* 题目列表 */}
          <YStack space="$3">
            {problems.map((problem, index) => (
              <Link key={problem.id} href={`/problem/${problem.id}`}>
                <Card 
                  p="$4" 
                  borderWidth={1}
                  borderColor="$borderColor"
                  backgroundColor="$background"
                  pressStyle={{ opacity: 0.8, backgroundColor: '$backgroundHover' }}
                  hoverStyle={{ backgroundColor: '$backgroundHover' }}
                  br="$4"
                >
                  <XStack jc="space-between" ai="center">
                    <XStack ai="center" space="$3" f={1}>
                      <XStack 
                        width={32} 
                        height={32} 
                        br={16} 
                        backgroundColor="$blue3" 
                        ai="center" 
                        jc="center"
                      >
                        <Text fontWeight="bold" color="$blue10">{index + 1}</Text>
                      </XStack>
                      <YStack f={1}>
                        <Text fontWeight="bold" fontSize="$4" color="$color" numberOfLines={1}>
                          第{index + 1}题
                        </Text>
                        <XStack ai="center" space="$1" mt="$1">
                          {[...Array(5)].map((_, i) => (
                            <Star 
                              key={i} 
                              size={12} 
                              fill={i < problem.difficulty ? "orange" : "none"} 
                              color="orange" 
                            />
                          ))}
                        </XStack>
                      </YStack>
                    </XStack>
                    <ChevronRight size={20} color="$gray8" />
                  </XStack>
                </Card>
              </Link>
            ))}
          </YStack>
        </YStack>
      </ScrollView>
    </YStack>
  )
}

export const getStaticPaths: GetStaticPaths = async () => {
  const quizIds = ['z1', 'z2', 'z3', 'z4', 'z5', 'z6', 'final']
  
  return {
    paths: quizIds.map(id => ({ params: { id } })),
    fallback: false,
  }
}

export const getStaticProps: GetStaticProps<QuizPageProps> = async (context) => {
  const { id } = context.params as { id: string }
  
  // 专题集训名称映射
  const quizNames: Record<string, string> = {
    'z1': '专题集训一：有理数',
    'z2': '专题集训二：有理数的运算',
    'z3': '专题集训三：代数式',
    'z4': '专题集训四：整式的加减',
    'z5': '专题集训五：一元一次方程',
    'z6': '专题集训六：几何图形初步',
    'final': '七上期末冲刺练',
  }
  
  // 获取该专题集训的所有题目
  const problems: Array<{ id: string; title: string; difficulty: number }> = []
  let quizIndex = 1
  while (problemData[`${id}-quiz-${quizIndex}`]) {
    const problem = problemData[`${id}-quiz-${quizIndex}`]
    problems.push({
      id: problem.id,
      title: problem.title,
      difficulty: problem.difficulty,
    })
    quizIndex++
  }

  return {
    props: {
      quizId: id,
      quizName: quizNames[id] || `专题集训`,
      problems,
    },
  }
}
