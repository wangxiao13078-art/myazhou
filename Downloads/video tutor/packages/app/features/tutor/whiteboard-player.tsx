'use client'

import React, { useEffect, useState } from 'react'
import { Solution, WhiteboardStep } from './types'
import katex from 'katex'

interface WhiteboardPlayerProps {
  solution: Solution
  onClose: () => void
}

// 渲染包含 LaTeX 的文本
function renderMathText(text: string): string {
  // 替换 $...$ 格式的数学公式
  return text.replace(/\$([^$]+)\$/g, (_, math) => {
    try {
      return katex.renderToString(math, { throwOnError: false })
    } catch {
      return math
    }
  })
}

// 单个绘图元素 - 使用流式布局
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
    marginBottom: 12,
  }

  // 数学公式
  if (drawing.type === 'math') {
    return (
      <div
        style={{
          ...baseStyle,
          textAlign: 'center',
          padding: '4px 16px',
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
          fontSize: 16,
          color: drawing.color || '#374151',
          textAlign: 'center',
          padding: '4px 16px',
        }}
        dangerouslySetInnerHTML={{
          __html: renderMathText(drawing.content || ''),
        }}
      />
    )
  }

  // 箭头
  if (drawing.type === 'arrow') {
    return (
      <div style={{ ...baseStyle, textAlign: 'center' }}>
        <svg width="40" height="40" viewBox="0 0 40 40">
          <defs>
            <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
              <polygon points="0 0, 10 3.5, 0 7" fill={drawing.color || '#4f46e5'} />
            </marker>
          </defs>
          <line x1="20" y1="5" x2="20" y2="30" stroke={drawing.color || '#4f46e5'} strokeWidth="2" markerEnd="url(#arrowhead)" />
        </svg>
      </div>
    )
  }

  // 线条
  if (drawing.type === 'line') {
    return (
      <div style={{ ...baseStyle, display: 'flex', justifyContent: 'center' }}>
        <div style={{ 
          width: 80, 
          height: 3, 
          backgroundColor: drawing.color || '#e5e7eb',
          borderRadius: 2,
        }} />
      </div>
    )
  }

  // 矩形框
  if (drawing.type === 'rect') {
    return (
      <div style={{ ...baseStyle, display: 'flex', justifyContent: 'center' }}>
        <div style={{ 
          width: 120, 
          height: 40, 
          border: `2px solid ${drawing.color || '#10b981'}`,
          borderRadius: 8,
          backgroundColor: drawing.fill || 'transparent',
        }} />
      </div>
    )
  }

  // 高亮框
  if (drawing.type === 'highlight') {
    return (
      <div style={{ ...baseStyle, display: 'flex', justifyContent: 'center' }}>
        <div style={{ 
          width: 100, 
          height: 30, 
          border: `2px dashed ${drawing.color || '#f59e0b'}`,
          borderRadius: 6,
          backgroundColor: 'rgba(251, 191, 36, 0.1)',
        }} />
      </div>
    )
  }

  // 圆形/勾号
  if (drawing.type === 'circle') {
    return (
      <div style={{ ...baseStyle, textAlign: 'center' }}>
        <svg width="40" height="40" viewBox="0 0 40 40">
          <circle cx="20" cy="20" r="15" stroke={drawing.color || '#10b981'} strokeWidth="3" fill="none" />
          <path d="M12 20 L18 26 L28 14" stroke={drawing.color || '#10b981'} strokeWidth="3" fill="none" strokeLinecap="round" strokeLinejoin="round" />
        </svg>
      </div>
    )
  }

  // 弧线
  if (drawing.type === 'arc') {
    return (
      <div style={{ ...baseStyle, textAlign: 'center' }}>
        <svg width="60" height="30" viewBox="0 0 60 30">
          <path d="M5 25 Q30 0 55 25" stroke={drawing.color || '#4f46e5'} strokeWidth="2" fill="none" />
        </svg>
      </div>
    )
  }

  return null
}

// 解释文本中的数学公式渲染
function ExplanationContent({ text }: { text: string }) {
  return (
    <span dangerouslySetInnerHTML={{ __html: renderMathText(text) }} />
  )
}

export function WhiteboardPlayer({ solution, onClose }: WhiteboardPlayerProps) {
  const [currentStepIndex, setCurrentStepIndex] = useState(0)
  const [key, setKey] = useState(0)

  const currentStep = solution.steps[currentStepIndex]

  const nextStep = () => {
    if (currentStepIndex < solution.steps.length - 1) {
      setCurrentStepIndex(currentStepIndex + 1)
      setKey(k => k + 1)
    }
  }

  const prevStep = () => {
    if (currentStepIndex > 0) {
      setCurrentStepIndex(currentStepIndex - 1)
      setKey(k => k + 1)
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

      {/* 白板区域 */}
      <div style={styles.whiteboard} key={key}>
        <div style={styles.stepBadge}>
          步骤 {currentStepIndex + 1} / {solution.steps.length}
        </div>
        
        <div style={styles.drawingsContainer}>
          {currentStep?.drawings.map((drawing, idx) => (
            <DrawingItem 
              key={`${currentStepIndex}-${drawing.id}`} 
              drawing={drawing} 
              delay={idx * 250}
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
          <span 
            style={styles.finalAnswerText}
            dangerouslySetInnerHTML={{ __html: renderMathText(solution.finalAnswer) }}
          />
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
