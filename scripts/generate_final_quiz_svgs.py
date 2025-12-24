#!/usr/bin/env python3
"""生成期末冲刺练习的SVG图形"""

import os

SVG_DIR = 'packages/app/assets/svg'

def create_svg(filename, content, width=600, height=200):
    """创建SVG文件"""
    filepath = os.path.join(SVG_DIR, filename)
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <style>
    .line {{ stroke: #333; stroke-width: 2; fill: none; }}
    .thin-line {{ stroke: #333; stroke-width: 1.5; fill: none; }}
    .arrow {{ stroke: #333; stroke-width: 2; fill: #333; }}
    .point {{ fill: #2563eb; }}
    .label {{ font-family: 'Times New Roman', serif; font-size: 16px; fill: #333; }}
    .small-label {{ font-family: 'Times New Roman', serif; font-size: 14px; fill: #333; }}
    .italic {{ font-style: italic; }}
  </style>
{content}
</svg>'''
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"✅ Created: {filename}")


def create_final_number_line_1():
    """第1题：数轴上a、b两点位置"""
    content = '''
  <!-- 数轴 -->
  <line x1="50" y1="100" x2="550" y2="100" class="line"/>
  <polygon points="550,100 540,95 540,105" class="arrow"/>
  
  <!-- 刻度线 -->
  <line x1="100" y1="93" x2="100" y2="107" class="thin-line"/>
  <line x1="200" y1="93" x2="200" y2="107" class="thin-line"/>
  <line x1="300" y1="93" x2="300" y2="107" class="thin-line"/>
  <line x1="400" y1="93" x2="400" y2="107" class="thin-line"/>
  <line x1="500" y1="93" x2="500" y2="107" class="thin-line"/>
  
  <!-- 刻度标签 -->
  <text x="100" y="130" class="label" text-anchor="middle">-2</text>
  <text x="200" y="130" class="label" text-anchor="middle">-1</text>
  <text x="300" y="130" class="label" text-anchor="middle">0</text>
  <text x="400" y="130" class="label" text-anchor="middle">1</text>
  <text x="500" y="130" class="label" text-anchor="middle">2</text>
  
  <!-- b点 (在-1和0之间，偏左) -->
  <circle cx="170" cy="100" r="5" class="point"/>
  <text x="170" y="80" class="label italic" text-anchor="middle">b</text>
  
  <!-- a点 (在0和1之间，偏右) -->
  <circle cx="430" cy="100" r="5" class="point"/>
  <text x="430" y="80" class="label italic" text-anchor="middle">a</text>
'''
    create_svg('final-number-line-1.svg', content, 600, 160)


def create_final_cube():
    """第2题：立方体展开图和堆叠图"""
    content = '''
  <!-- 图1：展开图 -->
  <text x="120" y="30" class="small-label" text-anchor="middle">图1</text>
  
  <!-- 展开图十字形状 -->
  <rect x="80" y="40" width="40" height="40" fill="none" stroke="#333" stroke-width="1.5"/>
  <text x="100" y="67" class="label" text-anchor="middle">5</text>
  
  <rect x="40" y="80" width="40" height="40" fill="none" stroke="#333" stroke-width="1.5"/>
  <text x="60" y="107" class="label" text-anchor="middle">1</text>
  
  <rect x="80" y="80" width="40" height="40" fill="none" stroke="#333" stroke-width="1.5"/>
  <text x="100" y="107" class="label" text-anchor="middle">2</text>
  
  <rect x="120" y="80" width="40" height="40" fill="none" stroke="#333" stroke-width="1.5"/>
  <text x="140" y="107" class="label" text-anchor="middle">3</text>
  
  <rect x="160" y="80" width="40" height="40" fill="none" stroke="#333" stroke-width="1.5"/>
  <text x="180" y="107" class="label" text-anchor="middle">4</text>
  
  <rect x="80" y="120" width="40" height="40" fill="none" stroke="#333" stroke-width="1.5"/>
  <text x="100" y="147" class="label" text-anchor="middle">6</text>
  
  <!-- 图2：三个立方体堆叠 -->
  <text x="380" y="30" class="small-label" text-anchor="middle">图2</text>
  
  <!-- 底部立方体 -->
  <polygon points="300,160 340,160 360,140 320,140" fill="#f0f0f0" stroke="#333" stroke-width="1.5"/>
  <polygon points="340,160 360,140 360,100 340,120" fill="#e0e0e0" stroke="#333" stroke-width="1.5"/>
  <polygon points="300,160 340,160 340,120 300,120" fill="#d0d0d0" stroke="#333" stroke-width="1.5"/>
  
  <!-- 中间立方体 -->
  <polygon points="340,120 380,120 400,100 360,100" fill="#f0f0f0" stroke="#333" stroke-width="1.5"/>
  <polygon points="380,120 400,100 400,60 380,80" fill="#e0e0e0" stroke="#333" stroke-width="1.5"/>
  <polygon points="340,120 380,120 380,80 340,80" fill="#d0d0d0" stroke="#333" stroke-width="1.5"/>
  
  <!-- 顶部立方体 -->
  <polygon points="380,80 420,80 440,60 400,60" fill="#f0f0f0" stroke="#333" stroke-width="1.5"/>
  <polygon points="420,80 440,60 440,20 420,40" fill="#e0e0e0" stroke="#333" stroke-width="1.5"/>
  <polygon points="380,80 420,80 420,40 380,40" fill="#d0d0d0" stroke="#333" stroke-width="1.5"/>
'''
    create_svg('final-cube.svg', content, 500, 180)


def create_final_triangles():
    """第4题：三角尺摆放方式"""
    content = '''
  <!-- A选项 -->
  <g transform="translate(30, 20)">
    <!-- 三角形1 -->
    <polygon points="0,80 80,80 0,0" fill="none" stroke="#333" stroke-width="1.5"/>
    <!-- 三角形2 -->
    <polygon points="10,70 70,70 70,10" fill="none" stroke="#333" stroke-width="1.5"/>
    <!-- 角度标记 -->
    <text x="8" y="65" class="small-label italic">α</text>
    <text x="55" y="65" class="small-label italic">β</text>
    <text x="40" y="105" class="small-label" text-anchor="middle">A</text>
  </g>
  
  <!-- B选项 -->
  <g transform="translate(160, 20)">
    <!-- 三角形1 -->
    <polygon points="0,80 80,80 80,0" fill="none" stroke="#333" stroke-width="1.5"/>
    <!-- 三角形2 -->
    <polygon points="10,70 70,70 10,10" fill="none" stroke="#333" stroke-width="1.5"/>
    <!-- 角度标记 -->
    <text x="60" y="65" class="small-label italic">β</text>
    <text x="18" y="25" class="small-label italic">α</text>
    <text x="40" y="105" class="small-label" text-anchor="middle">B</text>
  </g>
  
  <!-- C选项 -->
  <g transform="translate(290, 20)">
    <!-- 三角形1 -->
    <polygon points="0,80 80,80 40,0" fill="none" stroke="#333" stroke-width="1.5"/>
    <!-- 三角形2（内部） -->
    <polygon points="20,80 60,80 40,30" fill="none" stroke="#333" stroke-width="1.5"/>
    <!-- 角度标记 -->
    <text x="8" y="70" class="small-label italic">α</text>
    <text x="60" y="70" class="small-label italic">β</text>
    <text x="40" y="105" class="small-label" text-anchor="middle">C</text>
  </g>
  
  <!-- D选项 -->
  <g transform="translate(420, 20)">
    <!-- 三角形1 -->
    <polygon points="0,80 80,80 80,20" fill="none" stroke="#333" stroke-width="1.5"/>
    <!-- 三角形2 -->
    <polygon points="0,60 60,60 0,0" fill="none" stroke="#333" stroke-width="1.5"/>
    <!-- 角度标记 -->
    <text x="65" y="70" class="small-label italic">α</text>
    <text x="8" y="50" class="small-label italic">β</text>
    <text x="40" y="105" class="small-label" text-anchor="middle">D</text>
  </g>
'''
    create_svg('final-triangles.svg', content, 540, 130)


def create_final_angle_12():
    """第12题：角度综合图"""
    content = '''
  <!-- 原点O -->
  <circle cx="100" cy="150" r="3" fill="#333"/>
  <text x="88" y="165" class="label italic">O</text>
  
  <!-- 射线OB (水平向右) -->
  <line x1="100" y1="150" x2="350" y2="150" class="line"/>
  <text x="355" y="155" class="label italic">B</text>
  
  <!-- 射线OA (垂直向上) -->
  <line x1="100" y1="150" x2="100" y2="20" class="line"/>
  <text x="95" y="12" class="label italic">A</text>
  
  <!-- 射线OC (在∠AOB内) -->
  <line x1="100" y1="150" x2="280" y2="40" class="line"/>
  <text x="290" y="35" class="label italic">C</text>
  
  <!-- 射线OD (在∠AOB内，更靠近OB) -->
  <line x1="100" y1="150" x2="320" y2="85" class="line"/>
  <text x="330" y="85" class="label italic">D</text>
  
  <!-- 角度弧线 ∠COD -->
  <path d="M 160 115 A 60 60 0 0 1 175 95" fill="none" stroke="#2563eb" stroke-width="1.5"/>
  
  <!-- 直角标记 -->
  <polyline points="100,135 115,135 115,150" fill="none" stroke="#333" stroke-width="1"/>
'''
    create_svg('final-angle-12.svg', content, 400, 180)


def create_final_number_line_15():
    """第15题：数轴上A、B、C三点"""
    content = '''
  <!-- 数轴 -->
  <line x1="30" y1="80" x2="570" y2="80" class="line"/>
  <polygon points="570,80 560,75 560,85" class="arrow"/>
  
  <!-- 刻度线和点 -->
  <!-- A点 (-26) -->
  <line x1="80" y1="73" x2="80" y2="87" class="thin-line"/>
  <circle cx="80" cy="80" r="4" class="point"/>
  <text x="80" y="60" class="label italic" text-anchor="middle">A</text>
  <text x="80" y="108" class="label" text-anchor="middle">-26</text>
  
  <!-- B点 (-10) -->
  <line x1="210" y1="73" x2="210" y2="87" class="thin-line"/>
  <circle cx="210" cy="80" r="4" class="point"/>
  <text x="210" y="60" class="label italic" text-anchor="middle">B</text>
  <text x="210" y="108" class="label" text-anchor="middle">-10</text>
  
  <!-- 原点 (0) -->
  <line x1="290" y1="73" x2="290" y2="87" class="thin-line"/>
  <text x="290" y="108" class="label" text-anchor="middle">0</text>
  
  <!-- C点 (10) -->
  <line x1="370" y1="73" x2="370" y2="87" class="thin-line"/>
  <circle cx="370" cy="80" r="4" class="point"/>
  <text x="370" y="60" class="label italic" text-anchor="middle">C</text>
  <text x="370" y="108" class="label" text-anchor="middle">10</text>
'''
    create_svg('final-number-line-15.svg', content, 600, 130)


def create_final_segment_16():
    """第16题图1：线段MN上的AB运动"""
    content = '''
  <!-- 线段MN -->
  <line x1="50" y1="80" x2="550" y2="80" class="line"/>
  
  <!-- M点 -->
  <circle cx="50" cy="80" r="3" fill="#333"/>
  <text x="50" y="60" class="label italic" text-anchor="middle">M</text>
  
  <!-- C点 -->
  <circle cx="150" cy="80" r="3" fill="#333"/>
  <text x="150" y="60" class="label italic" text-anchor="middle">C</text>
  
  <!-- A点 -->
  <circle cx="250" cy="80" r="4" class="point"/>
  <text x="250" y="60" class="label italic" text-anchor="middle">A</text>
  
  <!-- B点 -->
  <circle cx="350" cy="80" r="4" class="point"/>
  <text x="350" y="60" class="label italic" text-anchor="middle">B</text>
  
  <!-- D点 -->
  <circle cx="450" cy="80" r="3" fill="#333"/>
  <text x="450" y="60" class="label italic" text-anchor="middle">D</text>
  
  <!-- N点 -->
  <circle cx="550" cy="80" r="3" fill="#333"/>
  <text x="550" y="60" class="label italic" text-anchor="middle">N</text>
  
  <text x="300" y="120" class="small-label" text-anchor="middle">图1</text>
'''
    create_svg('final-segment-16.svg', content, 600, 140)


def create_final_angle_16_2():
    """第16题图2：角MON内的角AOB转动"""
    content = '''
  <!-- 原点O -->
  <circle cx="150" cy="130" r="3" fill="#333"/>
  <text x="140" y="145" class="label italic">O</text>
  
  <!-- 射线OM -->
  <line x1="150" y1="130" x2="50" y2="60" class="line"/>
  <text x="40" y="55" class="label italic">M</text>
  
  <!-- 射线ON (水平向右) -->
  <line x1="150" y1="130" x2="330" y2="130" class="line"/>
  <text x="340" y="135" class="label italic">N</text>
  
  <!-- 射线OC -->
  <line x1="150" y1="130" x2="90" y2="50" class="thin-line" stroke="#666"/>
  <text x="80" y="45" class="small-label italic" fill="#666">C</text>
  
  <!-- 射线OA -->
  <line x1="150" y1="130" x2="200" y2="30" class="line"/>
  <text x="205" y="25" class="label italic">A</text>
  
  <!-- 射线OB -->
  <line x1="150" y1="130" x2="300" y2="70" class="line"/>
  <text x="310" y="65" class="label italic">B</text>
  
  <!-- 射线OD -->
  <line x1="150" y1="130" x2="290" y2="110" class="thin-line" stroke="#666"/>
  <text x="300" y="108" class="small-label italic" fill="#666">D</text>
  
  <text x="190" y="165" class="small-label" text-anchor="middle">图2</text>
'''
    create_svg('final-angle-16-2.svg', content, 380, 180)


def create_final_angle_16_3():
    """第16题图3：角比例问题"""
    content = '''
  <!-- 原点O -->
  <circle cx="100" cy="130" r="3" fill="#333"/>
  <text x="85" y="145" class="label italic">O</text>
  
  <!-- 射线OM -->
  <line x1="100" y1="130" x2="30" y2="70" class="line"/>
  <text x="20" y="65" class="label italic">M</text>
  
  <!-- 射线ON (水平向右) -->
  <line x1="100" y1="130" x2="320" y2="130" class="line"/>
  <text x="330" y="135" class="label italic">N</text>
  
  <!-- 射线OC -->
  <line x1="100" y1="130" x2="80" y2="40" class="line"/>
  <text x="75" y="30" class="label italic">C</text>
  
  <!-- 射线OA -->
  <line x1="100" y1="130" x2="180" y2="30" class="line"/>
  <text x="190" y="25" class="label italic">A</text>
  
  <!-- 射线OB -->
  <line x1="100" y1="130" x2="280" y2="70" class="line"/>
  <text x="290" y="65" class="label italic">B</text>
  
  <!-- 射线OD -->
  <line x1="100" y1="130" x2="280" y2="105" class="line"/>
  <text x="290" y="100" class="label italic">D</text>
  
  <text x="175" y="165" class="small-label" text-anchor="middle">图3</text>
'''
    create_svg('final-angle-16-3.svg', content, 370, 180)


if __name__ == '__main__':
    # 确保目录存在
    os.makedirs(SVG_DIR, exist_ok=True)
    
    print("开始生成期末冲刺练习SVG图形...")
    
    create_final_number_line_1()    # 第1题
    create_final_cube()              # 第2题
    create_final_triangles()         # 第4题
    create_final_angle_12()          # 第12题
    create_final_number_line_15()    # 第15题
    create_final_segment_16()        # 第16题图1
    create_final_angle_16_2()        # 第16题图2
    create_final_angle_16_3()        # 第16题图3
    
    print("\n✅ 所有期末冲刺练习SVG图形生成完成！")


