'use client'

import React, { useState, useRef } from 'react'
import { WhiteboardPlayer } from './whiteboard-player'
import { Solution } from './types'

// 演示方案：求解一元二次方程 - 包含图形和复杂公式
const DEMO_SOLUTION: Solution = {
  title: "演示：用公式法求解一元二次方程",
  steps: [
    {
      explanation: "给定方程 $x^2 + 5x + 6 = 0$，首先识别系数：$a=1$, $b=5$, $c=6$。",
      drawings: [
        // 方程 (居中)
        { id: '1', type: 'math', x: 280, y: 50, content: 'x^2 + 5x + 6 = 0', color: '#1a1a1a', duration: 800 },
        // 箭头指向系数说明
        { id: '3', type: 'arrow', x: 400, y: 80, x2: 400, y2: 120, color: '#4f46e5', strokeWidth: 2, duration: 500 },
        // 系数说明
        { id: '4', type: 'math', x: 280, y: 140, content: 'a=1, \\quad b=5, \\quad c=6', color: '#4f46e5', duration: 800 },
      ]
    },
    {
      explanation: "使用求根公式：$x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$",
      drawings: [
        // 公式框 (先画框)
        { id: '6', type: 'rect', x: 180, y: 200, width: 400, height: 90, color: '#10b981', strokeWidth: 2, duration: 600 },
        // 求根公式 (居中)
        { id: '5', type: 'math', x: 250, y: 230, content: 'x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}', color: '#1a1a1a', duration: 1000 },
      ]
    },
    {
      explanation: "代入系数计算判别式：$\\Delta = b^2 - 4ac = 25 - 24 = 1$",
      drawings: [
        // 判别式公式
        { id: '8', type: 'math', x: 50, y: 320, content: '\\Delta = b^2 - 4ac', color: '#1a1a1a', duration: 800 },
        // 等号箭头
        { id: '9', type: 'arrow', x: 280, y: 335, x2: 340, y2: 335, color: '#f59e0b', strokeWidth: 2, duration: 500 },
        // 代入数值
        { id: '10', type: 'math', x: 360, y: 320, content: '= 5^2 - 4 \\cdot 1 \\cdot 6', color: '#f59e0b', duration: 800 },
        // 结果
        { id: '11', type: 'math', x: 250, y: 380, content: '= 25 - 24 = 1', color: '#10b981', duration: 800 },
        // 结果圈出
        { id: '12', type: 'circle', x: 390, y: 395, radius: 25, color: '#10b981', strokeWidth: 3, duration: 500 },
      ]
    },
    {
      explanation: "因为 $\\Delta = 1 > 0$，方程有两个不相等的实根。代入公式求解：",
      drawings: [
        // 求解过程
        { id: '13', type: 'math', x: 80, y: 440, content: 'x = \\frac{-5 \\pm 1}{2}', color: '#1a1a1a', duration: 1000 },
        // 分支线
        { id: '14', type: 'line', x: 280, y: 455, x2: 330, y2: 480, color: '#ef4444', strokeWidth: 2, duration: 400 },
        { id: '15', type: 'line', x: 280, y: 455, x2: 330, y2: 430, color: '#3b82f6', strokeWidth: 2, duration: 400 },
        // 两个解
        { id: '16', type: 'math', x: 350, y: 415, content: 'x_1 = -2', color: '#3b82f6', duration: 800 },
        { id: '17', type: 'math', x: 350, y: 470, content: 'x_2 = -3', color: '#ef4444', duration: 800 },
      ]
    }
  ],
  finalAnswer: "x₁ = -2  或  x₂ = -3"
}

export function TutorScreen() {
  const [image, setImage] = useState<string | null>(null)
  const [solution, setSolution] = useState<Solution | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const fileInputRef = useRef<HTMLInputElement>(null)

  const solveProblem = async () => {
    if (!image) return
    setLoading(true)
    setError(null)

    try {
      const response = await fetch('/api/solve', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ image }),
      })

      const data = await response.json()

      if (!response.ok) {
        let userMessage = '无法解决该题目，请检查网络或重试。'
        
        if (data.error?.includes('Generative Language API has not been used')) {
          userMessage = 'AI 服务尚未启用。请访问 Google Cloud 控制台启用 "Generative Language API"。'
        } else if (data.error?.includes('404')) {
          userMessage = 'AI 模型加载失败 (404)。请确保 API Key 正确且模型可用。'
        } else if (data.error?.includes('API key not valid')) {
          userMessage = 'API Key 无效，请检查配置。'
        }
        
        throw new Error(userMessage)
      }

      setSolution(data)
    } catch (err: any) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  const runDemo = () => {
    setSolution(DEMO_SOLUTION)
  }

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (file) {
      const reader = new FileReader()
      reader.onloadend = () => {
        setImage(reader.result as string)
      }
      reader.readAsDataURL(file)
    }
  }

  if (solution) {
    return <WhiteboardPlayer solution={solution} onClose={() => setSolution(null)} />
  }

  return (
    <div style={styles.container}>
      <input
        type="file"
        ref={fileInputRef}
        onChange={handleFileChange}
        accept="image/*"
        style={{ display: 'none' }}
      />

      <h1 style={styles.title}>AI 数学老师</h1>

      <div style={styles.content}>
        {image ? (
          <div style={styles.imageContainer}>
            <img src={image} alt="数学题" style={styles.image} />
            <button onClick={() => setImage(null)} style={styles.removeButton}>
              删除图片
            </button>
          </div>
        ) : (
          <div style={styles.uploadContainer}>
            <p style={styles.hint}>请上传一张数学题的照片</p>
            <div style={styles.buttonGroup}>
              <button onClick={() => fileInputRef.current?.click()} style={styles.pickButton}>
                选择图片
              </button>
              <button onClick={runDemo} style={styles.demoButton}>
                运行演示
              </button>
            </div>
          </div>
        )}
      </div>

      {error && <p style={styles.error}>{error}</p>}

      {image && (
        <button
          onClick={solveProblem}
          disabled={loading}
          style={{
            ...styles.solveButton,
            opacity: loading ? 0.7 : 1,
          }}
        >
          {loading ? '正在分析题目...' : '使用 AI 解题'}
        </button>
      )}
    </div>
  )
}

const styles: Record<string, React.CSSProperties> = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    minHeight: '100vh',
    padding: 24,
    backgroundColor: '#fafafa',
    fontFamily: 'system-ui, -apple-system, sans-serif',
  },
  title: {
    fontSize: 28,
    fontWeight: 700,
    textAlign: 'center',
    marginBottom: 32,
    color: '#1a1a1a',
  },
  content: {
    flex: 1,
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
  uploadContainer: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    gap: 16,
  },
  hint: {
    color: '#666',
    fontSize: 16,
  },
  buttonGroup: {
    display: 'flex',
    gap: 12,
  },
  pickButton: {
    padding: '12px 24px',
    fontSize: 16,
    fontWeight: 600,
    backgroundColor: '#4f46e5',
    color: 'white',
    border: 'none',
    borderRadius: 8,
    cursor: 'pointer',
  },
  demoButton: {
    padding: '12px 24px',
    fontSize: 16,
    fontWeight: 600,
    backgroundColor: '#f59e0b',
    color: 'white',
    border: 'none',
    borderRadius: 8,
    cursor: 'pointer',
  },
  imageContainer: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    gap: 16,
  },
  image: {
    maxWidth: 300,
    maxHeight: 300,
    borderRadius: 8,
    boxShadow: '0 4px 12px rgba(0,0,0,0.1)',
  },
  removeButton: {
    padding: '8px 16px',
    fontSize: 14,
    backgroundColor: 'transparent',
    color: '#666',
    border: '1px solid #ddd',
    borderRadius: 6,
    cursor: 'pointer',
  },
  solveButton: {
    marginTop: 24,
    padding: '16px 32px',
    fontSize: 18,
    fontWeight: 600,
    backgroundColor: '#10b981',
    color: 'white',
    border: 'none',
    borderRadius: 10,
    cursor: 'pointer',
  },
  error: {
    color: '#ef4444',
    textAlign: 'center',
    marginTop: 16,
  },
}
