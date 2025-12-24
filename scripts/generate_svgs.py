#!/usr/bin/env python3
"""
生成数学题目所需的SVG图形
"""

import os

SVG_DIR = "../packages/app/assets/svg"

def ensure_dir():
    os.makedirs(SVG_DIR, exist_ok=True)

# ========== 数轴类型 ==========

def number_line_basic(filename, points=None, start=-5, end=5, title=""):
    """生成基础数轴SVG"""
    width = 600
    height = 100
    margin = 50
    line_y = 50
    
    # 计算刻度
    scale = (width - 2 * margin) / (end - start)
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
  
  <!-- 数轴主线 -->
  <line x1="{margin - 20}" y1="{line_y}" x2="{width - margin + 20}" y2="{line_y}" 
        stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
  
  <!-- 刻度和数字 -->
'''
    
    for i in range(start, end + 1):
        x = margin + (i - start) * scale
        svg += f'''  <line x1="{x}" y1="{line_y - 5}" x2="{x}" y2="{line_y + 5}" stroke="#333" stroke-width="1.5"/>
  <text x="{x}" y="{line_y + 20}" text-anchor="middle" font-size="12" fill="#333">{i}</text>
'''
    
    # 添加点
    if points:
        for point in points:
            name, value, color = point.get('name', ''), point.get('value', 0), point.get('color', '#e74c3c')
            x = margin + (value - start) * scale
            svg += f'''  <circle cx="{x}" cy="{line_y}" r="6" fill="{color}"/>
  <text x="{x}" y="{line_y - 15}" text-anchor="middle" font-size="14" font-weight="bold" fill="{color}">{name}</text>
'''
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def number_line_with_circle(filename, radius=1, start_pos=-1):
    """生成带圆的数轴（圆滚动问题）"""
    width = 600
    height = 150
    margin = 50
    line_y = 100
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
  
  <!-- 数轴主线 -->
  <line x1="{margin - 20}" y1="{line_y}" x2="{width - margin + 20}" y2="{line_y}" 
        stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
  
  <!-- 刻度 -->
'''
    scale = 40
    for i in range(-3, 8):
        x = margin + 120 + i * scale
        svg += f'''  <line x1="{x}" y1="{line_y - 5}" x2="{x}" y2="{line_y + 5}" stroke="#333" stroke-width="1.5"/>
  <text x="{x}" y="{line_y + 20}" text-anchor="middle" font-size="12" fill="#333">{i}</text>
'''
    
    # 圆
    circle_x = margin + 120 + start_pos * scale
    circle_y = line_y - radius * scale
    svg += f'''
  <!-- 圆 -->
  <circle cx="{circle_x}" cy="{circle_y}" r="{radius * scale}" fill="none" stroke="#3498db" stroke-width="2"/>
  <circle cx="{circle_x}" cy="{line_y}" r="5" fill="#e74c3c"/>
  <text x="{circle_x}" y="{line_y + 35}" text-anchor="middle" font-size="12" fill="#e74c3c">A</text>
'''
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def triangle_on_number_line(filename):
    """生成数轴上的等边三角形（翻转问题）"""
    width = 600
    height = 150
    margin = 50
    line_y = 120
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
  
  <!-- 数轴主线 -->
  <line x1="{margin - 20}" y1="{line_y}" x2="{width - margin + 20}" y2="{line_y}" 
        stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
'''
    
    scale = 50
    for i in range(-3, 6):
        x = margin + 100 + i * scale
        svg += f'''  <line x1="{x}" y1="{line_y - 5}" x2="{x}" y2="{line_y + 5}" stroke="#333" stroke-width="1.5"/>
  <text x="{x}" y="{line_y + 20}" text-anchor="middle" font-size="12" fill="#333">{i}</text>
'''
    
    # 等边三角形
    a_x = margin + 100  # A点在0
    c_x = margin + 100 - scale  # C点在-1
    b_x = (a_x + c_x) / 2  # B点在中间上方
    b_y = line_y - scale * 0.866  # 等边三角形高度
    
    svg += f'''
  <!-- 等边三角形 ABC -->
  <polygon points="{a_x},{line_y} {c_x},{line_y} {b_x},{b_y}" 
           fill="rgba(52, 152, 219, 0.2)" stroke="#3498db" stroke-width="2"/>
  
  <!-- 顶点标记 -->
  <circle cx="{a_x}" cy="{line_y}" r="5" fill="#e74c3c"/>
  <text x="{a_x}" y="{line_y - 10}" text-anchor="middle" font-size="14" font-weight="bold" fill="#e74c3c">A</text>
  
  <circle cx="{c_x}" cy="{line_y}" r="5" fill="#27ae60"/>
  <text x="{c_x}" y="{line_y - 10}" text-anchor="middle" font-size="14" font-weight="bold" fill="#27ae60">C</text>
  
  <circle cx="{b_x}" cy="{b_y}" r="5" fill="#9b59b6"/>
  <text x="{b_x}" y="{b_y - 10}" text-anchor="middle" font-size="14" font-weight="bold" fill="#9b59b6">B</text>
'''
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def number_line_ab_points(filename, a=-2, b=4):
    """生成带A、B两点的数轴"""
    width = 600
    height = 100
    margin = 50
    line_y = 50
    
    start = min(a, b) - 2
    end = max(a, b) + 2
    scale = (width - 2 * margin) / (end - start)
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
  
  <!-- 数轴主线 -->
  <line x1="{margin - 20}" y1="{line_y}" x2="{width - margin + 20}" y2="{line_y}" 
        stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
'''
    
    for i in range(int(start), int(end) + 1):
        x = margin + (i - start) * scale
        svg += f'''  <line x1="{x}" y1="{line_y - 5}" x2="{x}" y2="{line_y + 5}" stroke="#333" stroke-width="1.5"/>
  <text x="{x}" y="{line_y + 20}" text-anchor="middle" font-size="12" fill="#333">{i}</text>
'''
    
    # A点
    a_x = margin + (a - start) * scale
    svg += f'''
  <circle cx="{a_x}" cy="{line_y}" r="6" fill="#e74c3c"/>
  <text x="{a_x}" y="{line_y - 15}" text-anchor="middle" font-size="14" font-weight="bold" fill="#e74c3c">A</text>
'''
    
    # B点
    b_x = margin + (b - start) * scale
    svg += f'''
  <circle cx="{b_x}" cy="{line_y}" r="6" fill="#3498db"/>
  <text x="{b_x}" y="{line_y - 15}" text-anchor="middle" font-size="14" font-weight="bold" fill="#3498db">B</text>
'''
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def moving_points_diagram(filename):
    """生成动点问题的数轴图"""
    width = 600
    height = 120
    margin = 50
    line_y = 60
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
    <marker id="arrow-right" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#e74c3c"/>
    </marker>
  </defs>
  
  <!-- 数轴主线 -->
  <line x1="{margin - 20}" y1="{line_y}" x2="{width - margin + 20}" y2="{line_y}" 
        stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
'''
    
    scale = 25
    for i in range(-8, 11):
        x = margin + 50 + (i + 8) * scale
        if i % 2 == 0:
            svg += f'''  <line x1="{x}" y1="{line_y - 5}" x2="{x}" y2="{line_y + 5}" stroke="#333" stroke-width="1.5"/>
  <text x="{x}" y="{line_y + 20}" text-anchor="middle" font-size="10" fill="#333">{i}</text>
'''
        else:
            svg += f'''  <line x1="{x}" y1="{line_y - 3}" x2="{x}" y2="{line_y + 3}" stroke="#333" stroke-width="1"/>
'''
    
    # A点 (-8)
    a_x = margin + 50
    svg += f'''
  <circle cx="{a_x}" cy="{line_y}" r="6" fill="#e74c3c"/>
  <text x="{a_x}" y="{line_y - 15}" text-anchor="middle" font-size="12" font-weight="bold" fill="#e74c3c">A(-8)</text>
'''
    
    # B点 (10)
    b_x = margin + 50 + 18 * scale
    svg += f'''
  <circle cx="{b_x}" cy="{line_y}" r="6" fill="#3498db"/>
  <text x="{b_x}" y="{line_y - 15}" text-anchor="middle" font-size="12" font-weight="bold" fill="#3498db">B(10)</text>
'''
    
    # P点运动箭头
    p_x = margin + 50 + 4 * scale
    svg += f'''
  <circle cx="{p_x}" cy="{line_y}" r="5" fill="#27ae60"/>
  <text x="{p_x}" y="{line_y + 35}" text-anchor="middle" font-size="11" fill="#27ae60">P</text>
  <line x1="{p_x + 10}" y1="{line_y}" x2="{p_x + 40}" y2="{line_y}" stroke="#27ae60" stroke-width="2" stroke-dasharray="4" marker-end="url(#arrow-right)"/>
'''
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def circle_with_numbers(filename):
    """生成带数字的圆（滚动问题）"""
    width = 400
    height = 200
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <!-- 圆 -->
  <circle cx="200" cy="80" r="60" fill="none" stroke="#3498db" stroke-width="2"/>
  
  <!-- 四个数字 0,1,2,3 -->
  <text x="200" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#e74c3c">0</text>
  <text x="250" y="85" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">1</text>
  <text x="200" y="150" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">2</text>
  <text x="150" y="85" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">3</text>
  
  <!-- 圆心点 -->
  <circle cx="200" cy="80" r="3" fill="#333"/>
  
  <!-- 数轴 -->
  <line x1="50" y1="180" x2="350" y2="180" stroke="#333" stroke-width="2"/>
  <polygon points="350,180 340,175 340,185" fill="#333"/>
  
  <!-- 刻度 -->
  <line x1="100" y1="175" x2="100" y2="185" stroke="#333" stroke-width="1.5"/>
  <text x="100" y="198" text-anchor="middle" font-size="12">-1</text>
  
  <line x1="150" y1="175" x2="150" y2="185" stroke="#333" stroke-width="1.5"/>
  <text x="150" y="198" text-anchor="middle" font-size="12">0</text>
  
  <line x1="200" y1="175" x2="200" y2="185" stroke="#333" stroke-width="1.5"/>
  <text x="200" y="198" text-anchor="middle" font-size="12">1</text>
  
  <line x1="250" y1="175" x2="250" y2="185" stroke="#333" stroke-width="1.5"/>
  <text x="250" y="198" text-anchor="middle" font-size="12">2</text>
  
  <line x1="300" y1="175" x2="300" y2="185" stroke="#333" stroke-width="1.5"/>
  <text x="300" y="198" text-anchor="middle" font-size="12">3</text>
</svg>'''
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def abcd_number_line(filename):
    """生成带a,b,c,d四点的数轴"""
    width = 600
    height = 100
    margin = 50
    line_y = 50
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
  
  <!-- 数轴主线 -->
  <line x1="{margin - 20}" y1="{line_y}" x2="{width - margin + 20}" y2="{line_y}" 
        stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
  
  <!-- 原点 -->
  <line x1="300" y1="{line_y - 5}" x2="300" y2="{line_y + 5}" stroke="#333" stroke-width="2"/>
  <text x="300" y="{line_y + 20}" text-anchor="middle" font-size="12" fill="#333">0</text>
  
  <!-- a点 (负) -->
  <circle cx="120" cy="{line_y}" r="5" fill="#e74c3c"/>
  <text x="120" y="{line_y - 12}" text-anchor="middle" font-size="14" font-weight="bold" fill="#e74c3c">a</text>
  
  <!-- b点 (负，在a右边) -->
  <circle cx="200" cy="{line_y}" r="5" fill="#3498db"/>
  <text x="200" y="{line_y - 12}" text-anchor="middle" font-size="14" font-weight="bold" fill="#3498db">b</text>
  
  <!-- c点 (正) -->
  <circle cx="380" cy="{line_y}" r="5" fill="#27ae60"/>
  <text x="380" y="{line_y - 12}" text-anchor="middle" font-size="14" font-weight="bold" fill="#27ae60">c</text>
  
  <!-- d点 (正，在c右边) -->
  <circle cx="480" cy="{line_y}" r="5" fill="#9b59b6"/>
  <text x="480" y="{line_y - 12}" text-anchor="middle" font-size="14" font-weight="bold" fill="#9b59b6">d</text>
</svg>'''
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def generate_all():
    """生成所有SVG图形"""
    ensure_dir()
    
    # 基础数轴
    number_line_basic("number-line-basic.svg", 
                      points=[{'name': 'O', 'value': 0, 'color': '#333'}])
    
    # 带圆的数轴（t1-train-1）
    number_line_with_circle("number-line-circle.svg")
    
    # 三角形翻转（t2-example）
    triangle_on_number_line("triangle-flip.svg")
    
    # 带A、B两点的数轴（动点问题）
    number_line_ab_points("number-line-ab.svg", a=-8, b=10)
    
    # 动点问题
    moving_points_diagram("moving-points.svg")
    
    # 带数字的圆
    circle_with_numbers("circle-numbers.svg")
    
    # 带a,b,c,d四点的数轴
    abcd_number_line("number-line-abcd.svg")
    
    # 更多变体
    number_line_ab_points("number-line-ab-2.svg", a=-2, b=4)
    number_line_ab_points("number-line-ab-3.svg", a=-5, b=4)
    
    print("\n✅ All SVG files generated successfully!")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    generate_all()

"""
生成数学题目所需的SVG图形
"""

import os

SVG_DIR = "../packages/app/assets/svg"

def ensure_dir():
    os.makedirs(SVG_DIR, exist_ok=True)

# ========== 数轴类型 ==========

def number_line_basic(filename, points=None, start=-5, end=5, title=""):
    """生成基础数轴SVG"""
    width = 600
    height = 100
    margin = 50
    line_y = 50
    
    # 计算刻度
    scale = (width - 2 * margin) / (end - start)
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
  
  <!-- 数轴主线 -->
  <line x1="{margin - 20}" y1="{line_y}" x2="{width - margin + 20}" y2="{line_y}" 
        stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
  
  <!-- 刻度和数字 -->
'''
    
    for i in range(start, end + 1):
        x = margin + (i - start) * scale
        svg += f'''  <line x1="{x}" y1="{line_y - 5}" x2="{x}" y2="{line_y + 5}" stroke="#333" stroke-width="1.5"/>
  <text x="{x}" y="{line_y + 20}" text-anchor="middle" font-size="12" fill="#333">{i}</text>
'''
    
    # 添加点
    if points:
        for point in points:
            name, value, color = point.get('name', ''), point.get('value', 0), point.get('color', '#e74c3c')
            x = margin + (value - start) * scale
            svg += f'''  <circle cx="{x}" cy="{line_y}" r="6" fill="{color}"/>
  <text x="{x}" y="{line_y - 15}" text-anchor="middle" font-size="14" font-weight="bold" fill="{color}">{name}</text>
'''
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def number_line_with_circle(filename, radius=1, start_pos=-1):
    """生成带圆的数轴（圆滚动问题）"""
    width = 600
    height = 150
    margin = 50
    line_y = 100
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
  
  <!-- 数轴主线 -->
  <line x1="{margin - 20}" y1="{line_y}" x2="{width - margin + 20}" y2="{line_y}" 
        stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
  
  <!-- 刻度 -->
'''
    scale = 40
    for i in range(-3, 8):
        x = margin + 120 + i * scale
        svg += f'''  <line x1="{x}" y1="{line_y - 5}" x2="{x}" y2="{line_y + 5}" stroke="#333" stroke-width="1.5"/>
  <text x="{x}" y="{line_y + 20}" text-anchor="middle" font-size="12" fill="#333">{i}</text>
'''
    
    # 圆
    circle_x = margin + 120 + start_pos * scale
    circle_y = line_y - radius * scale
    svg += f'''
  <!-- 圆 -->
  <circle cx="{circle_x}" cy="{circle_y}" r="{radius * scale}" fill="none" stroke="#3498db" stroke-width="2"/>
  <circle cx="{circle_x}" cy="{line_y}" r="5" fill="#e74c3c"/>
  <text x="{circle_x}" y="{line_y + 35}" text-anchor="middle" font-size="12" fill="#e74c3c">A</text>
'''
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def triangle_on_number_line(filename):
    """生成数轴上的等边三角形（翻转问题）"""
    width = 600
    height = 150
    margin = 50
    line_y = 120
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
  
  <!-- 数轴主线 -->
  <line x1="{margin - 20}" y1="{line_y}" x2="{width - margin + 20}" y2="{line_y}" 
        stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
'''
    
    scale = 50
    for i in range(-3, 6):
        x = margin + 100 + i * scale
        svg += f'''  <line x1="{x}" y1="{line_y - 5}" x2="{x}" y2="{line_y + 5}" stroke="#333" stroke-width="1.5"/>
  <text x="{x}" y="{line_y + 20}" text-anchor="middle" font-size="12" fill="#333">{i}</text>
'''
    
    # 等边三角形
    a_x = margin + 100  # A点在0
    c_x = margin + 100 - scale  # C点在-1
    b_x = (a_x + c_x) / 2  # B点在中间上方
    b_y = line_y - scale * 0.866  # 等边三角形高度
    
    svg += f'''
  <!-- 等边三角形 ABC -->
  <polygon points="{a_x},{line_y} {c_x},{line_y} {b_x},{b_y}" 
           fill="rgba(52, 152, 219, 0.2)" stroke="#3498db" stroke-width="2"/>
  
  <!-- 顶点标记 -->
  <circle cx="{a_x}" cy="{line_y}" r="5" fill="#e74c3c"/>
  <text x="{a_x}" y="{line_y - 10}" text-anchor="middle" font-size="14" font-weight="bold" fill="#e74c3c">A</text>
  
  <circle cx="{c_x}" cy="{line_y}" r="5" fill="#27ae60"/>
  <text x="{c_x}" y="{line_y - 10}" text-anchor="middle" font-size="14" font-weight="bold" fill="#27ae60">C</text>
  
  <circle cx="{b_x}" cy="{b_y}" r="5" fill="#9b59b6"/>
  <text x="{b_x}" y="{b_y - 10}" text-anchor="middle" font-size="14" font-weight="bold" fill="#9b59b6">B</text>
'''
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def number_line_ab_points(filename, a=-2, b=4):
    """生成带A、B两点的数轴"""
    width = 600
    height = 100
    margin = 50
    line_y = 50
    
    start = min(a, b) - 2
    end = max(a, b) + 2
    scale = (width - 2 * margin) / (end - start)
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
  
  <!-- 数轴主线 -->
  <line x1="{margin - 20}" y1="{line_y}" x2="{width - margin + 20}" y2="{line_y}" 
        stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
'''
    
    for i in range(int(start), int(end) + 1):
        x = margin + (i - start) * scale
        svg += f'''  <line x1="{x}" y1="{line_y - 5}" x2="{x}" y2="{line_y + 5}" stroke="#333" stroke-width="1.5"/>
  <text x="{x}" y="{line_y + 20}" text-anchor="middle" font-size="12" fill="#333">{i}</text>
'''
    
    # A点
    a_x = margin + (a - start) * scale
    svg += f'''
  <circle cx="{a_x}" cy="{line_y}" r="6" fill="#e74c3c"/>
  <text x="{a_x}" y="{line_y - 15}" text-anchor="middle" font-size="14" font-weight="bold" fill="#e74c3c">A</text>
'''
    
    # B点
    b_x = margin + (b - start) * scale
    svg += f'''
  <circle cx="{b_x}" cy="{line_y}" r="6" fill="#3498db"/>
  <text x="{b_x}" y="{line_y - 15}" text-anchor="middle" font-size="14" font-weight="bold" fill="#3498db">B</text>
'''
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def moving_points_diagram(filename):
    """生成动点问题的数轴图"""
    width = 600
    height = 120
    margin = 50
    line_y = 60
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
    <marker id="arrow-right" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#e74c3c"/>
    </marker>
  </defs>
  
  <!-- 数轴主线 -->
  <line x1="{margin - 20}" y1="{line_y}" x2="{width - margin + 20}" y2="{line_y}" 
        stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
'''
    
    scale = 25
    for i in range(-8, 11):
        x = margin + 50 + (i + 8) * scale
        if i % 2 == 0:
            svg += f'''  <line x1="{x}" y1="{line_y - 5}" x2="{x}" y2="{line_y + 5}" stroke="#333" stroke-width="1.5"/>
  <text x="{x}" y="{line_y + 20}" text-anchor="middle" font-size="10" fill="#333">{i}</text>
'''
        else:
            svg += f'''  <line x1="{x}" y1="{line_y - 3}" x2="{x}" y2="{line_y + 3}" stroke="#333" stroke-width="1"/>
'''
    
    # A点 (-8)
    a_x = margin + 50
    svg += f'''
  <circle cx="{a_x}" cy="{line_y}" r="6" fill="#e74c3c"/>
  <text x="{a_x}" y="{line_y - 15}" text-anchor="middle" font-size="12" font-weight="bold" fill="#e74c3c">A(-8)</text>
'''
    
    # B点 (10)
    b_x = margin + 50 + 18 * scale
    svg += f'''
  <circle cx="{b_x}" cy="{line_y}" r="6" fill="#3498db"/>
  <text x="{b_x}" y="{line_y - 15}" text-anchor="middle" font-size="12" font-weight="bold" fill="#3498db">B(10)</text>
'''
    
    # P点运动箭头
    p_x = margin + 50 + 4 * scale
    svg += f'''
  <circle cx="{p_x}" cy="{line_y}" r="5" fill="#27ae60"/>
  <text x="{p_x}" y="{line_y + 35}" text-anchor="middle" font-size="11" fill="#27ae60">P</text>
  <line x1="{p_x + 10}" y1="{line_y}" x2="{p_x + 40}" y2="{line_y}" stroke="#27ae60" stroke-width="2" stroke-dasharray="4" marker-end="url(#arrow-right)"/>
'''
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def circle_with_numbers(filename):
    """生成带数字的圆（滚动问题）"""
    width = 400
    height = 200
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <!-- 圆 -->
  <circle cx="200" cy="80" r="60" fill="none" stroke="#3498db" stroke-width="2"/>
  
  <!-- 四个数字 0,1,2,3 -->
  <text x="200" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#e74c3c">0</text>
  <text x="250" y="85" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">1</text>
  <text x="200" y="150" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">2</text>
  <text x="150" y="85" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">3</text>
  
  <!-- 圆心点 -->
  <circle cx="200" cy="80" r="3" fill="#333"/>
  
  <!-- 数轴 -->
  <line x1="50" y1="180" x2="350" y2="180" stroke="#333" stroke-width="2"/>
  <polygon points="350,180 340,175 340,185" fill="#333"/>
  
  <!-- 刻度 -->
  <line x1="100" y1="175" x2="100" y2="185" stroke="#333" stroke-width="1.5"/>
  <text x="100" y="198" text-anchor="middle" font-size="12">-1</text>
  
  <line x1="150" y1="175" x2="150" y2="185" stroke="#333" stroke-width="1.5"/>
  <text x="150" y="198" text-anchor="middle" font-size="12">0</text>
  
  <line x1="200" y1="175" x2="200" y2="185" stroke="#333" stroke-width="1.5"/>
  <text x="200" y="198" text-anchor="middle" font-size="12">1</text>
  
  <line x1="250" y1="175" x2="250" y2="185" stroke="#333" stroke-width="1.5"/>
  <text x="250" y="198" text-anchor="middle" font-size="12">2</text>
  
  <line x1="300" y1="175" x2="300" y2="185" stroke="#333" stroke-width="1.5"/>
  <text x="300" y="198" text-anchor="middle" font-size="12">3</text>
</svg>'''
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def abcd_number_line(filename):
    """生成带a,b,c,d四点的数轴"""
    width = 600
    height = 100
    margin = 50
    line_y = 50
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
  
  <!-- 数轴主线 -->
  <line x1="{margin - 20}" y1="{line_y}" x2="{width - margin + 20}" y2="{line_y}" 
        stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
  
  <!-- 原点 -->
  <line x1="300" y1="{line_y - 5}" x2="300" y2="{line_y + 5}" stroke="#333" stroke-width="2"/>
  <text x="300" y="{line_y + 20}" text-anchor="middle" font-size="12" fill="#333">0</text>
  
  <!-- a点 (负) -->
  <circle cx="120" cy="{line_y}" r="5" fill="#e74c3c"/>
  <text x="120" y="{line_y - 12}" text-anchor="middle" font-size="14" font-weight="bold" fill="#e74c3c">a</text>
  
  <!-- b点 (负，在a右边) -->
  <circle cx="200" cy="{line_y}" r="5" fill="#3498db"/>
  <text x="200" y="{line_y - 12}" text-anchor="middle" font-size="14" font-weight="bold" fill="#3498db">b</text>
  
  <!-- c点 (正) -->
  <circle cx="380" cy="{line_y}" r="5" fill="#27ae60"/>
  <text x="380" y="{line_y - 12}" text-anchor="middle" font-size="14" font-weight="bold" fill="#27ae60">c</text>
  
  <!-- d点 (正，在c右边) -->
  <circle cx="480" cy="{line_y}" r="5" fill="#9b59b6"/>
  <text x="480" y="{line_y - 12}" text-anchor="middle" font-size="14" font-weight="bold" fill="#9b59b6">d</text>
</svg>'''
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def generate_all():
    """生成所有SVG图形"""
    ensure_dir()
    
    # 基础数轴
    number_line_basic("number-line-basic.svg", 
                      points=[{'name': 'O', 'value': 0, 'color': '#333'}])
    
    # 带圆的数轴（t1-train-1）
    number_line_with_circle("number-line-circle.svg")
    
    # 三角形翻转（t2-example）
    triangle_on_number_line("triangle-flip.svg")
    
    # 带A、B两点的数轴（动点问题）
    number_line_ab_points("number-line-ab.svg", a=-8, b=10)
    
    # 动点问题
    moving_points_diagram("moving-points.svg")
    
    # 带数字的圆
    circle_with_numbers("circle-numbers.svg")
    
    # 带a,b,c,d四点的数轴
    abcd_number_line("number-line-abcd.svg")
    
    # 更多变体
    number_line_ab_points("number-line-ab-2.svg", a=-2, b=4)
    number_line_ab_points("number-line-ab-3.svg", a=-5, b=4)
    
    print("\n✅ All SVG files generated successfully!")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    generate_all()


