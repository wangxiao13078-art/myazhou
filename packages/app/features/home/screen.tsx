import { Button, H1, Paragraph, Separator, XStack, YStack, ScrollView, H3, Card, Text } from 'tamagui'
import { ChevronRight, BookOpen, Star, Calculator, Variable, PlusSquare, Equal, ClipboardList } from '@tamagui/lucide-icons'
import React from 'react'
import { Link } from 'solito/link'
import { grade7Chapters } from './mock-chapters'
import { Header } from '../../ui/header'

// 专题集训数据
const quizData = [
  { id: 'z1', name: '专题集训一', count: 14, chapterIndex: 0 },
  { id: 'z2', name: '专题集训二', count: 7, chapterIndex: 1 },
  { id: 'z3', name: '专题集训三', count: 13, chapterIndex: 2 },
  { id: 'z4', name: '专题集训四', count: 13, chapterIndex: 3 },
  { id: 'z5', name: '专题集训五', count: 13, chapterIndex: 4 },
  { id: 'z6', name: '专题集训六', count: 14, chapterIndex: 5 },
  { id: 'final', name: '期末冲刺练', count: 16, chapterIndex: 6 },
]

// 每个专题的配色方案
const chapterThemes = [
  { bg: '$blue2', border: '$blue6', icon: '$blue9', accent: '$blue10' },
  { bg: '$green2', border: '$green6', icon: '$green9', accent: '$green10' },
  { bg: '$purple2', border: '$purple6', icon: '$purple9', accent: '$purple10' },
  { bg: '$orange2', border: '$orange6', icon: '$orange9', accent: '$orange10' },
  { bg: '$pink2', border: '$pink6', icon: '$pink9', accent: '$pink10' },
]

// 专题图标
const chapterIcons = [Calculator, Star, Variable, PlusSquare, Equal]

// 考法卡片组件
function TechniqueCard({ tech, theme }: { 
  tech: { id: string; title: string; methodName: string }
  theme: { bg: string; border: string; icon: string; accent: string }
}) {
  return (
    <Link href={`/problem/${tech.id}`}>
      <Card 
        p="$4" 
        borderWidth={1}
        borderColor="$gray5"
        backgroundColor="$background"
        pressStyle={{ opacity: 0.8, backgroundColor: theme.bg }}
        hoverStyle={{ backgroundColor: theme.bg, borderColor: theme.border }}
        br="$4"
        ml="$2"
      >
        <XStack jc="space-between" ai="center">
          <YStack space="$1" f={1}>
            <Text fontWeight="bold" fontSize="$4" color="$color">{tech.title}</Text>
            <XStack ai="center" space="$1">
              <BookOpen size={14} color={theme.accent} />
              <Text fontSize="$2" color={theme.accent}>方法：{tech.methodName}</Text>
            </XStack>
          </YStack>
          <XStack 
            width={28} 
            height={28} 
            br={14} 
            backgroundColor={theme.bg} 
            ai="center" 
            jc="center"
            borderWidth={1}
            borderColor={theme.border}
          >
            <ChevronRight size={16} color={theme.accent} />
          </XStack>
        </XStack>
      </Card>
    </Link>
  )
}

// 专题集训卡片组件
function QuizCard({ quiz, theme }: { 
  quiz: { id: string; name: string; count: number }
  theme: { bg: string; border: string; icon: string; accent: string }
}) {
  return (
    <Link href={`/quiz/${quiz.id}`}>
      <Card 
        p="$4" 
        borderWidth={2}
        borderColor={theme.border}
        backgroundColor={theme.bg}
        pressStyle={{ opacity: 0.8 }}
        hoverStyle={{ opacity: 0.9 }}
        br="$4"
        ml="$2"
      >
        <XStack jc="space-between" ai="center">
          <XStack ai="center" space="$2" f={1}>
            <ClipboardList size={20} color={theme.accent} />
            <YStack>
              <Text fontWeight="bold" fontSize="$4" color={theme.accent}>
                {quiz.name}
              </Text>
              <Text fontSize="$2" color={theme.icon}>
                共 {quiz.count} 道综合练习
              </Text>
            </YStack>
          </XStack>
          <XStack 
            width={28} 
            height={28} 
            br={14} 
            backgroundColor="$background" 
            ai="center" 
            jc="center"
            borderWidth={1}
            borderColor={theme.border}
          >
            <ChevronRight size={16} color={theme.accent} />
          </XStack>
        </XStack>
      </Card>
    </Link>
  )
}

export function HomeScreen() {
  return (
    <YStack f={1} backgroundColor="$background">
      <Header title="M压轴" />
      <ScrollView>
        <YStack f={1} p="$4" space="$4" maxWidth={600} alignSelf="center" width="100%">
          {/* 顶部标题卡片 */}
          <YStack 
            space="$2" 
            ai="center" 
            py="$6" 
            px="$4"
            br="$6"
            backgroundColor="$blue3"
            borderWidth={2}
            borderColor="$blue6"
          >
            <XStack ai="center" space="$2">
              <BookOpen size={32} color="$blue10" />
              <H1 ta="center" color="$blue10" fontSize="$9" fontWeight="900">压轴数学</H1>
            </XStack>
            <Paragraph ta="center" color="$blue11" fontSize="$4">初一 · 高阶版 · 84个考法</Paragraph>
            <XStack space="$2" mt="$2">
              <YStack ai="center" px="$4" py="$2" br="$4" backgroundColor="$blue4">
                <Text fontSize="$7" fontWeight="bold" color="$blue10">5</Text>
                <Text fontSize="$1" color="$blue11">专题</Text>
              </YStack>
              <YStack ai="center" px="$4" py="$2" br="$4" backgroundColor="$blue4">
                <Text fontSize="$7" fontWeight="bold" color="$blue10">27</Text>
                <Text fontSize="$1" color="$blue11">考法</Text>
              </YStack>
              <YStack ai="center" px="$4" py="$2" br="$4" backgroundColor="$blue4">
                <Text fontSize="$7" fontWeight="bold" color="$blue10">148</Text>
                <Text fontSize="$1" color="$blue11">习题</Text>
              </YStack>
            </XStack>
          </YStack>

          {/* 专题列表 */}
          {grade7Chapters.map((chapter, chapterIndex) => {
            const theme = chapterThemes[chapterIndex % chapterThemes.length]
            const IconComponent = chapterIcons[chapterIndex % chapterIcons.length]
            const quiz = quizData.find(q => q.chapterIndex === chapterIndex)
            
            return (
              <YStack key={chapter.id} space="$3" mt="$3">
                {/* 专题标题 */}
                <XStack 
                  ai="center" 
                  space="$2" 
                  px="$3" 
                  py="$2" 
                  br="$4"
                  backgroundColor={theme.bg}
                  borderLeftWidth={4}
                  borderLeftColor={theme.border}
                >
                  <IconComponent size={20} color={theme.icon} />
                  <H3 color={theme.accent} fontSize="$5" fontWeight="bold">{chapter.title}</H3>
                </XStack>
                
                {/* 考法卡片 */}
                {chapter.techniques.map((tech) => (
                  <TechniqueCard key={tech.id} tech={tech} theme={theme} />
                ))}
                
                {/* 专题集训入口 */}
                {quiz && <QuizCard quiz={quiz} theme={theme} />}
              </YStack>
            )
          })}
          
          {/* 期末冲刺练习入口 */}
          <YStack space="$3" mt="$4">
            <XStack 
              ai="center" 
              space="$2" 
              px="$3" 
              py="$2" 
              br="$4"
              backgroundColor="$orange2"
              borderLeftWidth={4}
              borderLeftColor="$orange8"
            >
              <Text fontSize="$6">🏆</Text>
              <H3 color="$orange10">七上期末冲刺练</H3>
            </XStack>
            
            <Link href="/quiz/final">
              <Card 
                p="$4" 
                borderWidth={2}
                borderColor="$orange6"
                backgroundColor="$orange2"
                pressStyle={{ opacity: 0.8, backgroundColor: '$orange3' }}
                hoverStyle={{ backgroundColor: '$orange3', borderColor: '$orange8' }}
                br="$4"
                ml="$2"
              >
                <XStack jc="space-between" ai="center">
                  <YStack space="$1" f={1}>
                    <Text fontWeight="bold" fontSize="$5" color="$orange10">期末冲刺练</Text>
                    <Text fontSize="$3" color="$orange11">共 16 道综合练习题 · 冲刺满分</Text>
                    <XStack ai="center" space="$1" mt="$1">
                      <Star size={14} color="$orange10" fill="$orange10" />
                      <Star size={14} color="$orange10" fill="$orange10" />
                      <Star size={14} color="$orange10" fill="$orange10" />
                      <Star size={14} color="$orange10" fill="$orange10" />
                      <Star size={14} color="$orange10" fill="$orange10" />
                      <Text fontSize="$2" color="$orange10" ml="$1">综合挑战</Text>
                    </XStack>
                  </YStack>
                  <XStack
                    width={32}
                    height={32}
                    br={16}
                    backgroundColor="$orange6"
                    ai="center"
                    jc="center"
                  >
                    <ChevronRight size={18} color="white" />
                  </XStack>
                </XStack>
              </Card>
            </Link>
          </YStack>
          
          <Separator my="$4" />
          
          {/* 底部按钮 */}
          <XStack space="$3" jc="center" pb="$8">
            <Button 
              theme="gray" 
              size="$4" 
              br="$10"
              backgroundColor="$gray3"
              borderWidth={1}
              borderColor="$gray6"
              color="$gray11"
            >
              初二内容(敬请期待)
            </Button>
            <Button 
              theme="gray" 
              size="$4" 
              br="$10"
              backgroundColor="$gray3"
              borderWidth={1}
              borderColor="$gray6"
              color="$gray11"
            >
              初三内容(敬请期待)
            </Button>
          </XStack>
        </YStack>
      </ScrollView>
    </YStack>
  )
}
