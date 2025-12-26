// math.js - 数学公式处理工具

/**
 * 将 LaTeX 公式转换为可读文本
 */
function renderMath(text) {
  if (!text) return ''

  // 首先统一反斜杠：将 \\\\ 转换为 \（处理双转义问题）
  let result = text.replace(/\\\\/g, '\\')

  // 移除 # 符号（用于标记的分隔符）
  result = result.replace(/#/g, '')

  // 处理独立公式块 $$...$$ （需要先处理，因为包含两个$）
  result = result.replace(/\$\$([\s\S]*?)\$\$/g, (match, formula) => {
    return formatFormula(formula)
  })

  // 处理行内公式 $...$
  result = result.replace(/\$([^$]+)\$/g, (match, formula) => {
    return formatFormula(formula)
  })

  // 处理不在 $ 内的 \text{...} 命令
  result = result.replace(/\\text\s*\{([^{}]*)\}/g, '$1')

  // 处理不在 $ 内的 \angle, \triangle 等符号
  result = result.replace(/\\angle/g, '∠')
  result = result.replace(/\\triangle/g, '△')
  result = result.replace(/\\times/g, '×')
  result = result.replace(/\\div/g, '÷')
  result = result.replace(/\\pm/g, '±')
  result = result.replace(/\\leq/g, '≤')
  result = result.replace(/\\geq/g, '≥')
  result = result.replace(/\\neq/g, '≠')
  result = result.replace(/\\pi/g, 'π')
  result = result.replace(/\\sqrt/g, '√')

  // 处理不在 $ 内的下标和上标（如 C_6^3）
  result = processInlineFormulas(result)

  // 处理换行
  result = result.replace(/\\n/g, '\n')

  // 清理残留的反斜杠命令
  result = result.replace(/\\[a-zA-Z]+\s*\{([^{}]*)\}/g, '$1')
  result = result.replace(/\\[a-zA-Z]+/g, '')

  return result.trim()
}

/**
 * 处理不在 $ 内的公式符号
 */
function processInlineFormulas(text) {
  let result = text

  // 处理 C_n^m 形式的组合数（数字版本）
  result = result.replace(/C_(\d+)\^(\d+)/g, (match, n, m) => {
    return 'C' + convertToSubscript(n) + convertToSuperscript(m)
  })

  // 处理 C_n^m 形式的组合数（字母版本）
  result = result.replace(/C_([a-zA-Z])\^([a-zA-Z])/g, (match, n, m) => {
    return 'C' + convertToSubscript(n) + convertToSuperscript(m)
  })

  // 处理 C_{...}^{...} 形式
  result = result.replace(/C_\{([^{}]+)\}\^\{([^{}]+)\}/g, (match, n, m) => {
    return 'C' + convertToSubscript(n) + convertToSuperscript(m)
  })

  // 处理单独的 ^m 或 ^n 形式
  result = result.replace(/\^([a-zA-Z0-9])/g, (match, exp) => {
    return convertToSuperscript(exp)
  })

  // 处理残留的 \cdots
  result = result.replace(/\\cdots/g, '⋯')

  return result
}

/**
 * 转换为下标
 */
function convertToSubscript(text) {
  const subscripts = {
    '0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄',
    '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉',
    'a': 'ₐ', 'e': 'ₑ', 'i': 'ᵢ', 'n': 'ₙ', 'o': 'ₒ',
    'r': 'ᵣ', 's': 'ₛ', 't': 'ₜ', 'u': 'ᵤ', 'v': 'ᵥ',
    'x': 'ₓ', '+': '₊', '-': '₋', '(': '₍', ')': '₎'
  }
  let result = ''
  for (const char of text) {
    result += subscripts[char] || char
  }
  return result
}

/**
 * 转换为上标
 */
function convertToSuperscript(text) {
  const superscripts = {
    '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
    '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹',
    'n': 'ⁿ', 'm': 'ᵐ', 'i': 'ⁱ', 'k': 'ᵏ', 'a': 'ᵃ', 'b': 'ᵇ', 'c': 'ᶜ',
    'x': 'ˣ', 'y': 'ʸ', 'z': 'ᶻ',
    '+': '⁺', '-': '⁻', '(': '⁽', ')': '⁾'
  }
  let result = ''
  for (const char of text) {
    result += superscripts[char] || char
  }
  return result
}

/**
 * 格式化数学公式
 * 将 LaTeX 命令转换为 Unicode
 */
function formatFormula(formula) {
  if (!formula) return ''

  let result = formula

  // ========== 处理分数 \frac{a}{b} → (a)/(b) ==========
  for (let i = 0; i < 5; i++) {
    result = result.replace(/\\frac\s*\{([^{}]*)\}\s*\{([^{}]*)\}/g, (match, num, den) => {
      const n = num.trim()
      const d = den.trim()
      if (n.length <= 3 && d.length <= 3 && !n.includes(' ') && !d.includes(' ')) {
        return `${n}/${d}`
      }
      return `(${n})/(${d})`
    })
  }

  // ========== 处理根号 ==========
  result = result.replace(/\\sqrt\s*\{([^{}]+)\}/g, '√($1)')
  result = result.replace(/\\sqrt\s*(\d+)/g, '√$1')
  result = result.replace(/\\sqrt/g, '√')

  // ========== 处理上标 ^{...} ==========
  result = result.replace(/\^\{([^{}]+)\}/g, (match, exp) => {
    return convertToSuperscript(exp)
  })
  
  // ^x 单字符形式
  result = result.replace(/\^([0-9n])/g, (match, char) => convertToSuperscript(char))

  // ========== 处理下标 _{...} ==========
  result = result.replace(/_\{([^{}]+)\}/g, (match, exp) => {
    return convertToSubscript(exp)
  })
  
  // _x 单字符形式
  result = result.replace(/_([0-9aeinx])/g, (match, char) => convertToSubscript(char))

  // ========== 处理文本命令 ==========
  result = result.replace(/\\text\s*\{([^{}]*)\}/g, '$1')
  result = result.replace(/\\textbf\s*\{([^{}]*)\}/g, '$1')
  result = result.replace(/\\textit\s*\{([^{}]*)\}/g, '$1')
  result = result.replace(/\\mathrm\s*\{([^{}]*)\}/g, '$1')
  result = result.replace(/\\mathbf\s*\{([^{}]*)\}/g, '$1')

  // ========== 希腊字母 ==========
  const greekLetters = {
    'alpha': 'α', 'beta': 'β', 'gamma': 'γ', 'delta': 'δ',
    'epsilon': 'ε', 'zeta': 'ζ', 'eta': 'η', 'theta': 'θ',
    'iota': 'ι', 'kappa': 'κ', 'lambda': 'λ', 'mu': 'μ',
    'nu': 'ν', 'xi': 'ξ', 'pi': 'π', 'rho': 'ρ',
    'sigma': 'σ', 'tau': 'τ', 'upsilon': 'υ', 'phi': 'φ',
    'chi': 'χ', 'psi': 'ψ', 'omega': 'ω',
    'Alpha': 'Α', 'Beta': 'Β', 'Gamma': 'Γ', 'Delta': 'Δ',
    'Theta': 'Θ', 'Lambda': 'Λ', 'Pi': 'Π', 'Sigma': 'Σ',
    'Phi': 'Φ', 'Psi': 'Ψ', 'Omega': 'Ω'
  }
  for (const [name, unicode] of Object.entries(greekLetters)) {
    result = result.replace(new RegExp('\\\\' + name + '(?![a-zA-Z])', 'g'), unicode)
  }

  // ========== 运算符和符号 ==========
  const operators = {
    'times': '×',
    'div': '÷',
    'pm': '±',
    'mp': '∓',
    'cdot': '·',
    'cdots': '⋯',
    'ldots': '…',
    'vdots': '⋮',
    'neq': '≠',
    'ne': '≠',
    'leq': '≤',
    'le': '≤',
    'geq': '≥',
    'ge': '≥',
    'approx': '≈',
    'equiv': '≡',
    'sim': '∼',
    'propto': '∝',
    'infty': '∞',
    'partial': '∂',
    'nabla': '∇',
    'sum': '∑',
    'prod': '∏',
    'int': '∫',
    'oint': '∮',
    'therefore': '∴',
    'because': '∵',
    'forall': '∀',
    'exists': '∃',
    'neg': '¬',
    'land': '∧',
    'lor': '∨',
    'oplus': '⊕',
    'otimes': '⊗'
  }
  for (const [name, unicode] of Object.entries(operators)) {
    result = result.replace(new RegExp('\\\\' + name + '(?![a-zA-Z])', 'g'), unicode)
  }

  // ========== 箭头 ==========
  const arrows = {
    'Rightarrow': '⇒',
    'rightarrow': '→',
    'Leftarrow': '⇐',
    'leftarrow': '←',
    'Leftrightarrow': '⇔',
    'leftrightarrow': '↔',
    'uparrow': '↑',
    'downarrow': '↓',
    'to': '→',
    'gets': '←',
    'mapsto': '↦'
  }
  for (const [name, unicode] of Object.entries(arrows)) {
    result = result.replace(new RegExp('\\\\' + name + '(?![a-zA-Z])', 'g'), unicode)
  }

  // ========== 集合符号 ==========
  const sets = {
    'in': '∈',
    'notin': '∉',
    'subset': '⊂',
    'subseteq': '⊆',
    'supset': '⊃',
    'supseteq': '⊇',
    'cup': '∪',
    'cap': '∩',
    'emptyset': '∅',
    'varnothing': '∅',
    'setminus': '∖'
  }
  for (const [name, unicode] of Object.entries(sets)) {
    result = result.replace(new RegExp('\\\\' + name + '(?![a-zA-Z])', 'g'), unicode)
  }

  // ========== 几何符号 ==========
  const geometry = {
    'angle': '∠',
    'triangle': '△',
    'square': '□',
    'circ': '°',
    'degree': '°',
    'parallel': '∥',
    'perp': '⊥',
    'cong': '≅'
  }
  for (const [name, unicode] of Object.entries(geometry)) {
    result = result.replace(new RegExp('\\\\' + name + '(?![a-zA-Z])', 'g'), unicode)
  }

  // ========== 括号 ==========
  result = result.replace(/\\left\s*\(/g, '(')
  result = result.replace(/\\right\s*\)/g, ')')
  result = result.replace(/\\left\s*\[/g, '[')
  result = result.replace(/\\right\s*\]/g, ']')
  result = result.replace(/\\left\s*\{/g, '{')
  result = result.replace(/\\right\s*\}/g, '}')
  result = result.replace(/\\left\s*\|/g, '|')
  result = result.replace(/\\right\s*\|/g, '|')
  result = result.replace(/\\lfloor/g, '⌊')
  result = result.replace(/\\rfloor/g, '⌋')
  result = result.replace(/\\lceil/g, '⌈')
  result = result.replace(/\\rceil/g, '⌉')
  result = result.replace(/\\left/g, '')
  result = result.replace(/\\right/g, '')

  // ========== 空格 ==========
  result = result.replace(/\\quad/g, '  ')
  result = result.replace(/\\qquad/g, '    ')
  result = result.replace(/\\,/g, ' ')
  result = result.replace(/\\;/g, ' ')
  result = result.replace(/\\:/g, ' ')
  result = result.replace(/\\ /g, ' ')
  result = result.replace(/~/g, ' ')

  // ========== 其他常用命令 ==========
  result = result.replace(/\\overline\s*\{([^{}]+)\}/g, '$1̅')
  result = result.replace(/\\underline\s*\{([^{}]+)\}/g, '$1')
  result = result.replace(/\\widehat\s*\{([^{}]+)\}/g, '$1̂')
  result = result.replace(/\\vec\s*\{([^{}]+)\}/g, '$1⃗')
  result = result.replace(/\\bar\s*\{([^{}]+)\}/g, '$1̄')
  result = result.replace(/\\dot\s*\{([^{}]+)\}/g, '$1̇')
  result = result.replace(/\\ddot\s*\{([^{}]+)\}/g, '$1̈')

  // ========== 清理 ==========
  // 移除剩余的未知 LaTeX 命令（保留命令后的内容）
  result = result.replace(/\\[a-zA-Z]+\s*\{([^{}]*)\}/g, '$1')
  // 移除独立的 LaTeX 命令
  result = result.replace(/\\[a-zA-Z]+/g, '')
  // 清理多余的花括号
  result = result.replace(/\{([^{}]*)\}/g, '$1')
  // 清理多余空格
  result = result.replace(/  +/g, ' ')

  return result.trim()
}

/**
 * 简化版：只做基本转换，用于标题等短文本
 */
function formatSimple(text) {
  if (!text) return ''
  let result = text.replace(/\\\\/g, '\\')
  return result
    .replace(/\$([^$]+)\$/g, '$1')
    .replace(/\\frac\{([^}]+)\}\{([^}]+)\}/g, '$1/$2')
    .replace(/\\text\{([^}]+)\}/g, '$1')
    .replace(/\\times/g, '×')
    .replace(/\\div/g, '÷')
    .replace(/\\pm/g, '±')
    .replace(/\\leq/g, '≤')
    .replace(/\\geq/g, '≥')
    .replace(/\\neq/g, '≠')
    .replace(/\\angle/g, '∠')
    .replace(/\\triangle/g, '△')
    .replace(/\\pi/g, 'π')
    .replace(/\\cdots/g, '⋯')
    .replace(/\\[a-zA-Z]+/g, '')
    .replace(/[{}]/g, '')
}

module.exports = {
  renderMath,
  formatFormula,
  formatSimple
}
