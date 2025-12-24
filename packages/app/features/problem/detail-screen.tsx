import React, { useState, useMemo } from 'react'
import { YStack, XStack, Text, Button, Card, ScrollView, H2, H3, Theme, Separator, Image } from 'tamagui'
import { ChevronRight, ChevronDown, BookOpen, Star, ListOrdered } from '@tamagui/lucide-icons'
import { Problem, MathStep } from './schema'
import { MathText } from '../../ui/math-text'
import { Header } from '../../ui/header'
import { useRouter } from 'solito/router'
import { getProblemsByTechnique } from './mock-data'
import { Link } from 'solito/link'
import { getProblemSvgs } from '../../ui/svg-image'

interface ProblemDetailScreenProps {
  problem: Problem
}

export function ProblemDetailScreen({ problem }: ProblemDetailScreenProps) {
  const [unlockedSteps, setUnlockedSteps] = useState<number[]>([])
  const { push } = useRouter()
  
  // 提取考法 ID（例如从 't1-example' 或 't1-train-1' 提取 't1'）
  const techniqueId = useMemo(() => {
    const match = problem.id.match(/^(t\d+)/)
    return match ? match[1] : null
  }, [problem.id])
  
  // 获取该考法的所有题目
  const allProblems = useMemo(() => {
    if (!techniqueId) return []
    return getProblemsByTechnique(techniqueId)
  }, [techniqueId])
  
  // 当前题目的索引和下一题
  const currentIndex = allProblems.findIndex(p => p.id === problem.id)
  const nextProblem = currentIndex >= 0 && currentIndex < allProblems.length - 1 
    ? allProblems[currentIndex + 1] 
    : null
  
  // 针对训练列表（排除例题）
  const trainingProblems = allProblems.filter(p => p.id.includes('-train-'))

  const toggleStep = (index: number) => {
    if (unlockedSteps.includes(index)) {
      setUnlockedSteps(unlockedSteps.filter(i => i !== index))
    } else {
      setUnlockedSteps([...unlockedSteps, index])
    }
  }

  return (
    <YStack f={1} backgroundColor="$background">
      <Header title="题目详情" showBack />
      <ScrollView>
        <YStack p="$4" space="$4" maxWidth={800} alignSelf="center" width="100%">
          {/* 标题与考点 */}
          <YStack space="$3">
            <XStack space="$2" flexWrap="wrap">
              {problem.tags.map(tag => (
                <Theme name="blue" key={tag}>
                  <Button size="$1" chromeless backgroundColor="$blue3" color="$blue11" br="$4" px="$2">
                    #{tag}
                  </Button>
                </Theme>
              ))}
              <XStack ml="auto" space="$1" alignItems="center">
                <Text fontSize="$2" color="$orange10">难度</Text>
                {[...Array(5)].map((_, i) => (
                  <Star key={i} size={10} fill={i < problem.difficulty ? "orange" : "none"} color="orange" />
                ))}
              </XStack>
            </XStack>
            <H2 color="$color" fontSize="$6" lineHeight={32}>{problem.title}</H2>
          </YStack>

          <Separator />

          {/* 题目内容 */}
          <Card p="$4" borderWidth={1} borderColor="$borderColor" backgroundColor="$backgroundHover" br="$4">
            <MathText content={problem.content} fontSize="$5" lineHeight={30} color="$gray12" />
          </Card>

          {/* SVG图形展示 */}
          {getProblemSvgs(problem.id).length > 0 && (
            <Card p="$4" borderWidth={1} borderColor="$blue5" backgroundColor="$blue1" br="$4">
              <YStack space="$3">
                <Text fontWeight="bold" color="$blue10" fontSize="$3">📐 题目图形</Text>
                <XStack flexWrap="wrap" jc="center" gap="$3">
                  {getProblemSvgs(problem.id).map((svgName, idx) => (
                    <Image
                      key={idx}
                      source={{ uri: `/svg/${svgName}.svg`, width: 350, height: 180 }}
                      width={350}
                      height={180}
                      resizeMode="contain"
                    />
                  ))}
                </XStack>
              </YStack>
            </Card>
          )}

          {/* 方法总结 - 对应《一本》的方法点拨 */}
          {problem.methodName && (
            <Theme name="orange">
              <YStack p="$4" br="$4" backgroundColor="$orange2" borderLeftWidth={4} borderLeftColor="$orange8" space="$2">
                <XStack alignItems="center" space="$2">
                  <BookOpen size={18} color="$orange10" />
                  <Text fontWeight="bold" color="$orange10" fontSize="$3">一本方法点拨</Text>
                </XStack>
                <Text color="$orange11" fontSize="$3">{problem.methodName}</Text>
              </YStack>
            </Theme>
          )}

          {/* 分步解析 */}
          <YStack space="$3" mt="$2">
            <XStack ai="center" space="$2">
              <Separator f={1} />
              <Text fontSize="$2" color="$gray9" fontWeight="bold">分步解析引导</Text>
              <Separator f={1} />
            </XStack>
            
            {problem.steps.map((step, index) => {
              const isUnlocked = unlockedSteps.includes(index)
              return (
                <YStack key={index} borderWidth={1} borderColor="$borderColor" br="$4" overflow="hidden" backgroundColor={isUnlocked ? "$background" : "$gray1"}>
                  <Button 
                    onPress={() => toggleStep(index)}
                    justifyContent="space-between"
                    backgroundColor="transparent"
                    p="$4"
                    br={0}
                    height="auto"
                    pressStyle={{ opacity: 0.8 }}
                  >
                    <Text fontWeight="bold" color={isUnlocked ? "$blue10" : "$gray11"} f={1} pr="$2">
                      {step.title}
                    </Text>
                    {isUnlocked ? <ChevronDown size={20} color="$blue10" /> : <ChevronRight size={20} color="$gray8" />}
                  </Button>
                  
                  {isUnlocked && (
                    <YStack p="$4" backgroundColor="$background" space="$3" borderTopWidth={1} borderTopColor="$borderColor">
                      <MathText content={step.content} color="$gray11" fontSize="$4" lineHeight={24} />
                      {step.formula && (
                        <YStack p="$3" backgroundColor="$gray2" br="$2">
                          <MathText content={step.formula} block />
                        </YStack>
                      )}
                    </YStack>
                  )}
                </YStack>
              )
            })}
          </YStack>

          {/* 针对训练列表（仅在例题页面显示） */}
          {problem.id.includes('-example') && trainingProblems.length > 0 && (
            <YStack space="$3" mt="$4">
              <XStack ai="center" space="$2">
                <ListOrdered size={18} color="$green10" />
                <Text fontWeight="bold" color="$green10" fontSize="$4">针对训练 ({trainingProblems.length}题)</Text>
              </XStack>
              
              <YStack space="$2">
                {trainingProblems.map((tp, index) => (
                  <Link key={tp.id} href={`/problem/${tp.id}`}>
                    <Card 
                      p="$3" 
                      borderWidth={1} 
                      borderColor="$borderColor" 
                      br="$3"
                      backgroundColor="$background"
                      hoverStyle={{ backgroundColor: '$backgroundHover' }}
                      pressStyle={{ opacity: 0.8 }}
                    >
                      <XStack ai="center" jc="space-between">
                        <XStack ai="center" space="$2" f={1}>
                          <Text color="$green10" fontWeight="bold" fontSize="$3">
                            训练{index + 1}
                          </Text>
                          <Text color="$gray11" fontSize="$3" numberOfLines={1} f={1}>
                            {tp.title.replace(/^针对训练\d+：/, '')}
                          </Text>
                        </XStack>
                        <ChevronRight size={16} color="$gray8" />
                      </XStack>
                    </Card>
                  </Link>
                ))}
              </YStack>
            </YStack>
          )}

          {/* 底部操作 */}
          <XStack space="$4" mt="$6" pb="$10">
            <Button f={1} theme="blue_alt1" size="$5" br="$10" borderWidth={1} borderColor="$borderColor">加入错题本</Button>
            <Button 
              f={1} 
              theme="blue" 
              size="$5" 
              br="$10"
              onPress={() => nextProblem && push(`/problem/${nextProblem.id}`)}
              opacity={nextProblem ? 1 : 0.5}
              disabled={!nextProblem}
            >
              {nextProblem ? '下一题' : '已完成'}
            </Button>
          </XStack>
        </YStack>
      </ScrollView>
    </YStack>
  )
}
