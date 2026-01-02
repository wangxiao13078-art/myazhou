import { NextRequest, NextResponse } from 'next/server'
import { SolutionSchema } from '../../../../../packages/app/features/tutor/types'

// 系统提示词 - 定义 AI 如何解题和生成白板动画步骤
const SYSTEM_PROMPT = `You are a helpful math tutor. Analyze the math problem in the image and provide a detailed step-by-step solution in CHINESE (简体中文) suitable for an animated whiteboard presentation.

Return your response as a valid JSON object with this exact structure:
{
  "title": "题目名称 (中文)",
  "steps": [
    {
      "explanation": "本步骤的详细中文解释 (可以使用 LaTeX 格式的数学符号，如 $x^2$)",
      "drawings": [
        { 
          "id": "unique_id_1", 
          "type": "math", 
          "x": 50, 
          "y": 50, 
          "content": "LaTeX mathematical expression (WITHOUT dollars, e.g., 'x^2 + 5x + 6 = 0')", 
          "color": "#1a1a1a", 
          "duration": 1000 
        }
      ]
    }
  ],
  "finalAnswer": "最终答案 (中文)"
}

Guidelines:
- IMPORTANT: All text (title, explanation, finalAnswer) MUST be in Simplified Chinese (简体中文).
- Use "type": "math" for equations and formulas. Content should be standard LaTeX string.
- Use "type": "text" for labels and short textual notes on the whiteboard.
- Position drawings using x (0-400) and y (0-350) coordinates.
- Space out y coordinates by at least 40-50 pixels between lines.
- Use colors: #1a1a1a (black), #4f46e5 (purple), #10b981 (green), #ef4444 (red).
- Each step should have 1-3 drawings.
- Provide 3-6 steps total.
- Keep content concise for whiteboard display.`

// Mock response for development without API key
const MOCK_SOLUTION = {
  title: "演示：求解一元二次方程",
  steps: [
    {
      explanation: "这是一个演示方案。要解决您真实的数学问题，请配置 API Key（OpenAI 或 Google Gemini）。",
      drawings: [
        { id: '1', type: 'math' as const, x: 50, y: 50, content: 'x^2 + 5x + 6 = 0', color: '#1a1a1a', duration: 1000 },
        { id: '2', type: 'text' as const, x: 50, y: 100, content: '识别系数: a=1, b=5, c=6', color: '#4f46e5', duration: 800 }
      ]
    },
    {
      explanation: "通过寻找两个数，它们的乘积等于 6 且和等于 5，来对方程进行因式分解。",
      drawings: [
        { id: '3', type: 'text' as const, x: 50, y: 150, content: '2 \\times 3 = 6 \\checkmark', color: '#10b981', duration: 800 },
        { id: '4', type: 'text' as const, x: 50, y: 190, content: '2 + 3 = 5 \\checkmark', color: '#10b981', duration: 800 }
      ]
    },
    {
      explanation: "写出方程的因式分解形式。",
      drawings: [
        { id: '5', type: 'math' as const, x: 50, y: 240, content: '(x + 2)(x + 3) = 0', color: '#4f46e5', duration: 1200 }
      ]
    },
    {
      explanation: "令每个因式等于零并求解 x。",
      drawings: [
        { id: '6', type: 'math' as const, x: 50, y: 290, content: 'x = -2', color: '#ef4444', duration: 1000 },
        { id: '7', type: 'math' as const, x: 150, y: 290, content: 'x = -3', color: '#ef4444', duration: 1000 }
      ]
    }
  ],
  finalAnswer: "x = -2 或 x = -3"
}

// 使用 Google Gemini API 解题
async function solveWithGemini(imageBase64: string) {
  const { GoogleGenerativeAI } = await import('@google/generative-ai')
  const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY!)
  
  // 使用更稳妥的模型名称和系统指令设置方式
  const model = genAI.getGenerativeModel({ 
    model: 'gemini-flash-latest',
    systemInstruction: SYSTEM_PROMPT,
  })
  
  // 提取 base64 数据
  const base64Match = imageBase64.match(/^data:(image\/\w+);base64,(.*)$/)
  let mimeType = 'image/jpeg'
  let base64Data = imageBase64
  
  if (base64Match) {
    mimeType = base64Match[1]
    base64Data = base64Match[2]
  } else if (imageBase64.includes(',')) {
    base64Data = imageBase64.split(',')[1]
  }
  
  const result = await model.generateContent([
    {
      inlineData: {
        mimeType,
        data: base64Data
      }
    }
  ])
  
  const text = result.response.text()
  // 提取 JSON
  const jsonMatch = text.match(/\{[\s\S]*\}/)
  if (!jsonMatch) {
    console.error('Raw AI response:', text)
    throw new Error('AI 返回了非 JSON 格式的内容，请重试。')
  }
  
  try {
    return JSON.parse(jsonMatch[0])
  } catch (e) {
    console.error('JSON parse error. Raw match:', jsonMatch[0])
    throw new Error('AI 返回的数据格式有误，请重试。')
  }
}

// 使用 OpenAI API 解题
async function solveWithOpenAI(imageBase64: string) {
  const OpenAI = (await import('openai')).default
  const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY })
  
  const response = await openai.chat.completions.create({
    model: "gpt-4o",
    messages: [
      { role: "system", content: SYSTEM_PROMPT },
      {
        role: "user",
        content: [
          { type: "text", text: "Please solve this math problem and return JSON." },
          { type: "image_url", image_url: { url: imageBase64 } }
        ],
      },
    ],
    response_format: { type: "json_object" },
  })
  
  return JSON.parse(response.choices[0].message.content || '{}')
}

export async function POST(req: NextRequest) {
  try {
    const { image } = await req.json()

    if (!image) {
      return NextResponse.json({ error: 'Image is required' }, { status: 400 })
    }

    let result

    // 优先使用 Gemini（免费额度更多），其次 OpenAI
    if (process.env.GEMINI_API_KEY) {
      console.log('Using Google Gemini API...')
      result = await solveWithGemini(image)
    } else if (process.env.OPENAI_API_KEY) {
      console.log('Using OpenAI API...')
      result = await solveWithOpenAI(image)
    } else {
      // 没有配置任何 API Key，返回演示数据
      console.log('No API key configured, returning demo response')
      return NextResponse.json(MOCK_SOLUTION)
    }

    // 验证返回的数据结构
    const validated = SolutionSchema.parse(result)
    return NextResponse.json(validated)
    
  } catch (error: any) {
    console.error('Error solving problem:', error)
    return NextResponse.json({ error: error.message }, { status: 500 })
  }
}
