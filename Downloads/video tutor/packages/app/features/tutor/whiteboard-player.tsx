'use client'

import React, { useEffect, useState, useRef } from 'react'
import { Solution, WhiteboardStep } from './types'
import katex from 'katex'

interface WhiteboardPlayerProps {
  solution: Solution
  onClose: () => void
}

// 单个绘图元素 - 使用流式布局，不使用绝对定位
function DrawingItem({ drawing, delay }: { drawing: WhiteboardStep; delay: number }) {
  const [visible, setVisible] = useState(false)

  useEffect(() => {
    const timer = setTimeout(() => setVisible(true), delay)
    return () => clearTimeout(timer)
  }, [delay])

  const baseStyle: React.CSSProperties = {
    opacity: visible ? 1 : 0,
    transform: visible ? 'translateY(0)' : 'translateY(10px)',
    transition: `all ${drawing.duration || 500}ms cubic-bezier(0.4, 0, 0.2, 1)`,
    marginBottom: 16,
  }

  // 数学公式
  if (drawing.type === 'math') {
    return (
      <div
        style={{
          ...baseStyle,
          textAlign: 'center',
          padding: '8px 16px',
        }}
        dangerouslySetInnerHTML={{
          __html: katex.renderToString(drawing.content || '', {
            throwOnError: false,
            displayMode: true,
          }),
        }}
      />
    )
  }

  // 普通文字
  if (drawing.type === 'text') {
    return (
      <div
        style={{
          ...baseStyle,
          fontSize: 18,
          color: drawing.color || '#374151',
          textAlign: 'center',
          padding: '4px 16px',
        }}
      >
        {drawing.content}
      </div>
    )
  }

  // 图形元素（箭头、线条等）- 简化为装饰性元素
  if (drawing.type === 'arrow') {
    return (
      <div style={{ ...baseStyle, textAlign: 'center', fontSize: 24, color: drawing.color || '#4f46e5' }}>
        ↓
      </div>
    )
  }

  if (drawing.type === 'line') {
    return (
      <div style={{ ...baseStyle, display: 'flex', justifyContent: 'center' }}>
        <div style={{ 
          width: 100, 
          height: 2, 
          backgroundColor: drawing.color || '#e5e7eb',
          borderRadius: 1,
        }} />
      </div>
    )
  }

  if (drawing.type === 'highlight' || drawing.type === 'rect') {
    return null // 高亮框不单独显示，改为用CSS强调
  }

  if (drawing.type === 'circle') {
    return (
      <div style={{ ...baseStyle, textAlign: 'center', fontSize: 20, color: drawing.color || '#10b981' }}>
        ✓
      </div>
    )
  }

  return null
}

// 解释文本中的数学公式渲染
function ExplanationContent({ text }: { text: string }) {
  const parts = text.split(/(\$.*?\$|\\\(.*?\\\))/g)
  
  return (
    <>
      {parts.map((part, i) => {
        if (part.startsWith('$') && part.endsWith('$')) {
          const math = part.slice(1, -1)
          return (
            <span
              key={i}
              dangerouslySetInnerHTML={{
                __html: katex.renderToString(math, { throwOnError: false }),
              }}
            />
          )
        }
        if (part.startsWith('\\(') && part.endsWith('\\)')) {
          const math = part.slice(2, -2)
          return (
            <span
              key={i}
              dangerouslySetInnerHTML={{
                __html: katex.renderToString(math, { throwOnError: false }),
              }}
            />
          )
        }
        return <span key={i}>{part}</span>
      })}
    </>
  )
}

export function WhiteboardPlayer({ solution, onClose }: WhiteboardPlayerProps) {
  const [currentStepIndex, setCurrentStepIndex] = useState(0)
  const [key, setKey] = useState(0) // 用于强制重新渲染动画

  const currentStep = solution.steps[currentStepIndex]

  const nextStep = () => {
    if (currentStepIndex < solution.steps.length - 1) {
      setCurrentStepIndex(currentStepIndex + 1)
      setKey(k => k + 1) // 重置动画
    }
  }

  const prevStep = () => {
    if (currentStepIndex > 0) {
      setCurrentStepIndex(currentStepIndex - 1)
      setKey(k => k + 1) // 重置动画
    }
  }

  return (
    <div style={styles.container}>
      {/* 头部 */}
      <div style={styles.header}>
        <h2 style={styles.title}>{solution.title}</h2>
        <button onClick={onClose} style={styles.closeButton}>
          ← 返回
        </button>
      </div>

      {/* 白板区域 - 只显示当前步骤 */}
      <div style={styles.whiteboard} key={key}>
        <div style={styles.stepBadge}>
          步骤 {currentStepIndex + 1} / {solution.steps.length}
        </div>
        
        <div style={styles.drawingsContainer}>
          {currentStep?.drawings.map((drawing, idx) => (
            <DrawingItem 
              key={`${currentStepIndex}-${drawing.id}`} 
              drawing={drawing} 
              delay={idx * 300}
            />
          ))}
        </div>
      </div>

      {/* 讲解区域 */}
      <div style={styles.explanationSection}>
        <div style={styles.explanationHeader}>
          <span style={styles.explanationIcon}>💡</span>
          <span style={styles.explanationTitle}>讲解</span>
        </div>
        <p style={styles.explanationText}>
          <ExplanationContent text={currentStep?.explanation || ''} />
        </p>
      </div>

      {/* 最终答案 */}
      {currentStepIndex === solution.steps.length - 1 && (
        <div style={styles.finalAnswer}>
          <span style={styles.finalAnswerIcon}>🎯</span>
          <span style={styles.finalAnswerLabel}>答案：</span>
          <span style={styles.finalAnswerText}>{solution.finalAnswer}</span>
        </div>
      )}

      {/* 底部导航 */}
      <div style={styles.footer}>
        <button
          onClick={prevStep}
          disabled={currentStepIndex === 0}
          style={{
            ...styles.navButton,
            opacity: currentStepIndex === 0 ? 0.4 : 1,
            cursor: currentStepIndex === 0 ? 'not-allowed' : 'pointer',
          }}
        >
          ← 上一步
        </button>
        
        <div style={styles.stepIndicator}>
          {solution.steps.map((_, idx) => (
            <div
              key={idx}
              style={{
                width: 10,
                height: 10,
                borderRadius: '50%',
                backgroundColor: idx === currentStepIndex ? '#4f46e5' : idx < currentStepIndex ? '#10b981' : '#d1d5db',
                margin: '0 4px',
                transition: 'all 0.3s',
              }}
            />
          ))}
        </div>

        <button
          onClick={nextStep}
          disabled={currentStepIndex === solution.steps.length - 1}
          style={{
            ...styles.nextButton,
            opacity: currentStepIndex === solution.steps.length - 1 ? 0.6 : 1,
            cursor: currentStepIndex === solution.steps.length - 1 ? 'not-allowed' : 'pointer',
          }}
        >
          {currentStepIndex === solution.steps.length - 1 ? '已完成 ✓' : '下一步 →'}
        </button>
      </div>
    </div>
  )
}

const styles: Record<string, React.CSSProperties> = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    height: '100vh',
    padding: '12px 16px',
    backgroundColor: '#f8fafc',
    fontFamily: 'system-ui, -apple-system, sans-serif',
  },
  header: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 12,
    paddingBottom: 12,
    borderBottom: '1px solid #e2e8f0',
  },
  title: {
    fontSize: 18,
    fontWeight: 700,
    color: '#1e293b',
    margin: 0,
    flex: 1,
    overflow: 'hidden',
    textOverflow: 'ellipsis',
    whiteSpace: 'nowrap',
  },
  closeButton: {
    padding: '8px 16px',
    fontSize: 14,
    fontWeight: 500,
    backgroundColor: '#fff',
    color: '#475569',
    border: '1px solid #e2e8f0',
    borderRadius: 8,
    cursor: 'pointer',
    flexShrink: 0,
    marginLeft: 12,
  },
  whiteboard: {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    backgroundColor: '#ffffff',
    borderRadius: 16,
    border: '3px solid #334155',
    boxShadow: '0 4px 20px rgba(0,0,0,0.08)',
    overflow: 'auto',
    position: 'relative',
  },
  stepBadge: {
    position: 'absolute',
    top: 12,
    left: 12,
    padding: '6px 12px',
    fontSize: 12,
    fontWeight: 600,
    backgroundColor: '#4f46e5',
    color: '#fff',
    borderRadius: 20,
  },
  drawingsContainer: {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    padding: '60px 24px 24px',
    minHeight: 200,
  },
  explanationSection: {
    marginTop: 12,
    padding: 16,
    backgroundColor: '#fff',
    borderRadius: 12,
    border: '1px solid #e2e8f0',
  },
  explanationHeader: {
    display: 'flex',
    alignItems: 'center',
    gap: 8,
    marginBottom: 8,
  },
  explanationIcon: {
    fontSize: 18,
  },
  explanationTitle: {
    fontSize: 14,
    fontWeight: 600,
    color: '#475569',
  },
  explanationText: {
    fontSize: 16,
    lineHeight: 1.8,
    color: '#334155',
    margin: 0,
  },
  finalAnswer: {
    marginTop: 12,
    padding: 16,
    backgroundColor: '#ecfdf5',
    borderRadius: 12,
    border: '2px solid #10b981',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    flexWrap: 'wrap',
  },
  finalAnswerIcon: {
    fontSize: 20,
  },
  finalAnswerLabel: {
    fontSize: 14,
    fontWeight: 600,
    color: '#059669',
  },
  finalAnswerText: {
    fontSize: 18,
    fontWeight: 700,
    color: '#065f46',
  },
  footer: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginTop: 12,
    paddingTop: 12,
    borderTop: '1px solid #e2e8f0',
  },
  navButton: {
    padding: '10px 20px',
    fontSize: 14,
    fontWeight: 500,
    backgroundColor: '#fff',
    color: '#475569',
    border: '1px solid #e2e8f0',
    borderRadius: 8,
  },
  nextButton: {
    padding: '10px 24px',
    fontSize: 14,
    fontWeight: 600,
    backgroundColor: '#4f46e5',
    color: '#fff',
    border: 'none',
    borderRadius: 8,
  },
  stepIndicator: {
    display: 'flex',
    alignItems: 'center',
  },
}
