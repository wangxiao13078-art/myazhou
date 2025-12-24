#!/usr/bin/env python3
"""
生成更多数学题目所需的SVG图形
"""

import os

SVG_DIR = "../packages/app/assets/svg"

def ensure_dir():
    os.makedirs(SVG_DIR, exist_ok=True)

# ========== 几何图形 ==========

def area_square_diagram(filename):
    """生成代数面积图 (a+b)² = a² + 2ab + b²"""
    width = 300
    height = 300
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <!-- 外框 -->
  <rect x="50" y="50" width="200" height="200" fill="none" stroke="#333" stroke-width="2"/>
  
  <!-- a² 区域 -->
  <rect x="50" y="50" width="130" height="130" fill="#e74c3c" fill-opacity="0.3" stroke="#e74c3c" stroke-width="1"/>
  <text x="115" y="120" text-anchor="middle" font-size="20" font-weight="bold" fill="#c0392b">a²</text>
  
  <!-- b² 区域 -->
  <rect x="180" y="180" width="70" height="70" fill="#3498db" fill-opacity="0.3" stroke="#3498db" stroke-width="1"/>
  <text x="215" y="220" text-anchor="middle" font-size="16" font-weight="bold" fill="#2980b9">b²</text>
  
  <!-- ab 区域 (上) -->
  <rect x="180" y="50" width="70" height="130" fill="#27ae60" fill-opacity="0.3" stroke="#27ae60" stroke-width="1"/>
  <text x="215" y="120" text-anchor="middle" font-size="14" font-weight="bold" fill="#1e8449">ab</text>
  
  <!-- ab 区域 (左) -->
  <rect x="50" y="180" width="130" height="70" fill="#27ae60" fill-opacity="0.3" stroke="#27ae60" stroke-width="1"/>
  <text x="115" y="220" text-anchor="middle" font-size="14" font-weight="bold" fill="#1e8449">ab</text>
  
  <!-- 标注 a -->
  <text x="115" y="40" text-anchor="middle" font-size="16" fill="#333">a</text>
  <line x1="50" y1="45" x2="180" y2="45" stroke="#333" stroke-width="1"/>
  
  <!-- 标注 b -->
  <text x="215" y="40" text-anchor="middle" font-size="16" fill="#333">b</text>
  <line x1="180" y1="45" x2="250" y2="45" stroke="#333" stroke-width="1"/>
  
  <!-- 右侧标注 -->
  <text x="265" y="120" text-anchor="middle" font-size="16" fill="#333">a</text>
  <text x="265" y="220" text-anchor="middle" font-size="16" fill="#333">b</text>
</svg>'''
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def chess_pattern(filename, rows=3, cols=3):
    """生成围棋棋子图案"""
    width = 200
    height = 200
    cell_size = 40
    margin = 40
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
'''
    
    # 绘制网格线
    for i in range(rows + 1):
        y = margin + i * cell_size
        svg += f'  <line x1="{margin}" y1="{y}" x2="{margin + cols * cell_size}" y2="{y}" stroke="#333" stroke-width="1"/>\n'
    
    for j in range(cols + 1):
        x = margin + j * cell_size
        svg += f'  <line x1="{x}" y1="{margin}" x2="{x}" y2="{margin + rows * cell_size}" stroke="#333" stroke-width="1"/>\n'
    
    # 绘制棋子（示例模式）
    black_positions = [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)]
    white_positions = [(0, 1), (1, 0), (1, 2), (2, 1)]
    
    for (r, c) in black_positions:
        x = margin + c * cell_size
        y = margin + r * cell_size
        svg += f'  <circle cx="{x}" cy="{y}" r="15" fill="#333" stroke="#333"/>\n'
    
    for (r, c) in white_positions:
        x = margin + c * cell_size
        y = margin + r * cell_size
        svg += f'  <circle cx="{x}" cy="{y}" r="15" fill="#fff" stroke="#333" stroke-width="2"/>\n'
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def matchstick_pattern(filename, n=3):
    """生成火柴棒图案"""
    width = 400
    height = 150
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
'''
    
    stick_len = 40
    margin = 30
    
    for i in range(n):
        x = margin + i * stick_len
        # 竖线
        svg += f'  <line x1="{x}" y1="30" x2="{x}" y2="{30 + stick_len}" stroke="#8B4513" stroke-width="4" stroke-linecap="round"/>\n'
        # 横线（上）
        svg += f'  <line x1="{x}" y1="30" x2="{x + stick_len}" y2="30" stroke="#8B4513" stroke-width="4" stroke-linecap="round"/>\n'
        # 横线（下）
        svg += f'  <line x1="{x}" y1="{30 + stick_len}" x2="{x + stick_len}" y2="{30 + stick_len}" stroke="#8B4513" stroke-width="4" stroke-linecap="round"/>\n'
    
    # 最后一根竖线
    x = margin + n * stick_len
    svg += f'  <line x1="{x}" y1="30" x2="{x}" y2="{30 + stick_len}" stroke="#8B4513" stroke-width="4" stroke-linecap="round"/>\n'
    
    # 标注
    svg += f'  <text x="{margin + (n * stick_len) / 2}" y="100" text-anchor="middle" font-size="14" fill="#333">图{n}</text>\n'
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def polygon_expansion(filename, sides=5):
    """生成正n边形扩展图"""
    import math
    
    width = 300
    height = 300
    cx, cy = 150, 150
    r = 60
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
'''
    
    # 计算顶点
    points = []
    for i in range(sides):
        angle = -math.pi / 2 + i * 2 * math.pi / sides
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        points.append((x, y))
    
    # 绘制中心正n边形
    pts_str = " ".join([f"{x},{y}" for x, y in points])
    svg += f'  <polygon points="{pts_str}" fill="#3498db" fill-opacity="0.3" stroke="#3498db" stroke-width="2"/>\n'
    
    # 绘制扩展的正n边形
    for i in range(sides):
        p1 = points[i]
        p2 = points[(i + 1) % sides]
        
        # 计算外扩顶点
        mid_x = (p1[0] + p2[0]) / 2
        mid_y = (p1[1] + p2[1]) / 2
        dx = mid_x - cx
        dy = mid_y - cy
        length = math.sqrt(dx * dx + dy * dy)
        
        # 外扩点
        outer_x = mid_x + dx / length * r * 0.8
        outer_y = mid_y + dy / length * r * 0.8
        
        # 绘制小三角形
        svg += f'  <polygon points="{p1[0]},{p1[1]} {p2[0]},{p2[1]} {outer_x},{outer_y}" fill="#e74c3c" fill-opacity="0.3" stroke="#e74c3c" stroke-width="1.5"/>\n'
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def house_floor_plan(filename):
    """生成房屋平面图"""
    width = 400
    height = 300
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <!-- 外框 -->
  <rect x="50" y="50" width="300" height="200" fill="none" stroke="#333" stroke-width="2"/>
  
  <!-- 主卧 -->
  <rect x="50" y="50" width="120" height="120" fill="#e74c3c" fill-opacity="0.2" stroke="#333" stroke-width="1"/>
  <text x="110" y="115" text-anchor="middle" font-size="14" fill="#333">主卧</text>
  <text x="110" y="135" text-anchor="middle" font-size="12" fill="#666">a×b</text>
  
  <!-- 次卧 -->
  <rect x="170" y="50" width="100" height="80" fill="#3498db" fill-opacity="0.2" stroke="#333" stroke-width="1"/>
  <text x="220" y="95" text-anchor="middle" font-size="14" fill="#333">次卧</text>
  
  <!-- 客厅 -->
  <rect x="170" y="130" width="180" height="120" fill="#27ae60" fill-opacity="0.2" stroke="#333" stroke-width="1"/>
  <text x="260" y="195" text-anchor="middle" font-size="14" fill="#333">客厅</text>
  
  <!-- 厨房 -->
  <rect x="270" y="50" width="80" height="80" fill="#f39c12" fill-opacity="0.2" stroke="#333" stroke-width="1"/>
  <text x="310" y="95" text-anchor="middle" font-size="14" fill="#333">厨房</text>
  
  <!-- 标注 -->
  <text x="110" y="40" text-anchor="middle" font-size="12" fill="#333">a m</text>
  <text x="35" y="115" text-anchor="middle" font-size="12" fill="#333" transform="rotate(-90 35 115)">b m</text>
</svg>'''
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def cube_diagram(filename):
    """生成正方体图"""
    width = 200
    height = 200
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <!-- 后面 -->
  <polygon points="70,40 150,40 150,120 70,120" fill="#3498db" fill-opacity="0.2" stroke="#333" stroke-width="1.5"/>
  
  <!-- 顶面 -->
  <polygon points="50,60 70,40 150,40 130,60" fill="#27ae60" fill-opacity="0.3" stroke="#333" stroke-width="1.5"/>
  
  <!-- 前面 -->
  <polygon points="50,60 130,60 130,140 50,140" fill="#e74c3c" fill-opacity="0.2" stroke="#333" stroke-width="2"/>
  
  <!-- 右面 -->
  <polygon points="130,60 150,40 150,120 130,140" fill="#f39c12" fill-opacity="0.3" stroke="#333" stroke-width="1.5"/>
  
  <!-- 标注 -->
  <text x="90" y="170" text-anchor="middle" font-size="14" fill="#333">a</text>
  <line x1="50" y1="155" x2="130" y2="155" stroke="#333" stroke-width="1"/>
</svg>'''
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def two_circles_on_line(filename):
    """生成两个圆在数轴上滚动的图"""
    width = 500
    height = 200
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
  
  <!-- 数轴 -->
  <line x1="30" y1="150" x2="470" y2="150" stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
'''
    
    # 刻度
    for i in range(-5, 8):
        x = 100 + i * 30
        svg += f'  <line x1="{x}" y1="145" x2="{x}" y2="155" stroke="#333" stroke-width="1.5"/>\n'
        svg += f'  <text x="{x}" y="170" text-anchor="middle" font-size="11" fill="#333">{i}</text>\n'
    
    # 小圆（半径1）
    svg += '''
  <circle cx="100" cy="120" r="30" fill="none" stroke="#e74c3c" stroke-width="2"/>
  <text x="100" y="125" text-anchor="middle" font-size="12" fill="#e74c3c">r=1</text>
  <circle cx="100" cy="150" r="4" fill="#e74c3c"/>
'''
    
    # 大圆（半径2）
    svg += '''
  <circle cx="220" cy="90" r="60" fill="none" stroke="#3498db" stroke-width="2"/>
  <text x="220" y="95" text-anchor="middle" font-size="12" fill="#3498db">r=2</text>
  <circle cx="220" cy="150" r="4" fill="#3498db"/>
'''
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def folding_number_line(filename):
    """生成数轴折叠图"""
    width = 500
    height = 120
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
  
  <!-- 数轴 -->
  <line x1="30" y1="60" x2="470" y2="60" stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
'''
    
    # 刻度
    for i in range(-5, 6):
        x = 150 + i * 30
        svg += f'  <line x1="{x}" y1="55" x2="{x}" y2="65" stroke="#333" stroke-width="1.5"/>\n'
        svg += f'  <text x="{x}" y="80" text-anchor="middle" font-size="12" fill="#333">{i}</text>\n'
    
    # A点和B点
    a_x = 150 - 3 * 30  # -3
    b_x = 150 + 5 * 30  # 5
    
    svg += f'''
  <circle cx="{a_x}" cy="60" r="5" fill="#e74c3c"/>
  <text x="{a_x}" y="45" text-anchor="middle" font-size="14" font-weight="bold" fill="#e74c3c">A</text>
  
  <circle cx="{b_x}" cy="60" r="5" fill="#3498db"/>
  <text x="{b_x}" y="45" text-anchor="middle" font-size="14" font-weight="bold" fill="#3498db">B</text>
  
  <!-- 折叠标记 -->
  <path d="M {(a_x + b_x) / 2} 40 Q {(a_x + b_x) / 2 - 30} 20 {a_x} 40" stroke="#27ae60" stroke-width="1.5" fill="none" stroke-dasharray="4"/>
  <path d="M {(a_x + b_x) / 2} 40 Q {(a_x + b_x) / 2 + 30} 20 {b_x} 40" stroke="#27ae60" stroke-width="1.5" fill="none" stroke-dasharray="4"/>
  <text x="{(a_x + b_x) / 2}" y="25" text-anchor="middle" font-size="12" fill="#27ae60">折叠</text>
'''
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def jumping_point(filename):
    """生成跳跃点图"""
    width = 500
    height = 150
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
  
  <!-- 数轴 -->
  <line x1="30" y1="100" x2="470" y2="100" stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
  
  <!-- 原点O -->
  <line x1="100" y1="95" x2="100" y2="105" stroke="#333" stroke-width="2"/>
  <text x="100" y="120" text-anchor="middle" font-size="12" fill="#333">O</text>
  <text x="100" y="135" text-anchor="middle" font-size="10" fill="#666">0</text>
  
  <!-- 起始点 (8个单位) -->
  <line x1="340" y1="95" x2="340" y2="105" stroke="#333" stroke-width="2"/>
  <text x="340" y="120" text-anchor="middle" font-size="12" fill="#333">8</text>
  <circle cx="340" cy="100" r="5" fill="#e74c3c"/>
  <text x="340" y="85" text-anchor="middle" font-size="12" fill="#e74c3c">P</text>
  
  <!-- 跳跃路径 -->
  <path d="M 340 90 Q 280 50 220 90" stroke="#3498db" stroke-width="1.5" fill="none" stroke-dasharray="4"/>
  <text x="280" y="55" text-anchor="middle" font-size="10" fill="#3498db">M₁</text>
  
  <path d="M 220 90 Q 180 60 160 90" stroke="#27ae60" stroke-width="1.5" fill="none" stroke-dasharray="4"/>
  <text x="190" y="65" text-anchor="middle" font-size="10" fill="#27ae60">M₂</text>
  
  <!-- 中间点 -->
  <circle cx="220" cy="100" r="4" fill="#3498db"/>
  <circle cx="160" cy="100" r="4" fill="#27ae60"/>
'''
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def generate_all():
    """生成所有SVG图形"""
    ensure_dir()
    
    # 代数面积图
    area_square_diagram("area-square.svg")
    
    # 围棋棋子图案
    chess_pattern("chess-pattern.svg")
    
    # 火柴棒图案
    for i in range(1, 5):
        matchstick_pattern(f"matchstick-{i}.svg", i)
    
    # 正多边形扩展
    for sides in [3, 4, 5, 6]:
        polygon_expansion(f"polygon-{sides}.svg", sides)
    
    # 房屋平面图
    house_floor_plan("house-plan.svg")
    
    # 正方体
    cube_diagram("cube.svg")
    
    # 双圆滚动
    two_circles_on_line("two-circles.svg")
    
    # 数轴折叠
    folding_number_line("folding-line.svg")
    
    # 跳跃点
    jumping_point("jumping-point.svg")
    
    print("\n✅ All additional SVG files generated successfully!")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    generate_all()

"""
生成更多数学题目所需的SVG图形
"""

import os

SVG_DIR = "../packages/app/assets/svg"

def ensure_dir():
    os.makedirs(SVG_DIR, exist_ok=True)

# ========== 几何图形 ==========

def area_square_diagram(filename):
    """生成代数面积图 (a+b)² = a² + 2ab + b²"""
    width = 300
    height = 300
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <!-- 外框 -->
  <rect x="50" y="50" width="200" height="200" fill="none" stroke="#333" stroke-width="2"/>
  
  <!-- a² 区域 -->
  <rect x="50" y="50" width="130" height="130" fill="#e74c3c" fill-opacity="0.3" stroke="#e74c3c" stroke-width="1"/>
  <text x="115" y="120" text-anchor="middle" font-size="20" font-weight="bold" fill="#c0392b">a²</text>
  
  <!-- b² 区域 -->
  <rect x="180" y="180" width="70" height="70" fill="#3498db" fill-opacity="0.3" stroke="#3498db" stroke-width="1"/>
  <text x="215" y="220" text-anchor="middle" font-size="16" font-weight="bold" fill="#2980b9">b²</text>
  
  <!-- ab 区域 (上) -->
  <rect x="180" y="50" width="70" height="130" fill="#27ae60" fill-opacity="0.3" stroke="#27ae60" stroke-width="1"/>
  <text x="215" y="120" text-anchor="middle" font-size="14" font-weight="bold" fill="#1e8449">ab</text>
  
  <!-- ab 区域 (左) -->
  <rect x="50" y="180" width="130" height="70" fill="#27ae60" fill-opacity="0.3" stroke="#27ae60" stroke-width="1"/>
  <text x="115" y="220" text-anchor="middle" font-size="14" font-weight="bold" fill="#1e8449">ab</text>
  
  <!-- 标注 a -->
  <text x="115" y="40" text-anchor="middle" font-size="16" fill="#333">a</text>
  <line x1="50" y1="45" x2="180" y2="45" stroke="#333" stroke-width="1"/>
  
  <!-- 标注 b -->
  <text x="215" y="40" text-anchor="middle" font-size="16" fill="#333">b</text>
  <line x1="180" y1="45" x2="250" y2="45" stroke="#333" stroke-width="1"/>
  
  <!-- 右侧标注 -->
  <text x="265" y="120" text-anchor="middle" font-size="16" fill="#333">a</text>
  <text x="265" y="220" text-anchor="middle" font-size="16" fill="#333">b</text>
</svg>'''
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def chess_pattern(filename, rows=3, cols=3):
    """生成围棋棋子图案"""
    width = 200
    height = 200
    cell_size = 40
    margin = 40
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
'''
    
    # 绘制网格线
    for i in range(rows + 1):
        y = margin + i * cell_size
        svg += f'  <line x1="{margin}" y1="{y}" x2="{margin + cols * cell_size}" y2="{y}" stroke="#333" stroke-width="1"/>\n'
    
    for j in range(cols + 1):
        x = margin + j * cell_size
        svg += f'  <line x1="{x}" y1="{margin}" x2="{x}" y2="{margin + rows * cell_size}" stroke="#333" stroke-width="1"/>\n'
    
    # 绘制棋子（示例模式）
    black_positions = [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)]
    white_positions = [(0, 1), (1, 0), (1, 2), (2, 1)]
    
    for (r, c) in black_positions:
        x = margin + c * cell_size
        y = margin + r * cell_size
        svg += f'  <circle cx="{x}" cy="{y}" r="15" fill="#333" stroke="#333"/>\n'
    
    for (r, c) in white_positions:
        x = margin + c * cell_size
        y = margin + r * cell_size
        svg += f'  <circle cx="{x}" cy="{y}" r="15" fill="#fff" stroke="#333" stroke-width="2"/>\n'
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def matchstick_pattern(filename, n=3):
    """生成火柴棒图案"""
    width = 400
    height = 150
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
'''
    
    stick_len = 40
    margin = 30
    
    for i in range(n):
        x = margin + i * stick_len
        # 竖线
        svg += f'  <line x1="{x}" y1="30" x2="{x}" y2="{30 + stick_len}" stroke="#8B4513" stroke-width="4" stroke-linecap="round"/>\n'
        # 横线（上）
        svg += f'  <line x1="{x}" y1="30" x2="{x + stick_len}" y2="30" stroke="#8B4513" stroke-width="4" stroke-linecap="round"/>\n'
        # 横线（下）
        svg += f'  <line x1="{x}" y1="{30 + stick_len}" x2="{x + stick_len}" y2="{30 + stick_len}" stroke="#8B4513" stroke-width="4" stroke-linecap="round"/>\n'
    
    # 最后一根竖线
    x = margin + n * stick_len
    svg += f'  <line x1="{x}" y1="30" x2="{x}" y2="{30 + stick_len}" stroke="#8B4513" stroke-width="4" stroke-linecap="round"/>\n'
    
    # 标注
    svg += f'  <text x="{margin + (n * stick_len) / 2}" y="100" text-anchor="middle" font-size="14" fill="#333">图{n}</text>\n'
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def polygon_expansion(filename, sides=5):
    """生成正n边形扩展图"""
    import math
    
    width = 300
    height = 300
    cx, cy = 150, 150
    r = 60
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
'''
    
    # 计算顶点
    points = []
    for i in range(sides):
        angle = -math.pi / 2 + i * 2 * math.pi / sides
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        points.append((x, y))
    
    # 绘制中心正n边形
    pts_str = " ".join([f"{x},{y}" for x, y in points])
    svg += f'  <polygon points="{pts_str}" fill="#3498db" fill-opacity="0.3" stroke="#3498db" stroke-width="2"/>\n'
    
    # 绘制扩展的正n边形
    for i in range(sides):
        p1 = points[i]
        p2 = points[(i + 1) % sides]
        
        # 计算外扩顶点
        mid_x = (p1[0] + p2[0]) / 2
        mid_y = (p1[1] + p2[1]) / 2
        dx = mid_x - cx
        dy = mid_y - cy
        length = math.sqrt(dx * dx + dy * dy)
        
        # 外扩点
        outer_x = mid_x + dx / length * r * 0.8
        outer_y = mid_y + dy / length * r * 0.8
        
        # 绘制小三角形
        svg += f'  <polygon points="{p1[0]},{p1[1]} {p2[0]},{p2[1]} {outer_x},{outer_y}" fill="#e74c3c" fill-opacity="0.3" stroke="#e74c3c" stroke-width="1.5"/>\n'
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def house_floor_plan(filename):
    """生成房屋平面图"""
    width = 400
    height = 300
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <!-- 外框 -->
  <rect x="50" y="50" width="300" height="200" fill="none" stroke="#333" stroke-width="2"/>
  
  <!-- 主卧 -->
  <rect x="50" y="50" width="120" height="120" fill="#e74c3c" fill-opacity="0.2" stroke="#333" stroke-width="1"/>
  <text x="110" y="115" text-anchor="middle" font-size="14" fill="#333">主卧</text>
  <text x="110" y="135" text-anchor="middle" font-size="12" fill="#666">a×b</text>
  
  <!-- 次卧 -->
  <rect x="170" y="50" width="100" height="80" fill="#3498db" fill-opacity="0.2" stroke="#333" stroke-width="1"/>
  <text x="220" y="95" text-anchor="middle" font-size="14" fill="#333">次卧</text>
  
  <!-- 客厅 -->
  <rect x="170" y="130" width="180" height="120" fill="#27ae60" fill-opacity="0.2" stroke="#333" stroke-width="1"/>
  <text x="260" y="195" text-anchor="middle" font-size="14" fill="#333">客厅</text>
  
  <!-- 厨房 -->
  <rect x="270" y="50" width="80" height="80" fill="#f39c12" fill-opacity="0.2" stroke="#333" stroke-width="1"/>
  <text x="310" y="95" text-anchor="middle" font-size="14" fill="#333">厨房</text>
  
  <!-- 标注 -->
  <text x="110" y="40" text-anchor="middle" font-size="12" fill="#333">a m</text>
  <text x="35" y="115" text-anchor="middle" font-size="12" fill="#333" transform="rotate(-90 35 115)">b m</text>
</svg>'''
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def cube_diagram(filename):
    """生成正方体图"""
    width = 200
    height = 200
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <!-- 后面 -->
  <polygon points="70,40 150,40 150,120 70,120" fill="#3498db" fill-opacity="0.2" stroke="#333" stroke-width="1.5"/>
  
  <!-- 顶面 -->
  <polygon points="50,60 70,40 150,40 130,60" fill="#27ae60" fill-opacity="0.3" stroke="#333" stroke-width="1.5"/>
  
  <!-- 前面 -->
  <polygon points="50,60 130,60 130,140 50,140" fill="#e74c3c" fill-opacity="0.2" stroke="#333" stroke-width="2"/>
  
  <!-- 右面 -->
  <polygon points="130,60 150,40 150,120 130,140" fill="#f39c12" fill-opacity="0.3" stroke="#333" stroke-width="1.5"/>
  
  <!-- 标注 -->
  <text x="90" y="170" text-anchor="middle" font-size="14" fill="#333">a</text>
  <line x1="50" y1="155" x2="130" y2="155" stroke="#333" stroke-width="1"/>
</svg>'''
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def two_circles_on_line(filename):
    """生成两个圆在数轴上滚动的图"""
    width = 500
    height = 200
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
  
  <!-- 数轴 -->
  <line x1="30" y1="150" x2="470" y2="150" stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
'''
    
    # 刻度
    for i in range(-5, 8):
        x = 100 + i * 30
        svg += f'  <line x1="{x}" y1="145" x2="{x}" y2="155" stroke="#333" stroke-width="1.5"/>\n'
        svg += f'  <text x="{x}" y="170" text-anchor="middle" font-size="11" fill="#333">{i}</text>\n'
    
    # 小圆（半径1）
    svg += '''
  <circle cx="100" cy="120" r="30" fill="none" stroke="#e74c3c" stroke-width="2"/>
  <text x="100" y="125" text-anchor="middle" font-size="12" fill="#e74c3c">r=1</text>
  <circle cx="100" cy="150" r="4" fill="#e74c3c"/>
'''
    
    # 大圆（半径2）
    svg += '''
  <circle cx="220" cy="90" r="60" fill="none" stroke="#3498db" stroke-width="2"/>
  <text x="220" y="95" text-anchor="middle" font-size="12" fill="#3498db">r=2</text>
  <circle cx="220" cy="150" r="4" fill="#3498db"/>
'''
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def folding_number_line(filename):
    """生成数轴折叠图"""
    width = 500
    height = 120
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
  
  <!-- 数轴 -->
  <line x1="30" y1="60" x2="470" y2="60" stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
'''
    
    # 刻度
    for i in range(-5, 6):
        x = 150 + i * 30
        svg += f'  <line x1="{x}" y1="55" x2="{x}" y2="65" stroke="#333" stroke-width="1.5"/>\n'
        svg += f'  <text x="{x}" y="80" text-anchor="middle" font-size="12" fill="#333">{i}</text>\n'
    
    # A点和B点
    a_x = 150 - 3 * 30  # -3
    b_x = 150 + 5 * 30  # 5
    
    svg += f'''
  <circle cx="{a_x}" cy="60" r="5" fill="#e74c3c"/>
  <text x="{a_x}" y="45" text-anchor="middle" font-size="14" font-weight="bold" fill="#e74c3c">A</text>
  
  <circle cx="{b_x}" cy="60" r="5" fill="#3498db"/>
  <text x="{b_x}" y="45" text-anchor="middle" font-size="14" font-weight="bold" fill="#3498db">B</text>
  
  <!-- 折叠标记 -->
  <path d="M {(a_x + b_x) / 2} 40 Q {(a_x + b_x) / 2 - 30} 20 {a_x} 40" stroke="#27ae60" stroke-width="1.5" fill="none" stroke-dasharray="4"/>
  <path d="M {(a_x + b_x) / 2} 40 Q {(a_x + b_x) / 2 + 30} 20 {b_x} 40" stroke="#27ae60" stroke-width="1.5" fill="none" stroke-dasharray="4"/>
  <text x="{(a_x + b_x) / 2}" y="25" text-anchor="middle" font-size="12" fill="#27ae60">折叠</text>
'''
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def jumping_point(filename):
    """生成跳跃点图"""
    width = 500
    height = 150
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
  
  <!-- 数轴 -->
  <line x1="30" y1="100" x2="470" y2="100" stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
  
  <!-- 原点O -->
  <line x1="100" y1="95" x2="100" y2="105" stroke="#333" stroke-width="2"/>
  <text x="100" y="120" text-anchor="middle" font-size="12" fill="#333">O</text>
  <text x="100" y="135" text-anchor="middle" font-size="10" fill="#666">0</text>
  
  <!-- 起始点 (8个单位) -->
  <line x1="340" y1="95" x2="340" y2="105" stroke="#333" stroke-width="2"/>
  <text x="340" y="120" text-anchor="middle" font-size="12" fill="#333">8</text>
  <circle cx="340" cy="100" r="5" fill="#e74c3c"/>
  <text x="340" y="85" text-anchor="middle" font-size="12" fill="#e74c3c">P</text>
  
  <!-- 跳跃路径 -->
  <path d="M 340 90 Q 280 50 220 90" stroke="#3498db" stroke-width="1.5" fill="none" stroke-dasharray="4"/>
  <text x="280" y="55" text-anchor="middle" font-size="10" fill="#3498db">M₁</text>
  
  <path d="M 220 90 Q 180 60 160 90" stroke="#27ae60" stroke-width="1.5" fill="none" stroke-dasharray="4"/>
  <text x="190" y="65" text-anchor="middle" font-size="10" fill="#27ae60">M₂</text>
  
  <!-- 中间点 -->
  <circle cx="220" cy="100" r="4" fill="#3498db"/>
  <circle cx="160" cy="100" r="4" fill="#27ae60"/>
'''
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def generate_all():
    """生成所有SVG图形"""
    ensure_dir()
    
    # 代数面积图
    area_square_diagram("area-square.svg")
    
    # 围棋棋子图案
    chess_pattern("chess-pattern.svg")
    
    # 火柴棒图案
    for i in range(1, 5):
        matchstick_pattern(f"matchstick-{i}.svg", i)
    
    # 正多边形扩展
    for sides in [3, 4, 5, 6]:
        polygon_expansion(f"polygon-{sides}.svg", sides)
    
    # 房屋平面图
    house_floor_plan("house-plan.svg")
    
    # 正方体
    cube_diagram("cube.svg")
    
    # 双圆滚动
    two_circles_on_line("two-circles.svg")
    
    # 数轴折叠
    folding_number_line("folding-line.svg")
    
    # 跳跃点
    jumping_point("jumping-point.svg")
    
    print("\n✅ All additional SVG files generated successfully!")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    generate_all()


