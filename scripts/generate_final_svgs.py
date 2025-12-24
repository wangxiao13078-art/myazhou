#!/usr/bin/env python3
"""生成期末冲刺练习的SVG图形"""

import os

SVG_DIR = 'public/svg'

def ensure_dir():
    os.makedirs(SVG_DIR, exist_ok=True)

def create_number_line_ab_final1():
    """第1题：数轴上a、b两点位置"""
    svg = '''<svg width="500" height="120" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#333"/>
    </marker>
  </defs>
  
  <!-- 数轴 -->
  <line x1="30" y1="60" x2="470" y2="60" stroke="#333" stroke-width="2" marker-end="url(#arrow1)"/>
  
  <!-- 刻度 -->
  <line x1="100" y1="55" x2="100" y2="65" stroke="#333" stroke-width="2"/>
  <text x="100" y="85" text-anchor="middle" font-size="14">-2</text>
  
  <line x1="180" y1="55" x2="180" y2="65" stroke="#333" stroke-width="2"/>
  <text x="180" y="85" text-anchor="middle" font-size="14">-1</text>
  
  <line x1="260" y1="55" x2="260" y2="65" stroke="#333" stroke-width="2"/>
  <text x="260" y="85" text-anchor="middle" font-size="14">0</text>
  
  <line x1="340" y1="55" x2="340" y2="65" stroke="#333" stroke-width="2"/>
  <text x="340" y="85" text-anchor="middle" font-size="14">1</text>
  
  <line x1="420" y1="55" x2="420" y2="65" stroke="#333" stroke-width="2"/>
  <text x="420" y="85" text-anchor="middle" font-size="14">2</text>
  
  <!-- 点b在-1和0之间 -->
  <circle cx="150" cy="60" r="5" fill="#2196F3"/>
  <text x="150" y="40" text-anchor="middle" font-size="14" font-style="italic">b</text>
  
  <!-- 点a在1和2之间 -->
  <circle cx="380" cy="60" r="5" fill="#F44336"/>
  <text x="380" y="40" text-anchor="middle" font-size="14" font-style="italic">a</text>
</svg>'''
    with open(f'{SVG_DIR}/final-1-number-line.svg', 'w') as f:
        f.write(svg)

def create_cube_unfold_final2():
    """第2题：立方体展开图和堆叠图"""
    svg = '''<svg width="550" height="200" xmlns="http://www.w3.org/2000/svg">
  <!-- 图1：展开图 -->
  <text x="100" y="20" text-anchor="middle" font-size="12">图1</text>
  
  <!-- 十字形展开 -->
  <rect x="70" y="30" width="40" height="40" fill="none" stroke="#333" stroke-width="1.5"/>
  <text x="90" y="55" text-anchor="middle" font-size="14">5</text>
  
  <rect x="30" y="70" width="40" height="40" fill="none" stroke="#333" stroke-width="1.5"/>
  <text x="50" y="95" text-anchor="middle" font-size="14">1</text>
  
  <rect x="70" y="70" width="40" height="40" fill="none" stroke="#333" stroke-width="1.5"/>
  <text x="90" y="95" text-anchor="middle" font-size="14">2</text>
  
  <rect x="110" y="70" width="40" height="40" fill="none" stroke="#333" stroke-width="1.5"/>
  <text x="130" y="95" text-anchor="middle" font-size="14">3</text>
  
  <rect x="150" y="70" width="40" height="40" fill="none" stroke="#333" stroke-width="1.5"/>
  <text x="170" y="95" text-anchor="middle" font-size="14">4</text>
  
  <rect x="70" y="110" width="40" height="40" fill="none" stroke="#333" stroke-width="1.5"/>
  <text x="90" y="135" text-anchor="middle" font-size="14">6</text>
  
  <!-- 图2：三个立方体堆叠 -->
  <text x="400" y="20" text-anchor="middle" font-size="12">图2</text>
  
  <!-- 第一个立方体（底层左） -->
  <polygon points="300,150 340,150 340,110 300,110" fill="#e3f2fd" stroke="#333" stroke-width="1.5"/>
  <polygon points="340,150 370,130 370,90 340,110" fill="#bbdefb" stroke="#333" stroke-width="1.5"/>
  <polygon points="300,110 340,110 370,90 330,90" fill="#90caf9" stroke="#333" stroke-width="1.5"/>
  
  <!-- 第二个立方体（底层右） -->
  <polygon points="340,150 380,150 380,110 340,110" fill="#e3f2fd" stroke="#333" stroke-width="1.5"/>
  <polygon points="380,150 410,130 410,90 380,110" fill="#bbdefb" stroke="#333" stroke-width="1.5"/>
  <polygon points="340,110 380,110 410,90 370,90" fill="#90caf9" stroke="#333" stroke-width="1.5"/>
  
  <!-- 第三个立方体（上层） -->
  <polygon points="340,110 380,110 380,70 340,70" fill="#e3f2fd" stroke="#333" stroke-width="1.5"/>
  <polygon points="380,110 410,90 410,50 380,70" fill="#bbdefb" stroke="#333" stroke-width="1.5"/>
  <polygon points="340,70 380,70 410,50 370,50" fill="#90caf9" stroke="#333" stroke-width="1.5"/>
</svg>'''
    with open(f'{SVG_DIR}/final-2-cube.svg', 'w') as f:
        f.write(svg)

def create_triangles_final4():
    """第4题：三角尺摆放图"""
    svg = '''<svg width="500" height="250" xmlns="http://www.w3.org/2000/svg">
  <!-- 选项A -->
  <text x="60" y="20" text-anchor="middle" font-size="14" font-weight="bold">A</text>
  <polygon points="20,100 80,100 80,40" fill="none" stroke="#333" stroke-width="1.5"/>
  <polygon points="80,100 80,40 120,100" fill="none" stroke="#333" stroke-width="1.5"/>
  <text x="45" y="85" font-size="12" font-style="italic">α</text>
  <text x="95" y="85" font-size="12" font-style="italic">β</text>
  
  <!-- 选项B -->
  <text x="190" y="20" text-anchor="middle" font-size="14" font-weight="bold">B</text>
  <polygon points="150,100 210,100 210,40" fill="none" stroke="#333" stroke-width="1.5"/>
  <polygon points="210,100 210,40 250,100" fill="none" stroke="#333" stroke-width="1.5"/>
  <text x="175" y="85" font-size="12" font-style="italic">β</text>
  <text x="225" y="60" font-size="12" font-style="italic">α</text>
  
  <!-- 选项C -->
  <text x="60" y="130" text-anchor="middle" font-size="14" font-weight="bold">C</text>
  <polygon points="20,210 80,210 50,150" fill="none" stroke="#333" stroke-width="1.5"/>
  <polygon points="80,210 120,210 80,150" fill="none" stroke="#333" stroke-width="1.5"/>
  <text x="45" y="195" font-size="12" font-style="italic">α</text>
  <text x="95" y="195" font-size="12" font-style="italic">β</text>
  
  <!-- 选项D -->
  <text x="190" y="130" text-anchor="middle" font-size="14" font-weight="bold">D</text>
  <polygon points="150,210 210,210 180,150" fill="none" stroke="#333" stroke-width="1.5"/>
  <polygon points="210,210 250,210 210,150" fill="none" stroke="#333" stroke-width="1.5"/>
  <text x="175" y="165" font-size="12" font-style="italic">α</text>
  <text x="225" y="195" font-size="12" font-style="italic">β</text>
</svg>'''
    with open(f'{SVG_DIR}/final-4-triangles.svg', 'w') as f:
        f.write(svg)

def create_angle_final12():
    """第12题：角度图（多射线从O点发出）"""
    svg = '''<svg width="350" height="200" xmlns="http://www.w3.org/2000/svg">
  <!-- 点O -->
  <circle cx="100" cy="150" r="3" fill="#333"/>
  <text x="85" y="165" font-size="14" font-style="italic">O</text>
  
  <!-- 射线OA（水平向左上） -->
  <line x1="100" y1="150" x2="30" y2="80" stroke="#333" stroke-width="1.5"/>
  <text x="20" y="70" font-size="14" font-style="italic">A</text>
  
  <!-- 射线OB（水平向右） -->
  <line x1="100" y1="150" x2="300" y2="150" stroke="#333" stroke-width="1.5"/>
  <text x="305" y="155" font-size="14" font-style="italic">B</text>
  
  <!-- 射线OC（中间偏上） -->
  <line x1="100" y1="150" x2="180" y2="50" stroke="#2196F3" stroke-width="1.5"/>
  <text x="185" y="45" font-size="14" font-style="italic" fill="#2196F3">C</text>
  
  <!-- 射线OD（中间偏下） -->
  <line x1="100" y1="150" x2="250" y2="100" stroke="#F44336" stroke-width="1.5"/>
  <text x="255" y="95" font-size="14" font-style="italic" fill="#F44336">D</text>
  
  <!-- 角度标记 -->
  <path d="M 120,150 A 20,20 0 0,0 115,135" fill="none" stroke="#333" stroke-width="1"/>
  <path d="M 115,135 A 25,25 0 0,0 100,130" fill="none" stroke="#2196F3" stroke-width="1"/>
  
  <!-- 90度标记 -->
  <rect x="100" y="130" width="8" height="8" fill="none" stroke="#333" stroke-width="1"/>
  
  <!-- 标注角AOB = 90° -->
  <text x="200" y="180" font-size="12">∠AOB = 90°</text>
  <text x="200" y="195" font-size="12">∠COD = 45°</text>
</svg>'''
    with open(f'{SVG_DIR}/final-12-angle.svg', 'w') as f:
        f.write(svg)

def create_number_line_abc_final15():
    """第15题：数轴ABC三点"""
    svg = '''<svg width="550" height="120" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow15" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#333"/>
    </marker>
  </defs>
  
  <!-- 数轴 -->
  <line x1="30" y1="60" x2="520" y2="60" stroke="#333" stroke-width="2" marker-end="url(#arrow15)"/>
  
  <!-- 点A：-26 -->
  <line x1="80" y1="55" x2="80" y2="65" stroke="#333" stroke-width="2"/>
  <circle cx="80" cy="60" r="4" fill="#F44336"/>
  <text x="80" y="85" text-anchor="middle" font-size="12">-26</text>
  <text x="80" y="40" text-anchor="middle" font-size="14" font-style="italic">A</text>
  
  <!-- 点B：-10 -->
  <line x1="200" y1="55" x2="200" y2="65" stroke="#333" stroke-width="2"/>
  <circle cx="200" cy="60" r="4" fill="#2196F3"/>
  <text x="200" y="85" text-anchor="middle" font-size="12">-10</text>
  <text x="200" y="40" text-anchor="middle" font-size="14" font-style="italic">B</text>
  
  <!-- 原点0 -->
  <line x1="280" y1="55" x2="280" y2="65" stroke="#333" stroke-width="2"/>
  <text x="280" y="85" text-anchor="middle" font-size="12">0</text>
  
  <!-- 点C：10 -->
  <line x1="360" y1="55" x2="360" y2="65" stroke="#333" stroke-width="2"/>
  <circle cx="360" cy="60" r="4" fill="#4CAF50"/>
  <text x="360" y="85" text-anchor="middle" font-size="12">10</text>
  <text x="360" y="40" text-anchor="middle" font-size="14" font-style="italic">C</text>
</svg>'''
    with open(f'{SVG_DIR}/final-15-number-line.svg', 'w') as f:
        f.write(svg)

def create_final16_figure1():
    """第16题图1：线段MN上的AB"""
    svg = '''<svg width="400" height="100" xmlns="http://www.w3.org/2000/svg">
  <text x="200" y="20" text-anchor="middle" font-size="12">图1</text>
  
  <!-- 线段MN -->
  <line x1="50" y1="50" x2="350" y2="50" stroke="#333" stroke-width="2"/>
  
  <!-- 点M -->
  <circle cx="50" cy="50" r="3" fill="#333"/>
  <text x="50" y="75" text-anchor="middle" font-size="14" font-style="italic">M</text>
  
  <!-- 点C（AM的中点） -->
  <circle cx="120" cy="50" r="3" fill="#2196F3"/>
  <text x="120" y="75" text-anchor="middle" font-size="14" font-style="italic" fill="#2196F3">C</text>
  
  <!-- 点A -->
  <circle cx="150" cy="50" r="3" fill="#333"/>
  <text x="150" y="35" text-anchor="middle" font-size="14" font-style="italic">A</text>
  
  <!-- 点B -->
  <circle cx="200" cy="50" r="3" fill="#333"/>
  <text x="200" y="35" text-anchor="middle" font-size="14" font-style="italic">B</text>
  
  <!-- 点D（BN的中点） -->
  <circle cx="275" cy="50" r="3" fill="#F44336"/>
  <text x="275" y="75" text-anchor="middle" font-size="14" font-style="italic" fill="#F44336">D</text>
  
  <!-- 点N -->
  <circle cx="350" cy="50" r="3" fill="#333"/>
  <text x="350" y="75" text-anchor="middle" font-size="14" font-style="italic">N</text>
</svg>'''
    with open(f'{SVG_DIR}/final-16-figure1.svg', 'w') as f:
        f.write(svg)

def create_final16_figure2():
    """第16题图2：角度图（∠AOB在∠MON内部转动）"""
    svg = '''<svg width="250" height="180" xmlns="http://www.w3.org/2000/svg">
  <text x="125" y="20" text-anchor="middle" font-size="12">图2</text>
  
  <!-- 点O -->
  <circle cx="80" cy="140" r="3" fill="#333"/>
  <text x="65" y="155" font-size="14" font-style="italic">O</text>
  
  <!-- 射线OM -->
  <line x1="80" y1="140" x2="20" y2="60" stroke="#333" stroke-width="1.5"/>
  <text x="10" y="55" font-size="14" font-style="italic">M</text>
  
  <!-- 射线ON -->
  <line x1="80" y1="140" x2="220" y2="140" stroke="#333" stroke-width="1.5"/>
  <text x="225" y="145" font-size="14" font-style="italic">N</text>
  
  <!-- 射线OA -->
  <line x1="80" y1="140" x2="100" y2="50" stroke="#2196F3" stroke-width="1.5"/>
  <text x="105" y="45" font-size="14" font-style="italic" fill="#2196F3">A</text>
  
  <!-- 射线OB -->
  <line x1="80" y1="140" x2="180" y2="90" stroke="#2196F3" stroke-width="1.5"/>
  <text x="185" y="85" font-size="14" font-style="italic" fill="#2196F3">B</text>
  
  <!-- 射线OC（平分∠AOM） -->
  <line x1="80" y1="140" x2="55" y2="55" stroke="#4CAF50" stroke-width="1" stroke-dasharray="4,2"/>
  <text x="45" y="50" font-size="12" font-style="italic" fill="#4CAF50">C</text>
  
  <!-- 射线OD（平分∠BON） -->
  <line x1="80" y1="140" x2="200" y2="110" stroke="#F44336" stroke-width="1" stroke-dasharray="4,2"/>
  <text x="205" y="105" font-size="12" font-style="italic" fill="#F44336">D</text>
</svg>'''
    with open(f'{SVG_DIR}/final-16-figure2.svg', 'w') as f:
        f.write(svg)

def create_final16_figure3():
    """第16题图3：角度比例图"""
    svg = '''<svg width="250" height="180" xmlns="http://www.w3.org/2000/svg">
  <text x="125" y="20" text-anchor="middle" font-size="12">图3</text>
  
  <!-- 点O -->
  <circle cx="80" cy="140" r="3" fill="#333"/>
  <text x="65" y="155" font-size="14" font-style="italic">O</text>
  
  <!-- 射线OM -->
  <line x1="80" y1="140" x2="20" y2="60" stroke="#333" stroke-width="1.5"/>
  <text x="10" y="55" font-size="14" font-style="italic">M</text>
  
  <!-- 射线ON -->
  <line x1="80" y1="140" x2="220" y2="140" stroke="#333" stroke-width="1.5"/>
  <text x="225" y="145" font-size="14" font-style="italic">N</text>
  
  <!-- 射线OA -->
  <line x1="80" y1="140" x2="90" y2="45" stroke="#2196F3" stroke-width="1.5"/>
  <text x="95" y="40" font-size="14" font-style="italic" fill="#2196F3">A</text>
  
  <!-- 射线OB -->
  <line x1="80" y1="140" x2="190" y2="80" stroke="#2196F3" stroke-width="1.5"/>
  <text x="195" y="75" font-size="14" font-style="italic" fill="#2196F3">B</text>
  
  <!-- 射线OC -->
  <line x1="80" y1="140" x2="50" y2="50" stroke="#4CAF50" stroke-width="1.5"/>
  <text x="40" y="45" font-size="14" font-style="italic" fill="#4CAF50">C</text>
  
  <!-- 射线OD -->
  <line x1="80" y1="140" x2="210" y2="100" stroke="#F44336" stroke-width="1.5"/>
  <text x="215" y="95" font-size="14" font-style="italic" fill="#F44336">D</text>
</svg>'''
    with open(f'{SVG_DIR}/final-16-figure3.svg', 'w') as f:
        f.write(svg)

if __name__ == '__main__':
    ensure_dir()
    create_number_line_ab_final1()
    create_cube_unfold_final2()
    create_triangles_final4()
    create_angle_final12()
    create_number_line_abc_final15()
    create_final16_figure1()
    create_final16_figure2()
    create_final16_figure3()
    print("✅ 期末冲刺练SVG图形生成完成!")


