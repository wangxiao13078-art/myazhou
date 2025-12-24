#!/usr/bin/env python3
"""
为剩余题目生成练习题SVG图形
t6, t8, t9, t10, t11, t16, t17, t18, t20, t21, t24, t25, t26
"""

from pathlib import Path

OUTPUT_DIR = Path("/Users/youyou/Downloads/M压轴/packages/svg_figures")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def svg(width, height, content):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<style>
text {{ font-family: -apple-system, 'Helvetica Neue', sans-serif; }}
.formula {{ font-size: 16px; fill: #333; font-weight: 500; font-style: italic; }}
.label {{ font-size: 14px; fill: #333; font-weight: 500; }}
.small {{ font-size: 12px; fill: #666; }}
.box {{ stroke: #667eea; stroke-width: 2; fill: rgba(102,126,234,0.05); rx: 8; }}
.highlight {{ fill: #fef3c7; stroke: #fbbf24; }}
.arrow {{ fill: #667eea; }}
.line {{ stroke: #667eea; stroke-width: 2; }}
</style>
<defs>
<marker id="arrow-right" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
<path d="M0,0 L0,6 L9,3 z" class="arrow"/>
</marker>
</defs>
{content}
</svg>'''

def save(filename, content):
    (OUTPUT_DIR / filename).write_text(content, encoding='utf-8')
    print(f"  ✅ {filename}")

# ========== 公式框 ==========

def formula_box(formulas, title="", width=350, height=None):
    """公式展示框"""
    if height is None:
        height = 60 + len(formulas) * 35
    
    c = []
    # 背景框
    c.append(f'<rect x="10" y="10" width="{width-20}" height="{height-20}" class="box"/>')
    
    # 标题
    if title:
        c.append(f'<text x="25" y="35" class="label">{title}</text>')
        y_start = 60
    else:
        y_start = 40
    
    # 公式
    for i, formula in enumerate(formulas):
        y = y_start + i * 32
        c.append(f'<text x="30" y="{y}" class="formula">{formula}</text>')
    
    return svg(width, height, '\n'.join(c))

def calculation_steps(steps, width=380, height=None):
    """计算步骤框"""
    if height is None:
        height = 50 + len(steps) * 30
    
    c = []
    c.append(f'<rect x="10" y="10" width="{width-20}" height="{height-20}" class="box"/>')
    
    for i, step in enumerate(steps):
        y = 40 + i * 28
        # 步骤编号
        c.append(f'<circle cx="25" cy="{y-5}" r="10" fill="#667eea"/>')
        c.append(f'<text x="25" y="{y}" text-anchor="middle" fill="white" font-size="11">{i+1}</text>')
        # 内容
        c.append(f'<text x="45" y="{y}" class="small">{step}</text>')
    
    return svg(width, height, '\n'.join(c))

def definition_box(symbol, definition, example, width=350, height=120):
    """新定义展示框"""
    c = []
    # 主框
    c.append(f'<rect x="10" y="10" width="{width-20}" height="{height-20}" class="box"/>')
    
    # 定义符号
    c.append(f'<rect x="20" y="25" width="60" height="35" class="highlight" rx="5"/>')
    c.append(f'<text x="50" y="50" text-anchor="middle" class="formula">{symbol}</text>')
    
    # 定义内容
    c.append(f'<text x="95" y="48" class="label">{definition}</text>')
    
    # 示例
    c.append(f'<text x="25" y="85" class="small">例：{example}</text>')
    
    return svg(width, height, '\n'.join(c))

def fraction_sequence(n=5, width=400, height=80):
    """分数序列图"""
    c = []
    c.append(f'<rect x="10" y="10" width="{width-20}" height="{height-20}" class="box"/>')
    
    # 序列
    x_start = 30
    spacing = 70
    for i in range(1, n+1):
        x = x_start + (i-1) * spacing
        # 分数
        c.append(f'<text x="{x}" y="35" class="small">1</text>')
        c.append(f'<line x1="{x-5}" y1="40" x2="{x+15}" y2="40" stroke="#333" stroke-width="1"/>')
        c.append(f'<text x="{x}" y="55" class="small">{i}×{i+1}</text>')
        # 加号或省略号
        if i < n:
            c.append(f'<text x="{x+40}" y="45" class="label">+</text>')
    
    c.append(f'<text x="{x_start + n*spacing - 20}" y="45" class="label">+ ...</text>')
    
    return svg(width, height, '\n'.join(c))

def substitution_diagram(width=350, height=100):
    """整体代入示意图"""
    c = []
    c.append(f'<rect x="10" y="10" width="{width-20}" height="{height-20}" class="box"/>')
    
    # 原式
    c.append(f'<text x="30" y="40" class="label">4(a+b) - 2(a+b)</text>')
    
    # 箭头
    c.append(f'<line x1="170" y1="35" x2="210" y2="35" class="line" marker-end="url(#arrow-right)"/>')
    c.append(f'<text x="190" y="55" text-anchor="middle" class="small">整体</text>')
    
    # 结果
    c.append(f'<text x="225" y="40" class="label">(4-2)(a+b) = 2(a+b)</text>')
    
    # 高亮 (a+b)
    c.append(f'<rect x="50" y="22" width="50" height="25" class="highlight" rx="3"/>')
    c.append(f'<rect x="118" y="22" width="50" height="25" class="highlight" rx="3"/>')
    
    return svg(width, height, '\n'.join(c))

def equation_solve(width=320, height=100):
    """方程求解示意图"""
    c = []
    c.append(f'<rect x="10" y="10" width="{width-20}" height="{height-20}" class="box"/>')
    
    # 方程
    c.append(f'<text x="30" y="40" class="formula">½(2x-1) + ⅙(2x-1) + ⅓(2x-1) = 5</text>')
    
    # 提取公因式
    c.append(f'<line x1="30" y1="55" x2="290" y2="55" stroke="#667eea" stroke-width="1" stroke-dasharray="3,3"/>')
    c.append(f'<text x="30" y="75" class="small">合并系数：(½ + ⅙ + ⅓)(2x-1) = 1·(2x-1) = 5</text>')
    
    return svg(width, height, '\n'.join(c))

# ========== 主函数 ==========

def main():
    print("=" * 60)
    print("🎨 为剩余题目生成练习题SVG图形")
    print("=" * 60)
    
    # t6: 新定义问题
    print("\n📚 t6 练习题")
    save("t6_train_1.svg", definition_box("a⊙b", "= a(a+b) - 1", "(1⊙2)⊙3 = ?"))
    save("t6_train_2.svg", formula_box([
        "定义：C_n^m = n!/(m!(n-m)!)",
        "例：C_6^2 = 6×5/(2×1) = 15"
    ], "组合数定义"))
    
    # t8: 拼凑法
    print("\n📚 t8 练习题")
    save("t8_train_1.svg", calculation_steps([
        "将小数转化为分数",
        "互为相反数的先相加得0",
        "分母相同的分数先相加",
        "整数部分和分数部分分别相加"
    ]))
    
    # t9: 裂项法
    print("\n📚 t9 练习题")
    save("t9_train_1.svg", fraction_sequence())
    save("t9_train_2.svg", formula_box([
        "1/(n(n+1)) = 1/n - 1/(n+1)",
        "裂项相消，剩首尾"
    ], "裂项公式"))
    
    # t10: 倒数法
    print("\n📚 t10 练习题")
    save("t10_train_1.svg", formula_box([
        "a × 1/a = 1 (倒数关系)",
        "分配律：a(b+c) = ab + ac"
    ], "运算技巧"))
    
    # t11: 混合运算
    print("\n📚 t11 练习题")
    save("t11_train_1.svg", calculation_steps([
        "先算乘方：(-1)⁶ = 1，(-3)³ = -27",
        "再算括号内：0.5 - ⅔ = -⅙",
        "然后乘除",
        "最后加减"
    ]))
    
    # t16: 用字母表示数
    print("\n📚 t16 练习题")
    save("t16_train_1.svg", formula_box([
        "面积 = 长 × 宽",
        "周长 = 2(长 + 宽)"
    ], "几何公式"))
    
    # t17: 代数式求值
    print("\n📚 t17 练习题")
    save("t17_train_1.svg", calculation_steps([
        "写出代数式",
        "代入已知值",
        "按运算顺序计算",
        "得出结果"
    ]))
    
    # t18: 整体思想
    print("\n📚 t18 练习题")
    save("t18_train_1.svg", substitution_diagram())
    
    # t20: 代数式新定义
    print("\n📚 t20 练习题")
    save("t20_train_1.svg", definition_box("C_n^m", "= n(n-1)...(n-m+1)/(m!)", "C_8^3 = 56"))
    
    # t21: 化简求值
    print("\n📚 t21 练习题")
    save("t21_train_1.svg", formula_box([
        "将 (a+b) 看作整体",
        "(a-c) + (c-d) = a-d",
        "利用整体关系化简"
    ], "整体思想"))
    
    # t24: 新定义
    print("\n📚 t24 练习题")
    save("t24_train_1.svg", definition_box("(a,b)", "有趣数对：a-b=2ab", "(2, 0.4) → 2-0.4=2×2×0.4"))
    
    # t25: 整体思想解方程
    print("\n📚 t25 练习题")
    save("t25_train_1.svg", equation_solve())
    
    # t26: 裂项相消解方程
    print("\n📚 t26 练习题")
    save("t26_train_1.svg", formula_box([
        "x(1 - 1/2)(1 - 1/3)...(1 - 1/23) = 22",
        "提取x，括号内裂项相消"
    ], "裂项相消"))
    
    print("\n" + "=" * 60)
    print("✅ 剩余题目SVG图形生成完成！")

if __name__ == "__main__":
    main()


