import React from 'react'
import { Text, TextProps, YStack, XStack } from 'tamagui'
// 注意：在 Native 环境下，我们需要特殊的 LaTeX 渲染，这里先写 Web 版逻辑
// 实际项目中我们会使用 .native.tsx 来区分
import 'katex/dist/katex.min.css'
import { InlineMath, BlockMath } from 'react-katex'

interface MathTextProps extends TextProps {
  content: string
  block?: boolean
}

export function MathText({ content, block, ...props }: MathTextProps) {
  if (block) {
    return (
      <Text {...props}>
        <BlockMath math={content} />
      </Text>
    )
  }

  // 先处理块级公式 $$...$$
  // 然后处理行内公式 $...$
  // 使用 [\s\S] 来匹配包括换行符的任意字符
  
  const renderContent = () => {
    const result: React.ReactNode[] = []
    let remaining = content
    let key = 0
    
    while (remaining.length > 0) {
      // 查找块级公式 $$...$$
      const blockMatch = remaining.match(/^\$\$([\s\S]*?)\$\$/)
      if (blockMatch) {
        result.push(
          <YStack key={key++} my="$2">
            <BlockMath math={blockMatch[1]} />
          </YStack>
        )
        remaining = remaining.slice(blockMatch[0].length)
        continue
      }
      
      // 查找行内公式 $...$
      const inlineMatch = remaining.match(/^\$((?:[^$\\]|\\.)+)\$/)
      if (inlineMatch) {
        try {
          result.push(<InlineMath key={key++} math={inlineMatch[1]} />)
        } catch (e) {
          // 如果 KaTeX 解析失败，显示原始文本
          result.push(<Text key={key++} color="$red10">{inlineMatch[0]}</Text>)
        }
        remaining = remaining.slice(inlineMatch[0].length)
        continue
      }
      
      // 查找下一个 $ 符号
      const nextDollar = remaining.indexOf('$')
      if (nextDollar === -1) {
        // 没有更多公式，添加剩余文本
        result.push(remaining)
        break
      } else if (nextDollar > 0) {
        // 添加 $ 之前的普通文本
        result.push(remaining.slice(0, nextDollar))
        remaining = remaining.slice(nextDollar)
      } else {
        // 如果 $ 在开头但没有匹配到公式模式，可能是单独的 $ 符号
        result.push('$')
        remaining = remaining.slice(1)
      }
    }
    
    return result
  }

  return (
    <Text {...props} style={{ display: 'block' }}>
      {renderContent()}
    </Text>
  )
}
