#!/usr/bin/env python3
"""
生成几何图形SVG（角度、线段、射线等）
"""

import os
import math

SVG_DIR = "../packages/app/assets/svg"

def ensure_dir():
    os.makedirs(SVG_DIR, exist_ok=True)

def angle_rays_from_point(filename, rays_count=5, angle_span=150):
    """生成从O点发出的多条射线（角度问题）"""
    width = 400
    height = 300
    cx, cy = 200, 200  # O点位置
    ray_length = 150
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#333"/>
    </marker>
  </defs>
'''
    
    labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'][:rays_count]
    colors = ['#e74c3c', '#3498db', '#27ae60', '#f39c12', '#9b59b6', '#1abc9c']
    
    start_angle = -angle_span / 2
    angle_step = angle_span / (rays_count - 1) if rays_count > 1 else 0
    
    for i, label in enumerate(labels):
        angle = math.radians(start_angle + i * angle_step - 90)  # -90 to start from top
        end_x = cx + ray_length * math.cos(angle)
        end_y = cy + ray_length * math.sin(angle)
        color = colors[i % len(colors)]
        
        svg += f'''  <line x1="{cx}" y1="{cy}" x2="{end_x}" y2="{end_y}" 
        stroke="{color}" stroke-width="2" marker-end="url(#arrowhead)"/>
  <text x="{end_x + 15 * math.cos(angle)}" y="{end_y + 15 * math.sin(angle)}" 
        text-anchor="middle" font-size="16" font-weight="bold" fill="{color}">{label}</text>
'''
    
    # O点
    svg += f'''
  <circle cx="{cx}" cy="{cy}" r="4" fill="#333"/>
  <text x="{cx - 15}" y="{cy + 20}" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">O</text>
'''
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def angle_bisector(filename):
    """生成角平分线图"""
    width = 400
    height = 300
    cx, cy = 100, 250
    ray_length = 200
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#333"/>
    </marker>
  </defs>
'''
    
    # 射线 OA (水平向右)
    svg += f'''  <line x1="{cx}" y1="{cy}" x2="{cx + ray_length}" y2="{cy}" 
        stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
  <text x="{cx + ray_length + 15}" y="{cy}" text-anchor="middle" font-size="16" font-weight="bold">A</text>
'''
    
    # 射线 OB (向上倾斜)
    angle_b = math.radians(-60)
    end_bx = cx + ray_length * math.cos(angle_b)
    end_by = cy + ray_length * math.sin(angle_b)
    svg += f'''  <line x1="{cx}" y1="{cy}" x2="{end_bx}" y2="{end_by}" 
        stroke="#3498db" stroke-width="2" marker-end="url(#arrowhead)"/>
  <text x="{end_bx + 10}" y="{end_by - 10}" text-anchor="middle" font-size="16" font-weight="bold" fill="#3498db">B</text>
'''
    
    # 射线 OC (角平分线，虚线)
    angle_c = math.radians(-30)
    end_cx = cx + ray_length * 0.9 * math.cos(angle_c)
    end_cy = cy + ray_length * 0.9 * math.sin(angle_c)
    svg += f'''  <line x1="{cx}" y1="{cy}" x2="{end_cx}" y2="{end_cy}" 
        stroke="#e74c3c" stroke-width="2" stroke-dasharray="5" marker-end="url(#arrowhead)"/>
  <text x="{end_cx + 10}" y="{end_cy}" text-anchor="middle" font-size="16" font-weight="bold" fill="#e74c3c">C</text>
'''
    
    # 角度弧
    svg += f'''
  <path d="M {cx + 40} {cy} A 40 40 0 0 0 {cx + 40 * math.cos(angle_b)} {cy + 40 * math.sin(angle_b)}" 
        fill="none" stroke="#666" stroke-width="1.5"/>
'''
    
    # O点
    svg += f'''
  <circle cx="{cx}" cy="{cy}" r="4" fill="#333"/>
  <text x="{cx - 15}" y="{cy + 5}" text-anchor="middle" font-size="16" font-weight="bold">O</text>
'''
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def rotating_angle(filename):
    """生成旋转角度问题图"""
    width = 400
    height = 300
    cx, cy = 200, 200
    ray_length = 130
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#333"/>
    </marker>
  </defs>
'''
    
    # 固定射线 OA, OB
    angles = {
        'A': 0,
        'B': -120,
    }
    
    for label, deg in angles.items():
        angle = math.radians(deg)
        end_x = cx + ray_length * math.cos(angle)
        end_y = cy + ray_length * math.sin(angle)
        svg += f'''  <line x1="{cx}" y1="{cy}" x2="{end_x}" y2="{end_y}" 
        stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
  <text x="{end_x + 15 * math.cos(angle)}" y="{end_y + 15 * math.sin(angle)}" 
        text-anchor="middle" font-size="16" font-weight="bold">{label}</text>
'''
    
    # 旋转射线 OM (蓝色虚线)
    angle_m = math.radians(-45)
    end_mx = cx + ray_length * math.cos(angle_m)
    end_my = cy + ray_length * math.sin(angle_m)
    svg += f'''  <line x1="{cx}" y1="{cy}" x2="{end_mx}" y2="{end_my}" 
        stroke="#3498db" stroke-width="2" stroke-dasharray="5" marker-end="url(#arrowhead)"/>
  <text x="{end_mx + 12}" y="{end_my - 5}" text-anchor="middle" font-size="16" font-weight="bold" fill="#3498db">M</text>
'''
    
    # 旋转射线 ON (红色虚线)
    angle_n = math.radians(-80)
    end_nx = cx + ray_length * math.cos(angle_n)
    end_ny = cy + ray_length * math.sin(angle_n)
    svg += f'''  <line x1="{cx}" y1="{cy}" x2="{end_nx}" y2="{end_ny}" 
        stroke="#e74c3c" stroke-width="2" stroke-dasharray="5" marker-end="url(#arrowhead)"/>
  <text x="{end_nx - 5}" y="{end_ny - 10}" text-anchor="middle" font-size="16" font-weight="bold" fill="#e74c3c">N</text>
'''
    
    # 旋转箭头
    svg += f'''
  <path d="M {cx + 50} {cy - 30} A 50 50 0 0 0 {cx + 30} {cy - 50}" 
        fill="none" stroke="#27ae60" stroke-width="2" marker-end="url(#arrowhead)"/>
  <text x="{cx + 60}" y="{cy - 50}" font-size="12" fill="#27ae60">旋转</text>
'''
    
    # O点
    svg += f'''
  <circle cx="{cx}" cy="{cy}" r="4" fill="#333"/>
  <text x="{cx + 15}" y="{cy + 15}" text-anchor="middle" font-size="16" font-weight="bold">O</text>
'''
    
    # 角度标注
    svg += f'''
  <path d="M {cx + 30} {cy} A 30 30 0 0 0 {cx + 30 * math.cos(math.radians(-120))} {cy + 30 * math.sin(math.radians(-120))}" 
        fill="none" stroke="#666" stroke-width="1"/>
  <text x="{cx - 20}" y="{cy - 40}" font-size="12" fill="#666">120°</text>
'''
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def line_segment_abc(filename):
    """生成线段ABC图"""
    width = 400
    height = 100
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <!-- 线段 -->
  <line x1="50" y1="50" x2="350" y2="50" stroke="#333" stroke-width="2"/>
  
  <!-- 点A -->
  <circle cx="50" cy="50" r="4" fill="#e74c3c"/>
  <text x="50" y="35" text-anchor="middle" font-size="16" font-weight="bold" fill="#e74c3c">A</text>
  
  <!-- 点B -->
  <circle cx="200" cy="50" r="4" fill="#3498db"/>
  <text x="200" y="35" text-anchor="middle" font-size="16" font-weight="bold" fill="#3498db">B</text>
  
  <!-- 点C -->
  <circle cx="350" cy="50" r="4" fill="#27ae60"/>
  <text x="350" y="35" text-anchor="middle" font-size="16" font-weight="bold" fill="#27ae60">C</text>
</svg>'''
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def line_segment_with_midpoints(filename):
    """生成带中点的线段图"""
    width = 500
    height = 100
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <!-- 线段 -->
  <line x1="50" y1="50" x2="450" y2="50" stroke="#333" stroke-width="2"/>
  
  <!-- 点A -->
  <circle cx="50" cy="50" r="4" fill="#e74c3c"/>
  <text x="50" y="35" text-anchor="middle" font-size="14" font-weight="bold" fill="#e74c3c">A</text>
  
  <!-- 点M (AC中点) -->
  <circle cx="150" cy="50" r="4" fill="#9b59b6"/>
  <text x="150" y="75" text-anchor="middle" font-size="14" font-weight="bold" fill="#9b59b6">M</text>
  
  <!-- 点C -->
  <circle cx="250" cy="50" r="4" fill="#3498db"/>
  <text x="250" y="35" text-anchor="middle" font-size="14" font-weight="bold" fill="#3498db">C</text>
  
  <!-- 点N (BC中点) -->
  <circle cx="350" cy="50" r="4" fill="#f39c12"/>
  <text x="350" y="75" text-anchor="middle" font-size="14" font-weight="bold" fill="#f39c12">N</text>
  
  <!-- 点B -->
  <circle cx="450" cy="50" r="4" fill="#27ae60"/>
  <text x="450" y="35" text-anchor="middle" font-size="14" font-weight="bold" fill="#27ae60">B</text>
</svg>'''
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def triangle_with_lines(filename):
    """生成带线段的三角形"""
    width = 300
    height = 250
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <!-- 三角形 -->
  <polygon points="150,30 50,200 250,200" fill="none" stroke="#333" stroke-width="2"/>
  
  <!-- 顶点标记 -->
  <text x="150" y="20" text-anchor="middle" font-size="14" font-weight="bold">A</text>
  <text x="40" y="215" text-anchor="middle" font-size="14" font-weight="bold">B</text>
  <text x="260" y="215" text-anchor="middle" font-size="14" font-weight="bold">C</text>
  
  <!-- 中线 -->
  <line x1="150" y1="30" x2="150" y2="200" stroke="#e74c3c" stroke-width="1.5" stroke-dasharray="4"/>
  <circle cx="150" cy="200" r="3" fill="#e74c3c"/>
  <text x="160" y="215" text-anchor="start" font-size="12" fill="#e74c3c">D</text>
  
  <!-- 高或其他辅助线 -->
  <line x1="50" y1="200" x2="250" y2="200" stroke="#3498db" stroke-width="1"/>
</svg>'''
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def angle_aob_with_bisector(filename, main_angle=150):
    """生成∠AOB及其平分线"""
    width = 400
    height = 300
    cx, cy = 80, 250
    ray_length = 250
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#333"/>
    </marker>
  </defs>
'''
    
    # 射线 OA (水平)
    svg += f'''  <line x1="{cx}" y1="{cy}" x2="{cx + ray_length}" y2="{cy}" 
        stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
  <text x="{cx + ray_length + 12}" y="{cy + 5}" font-size="16" font-weight="bold">A</text>
'''
    
    # 射线 OB
    angle_b = math.radians(-main_angle)
    end_bx = cx + ray_length * math.cos(angle_b)
    end_by = cy + ray_length * math.sin(angle_b)
    svg += f'''  <line x1="{cx}" y1="{cy}" x2="{end_bx}" y2="{end_by}" 
        stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
  <text x="{end_bx + 8}" y="{end_by - 5}" font-size="16" font-weight="bold">B</text>
'''
    
    # 射线 OC (平分线)
    angle_c = math.radians(-main_angle / 2)
    end_cx = cx + ray_length * 0.85 * math.cos(angle_c)
    end_cy = cy + ray_length * 0.85 * math.sin(angle_c)
    svg += f'''  <line x1="{cx}" y1="{cy}" x2="{end_cx}" y2="{end_cy}" 
        stroke="#e74c3c" stroke-width="2" stroke-dasharray="5" marker-end="url(#arrowhead)"/>
  <text x="{end_cx + 10}" y="{end_cy}" font-size="16" font-weight="bold" fill="#e74c3c">C</text>
'''
    
    # 角度弧
    arc_r = 50
    svg += f'''
  <path d="M {cx + arc_r} {cy} A {arc_r} {arc_r} 0 0 0 {cx + arc_r * math.cos(angle_b)} {cy + arc_r * math.sin(angle_b)}" 
        fill="none" stroke="#666" stroke-width="1"/>
  <text x="{cx + 35}" y="{cy - 35}" font-size="12" fill="#666">{main_angle}°</text>
'''
    
    # O点
    svg += f'''
  <circle cx="{cx}" cy="{cy}" r="4" fill="#333"/>
  <text x="{cx - 12}" y="{cy + 18}" font-size="16" font-weight="bold">O</text>
'''
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def multiple_rays_angle(filename):
    """生成多条射线（5条）从O点发出的图"""
    width = 400
    height = 350
    cx, cy = 80, 300
    ray_length = 280
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#333"/>
    </marker>
  </defs>
'''
    
    rays = [
        ('A', 0, '#333'),
        ('B', -30, '#e74c3c'),
        ('C', -60, '#3498db'),
        ('D', -90, '#27ae60'),
        ('E', -120, '#f39c12'),
    ]
    
    for label, deg, color in rays:
        angle = math.radians(deg)
        length = ray_length if label in ['A', 'E'] else ray_length * 0.85
        end_x = cx + length * math.cos(angle)
        end_y = cy + length * math.sin(angle)
        
        dash = '' if label in ['A', 'B', 'E'] else 'stroke-dasharray="5"'
        svg += f'''  <line x1="{cx}" y1="{cy}" x2="{end_x}" y2="{end_y}" 
        stroke="{color}" stroke-width="2" {dash} marker-end="url(#arrowhead)"/>
  <text x="{end_x + 12 * math.cos(angle)}" y="{end_y + 12 * math.sin(angle) - 3}" 
        text-anchor="middle" font-size="16" font-weight="bold" fill="{color}">{label}</text>
'''
    
    # O点
    svg += f'''
  <circle cx="{cx}" cy="{cy}" r="4" fill="#333"/>
  <text x="{cx - 15}" y="{cy + 18}" font-size="16" font-weight="bold">O</text>
'''
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def generate_all():
    """生成所有几何SVG"""
    ensure_dir()
    
    # 角度图
    angle_rays_from_point("angle-rays-5.svg", 5, 150)
    angle_rays_from_point("angle-rays-4.svg", 4, 120)
    angle_rays_from_point("angle-rays-3.svg", 3, 90)
    
    # 角平分线
    angle_bisector("angle-bisector.svg")
    
    # 旋转角度
    rotating_angle("rotating-angle.svg")
    
    # 线段图
    line_segment_abc("segment-abc.svg")
    line_segment_with_midpoints("segment-midpoints.svg")
    
    # 三角形
    triangle_with_lines("triangle-lines.svg")
    
    # 角AOB及平分线
    angle_aob_with_bisector("angle-aob-150.svg", 150)
    angle_aob_with_bisector("angle-aob-120.svg", 120)
    
    # 多射线
    multiple_rays_angle("rays-abcde.svg")
    
    print("\n✅ All geometry SVG files generated successfully!")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    generate_all()

"""
生成几何图形SVG（角度、线段、射线等）
"""

import os
import math

SVG_DIR = "../packages/app/assets/svg"

def ensure_dir():
    os.makedirs(SVG_DIR, exist_ok=True)

def angle_rays_from_point(filename, rays_count=5, angle_span=150):
    """生成从O点发出的多条射线（角度问题）"""
    width = 400
    height = 300
    cx, cy = 200, 200  # O点位置
    ray_length = 150
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#333"/>
    </marker>
  </defs>
'''
    
    labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'][:rays_count]
    colors = ['#e74c3c', '#3498db', '#27ae60', '#f39c12', '#9b59b6', '#1abc9c']
    
    start_angle = -angle_span / 2
    angle_step = angle_span / (rays_count - 1) if rays_count > 1 else 0
    
    for i, label in enumerate(labels):
        angle = math.radians(start_angle + i * angle_step - 90)  # -90 to start from top
        end_x = cx + ray_length * math.cos(angle)
        end_y = cy + ray_length * math.sin(angle)
        color = colors[i % len(colors)]
        
        svg += f'''  <line x1="{cx}" y1="{cy}" x2="{end_x}" y2="{end_y}" 
        stroke="{color}" stroke-width="2" marker-end="url(#arrowhead)"/>
  <text x="{end_x + 15 * math.cos(angle)}" y="{end_y + 15 * math.sin(angle)}" 
        text-anchor="middle" font-size="16" font-weight="bold" fill="{color}">{label}</text>
'''
    
    # O点
    svg += f'''
  <circle cx="{cx}" cy="{cy}" r="4" fill="#333"/>
  <text x="{cx - 15}" y="{cy + 20}" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">O</text>
'''
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def angle_bisector(filename):
    """生成角平分线图"""
    width = 400
    height = 300
    cx, cy = 100, 250
    ray_length = 200
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#333"/>
    </marker>
  </defs>
'''
    
    # 射线 OA (水平向右)
    svg += f'''  <line x1="{cx}" y1="{cy}" x2="{cx + ray_length}" y2="{cy}" 
        stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
  <text x="{cx + ray_length + 15}" y="{cy}" text-anchor="middle" font-size="16" font-weight="bold">A</text>
'''
    
    # 射线 OB (向上倾斜)
    angle_b = math.radians(-60)
    end_bx = cx + ray_length * math.cos(angle_b)
    end_by = cy + ray_length * math.sin(angle_b)
    svg += f'''  <line x1="{cx}" y1="{cy}" x2="{end_bx}" y2="{end_by}" 
        stroke="#3498db" stroke-width="2" marker-end="url(#arrowhead)"/>
  <text x="{end_bx + 10}" y="{end_by - 10}" text-anchor="middle" font-size="16" font-weight="bold" fill="#3498db">B</text>
'''
    
    # 射线 OC (角平分线，虚线)
    angle_c = math.radians(-30)
    end_cx = cx + ray_length * 0.9 * math.cos(angle_c)
    end_cy = cy + ray_length * 0.9 * math.sin(angle_c)
    svg += f'''  <line x1="{cx}" y1="{cy}" x2="{end_cx}" y2="{end_cy}" 
        stroke="#e74c3c" stroke-width="2" stroke-dasharray="5" marker-end="url(#arrowhead)"/>
  <text x="{end_cx + 10}" y="{end_cy}" text-anchor="middle" font-size="16" font-weight="bold" fill="#e74c3c">C</text>
'''
    
    # 角度弧
    svg += f'''
  <path d="M {cx + 40} {cy} A 40 40 0 0 0 {cx + 40 * math.cos(angle_b)} {cy + 40 * math.sin(angle_b)}" 
        fill="none" stroke="#666" stroke-width="1.5"/>
'''
    
    # O点
    svg += f'''
  <circle cx="{cx}" cy="{cy}" r="4" fill="#333"/>
  <text x="{cx - 15}" y="{cy + 5}" text-anchor="middle" font-size="16" font-weight="bold">O</text>
'''
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def rotating_angle(filename):
    """生成旋转角度问题图"""
    width = 400
    height = 300
    cx, cy = 200, 200
    ray_length = 130
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#333"/>
    </marker>
  </defs>
'''
    
    # 固定射线 OA, OB
    angles = {
        'A': 0,
        'B': -120,
    }
    
    for label, deg in angles.items():
        angle = math.radians(deg)
        end_x = cx + ray_length * math.cos(angle)
        end_y = cy + ray_length * math.sin(angle)
        svg += f'''  <line x1="{cx}" y1="{cy}" x2="{end_x}" y2="{end_y}" 
        stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
  <text x="{end_x + 15 * math.cos(angle)}" y="{end_y + 15 * math.sin(angle)}" 
        text-anchor="middle" font-size="16" font-weight="bold">{label}</text>
'''
    
    # 旋转射线 OM (蓝色虚线)
    angle_m = math.radians(-45)
    end_mx = cx + ray_length * math.cos(angle_m)
    end_my = cy + ray_length * math.sin(angle_m)
    svg += f'''  <line x1="{cx}" y1="{cy}" x2="{end_mx}" y2="{end_my}" 
        stroke="#3498db" stroke-width="2" stroke-dasharray="5" marker-end="url(#arrowhead)"/>
  <text x="{end_mx + 12}" y="{end_my - 5}" text-anchor="middle" font-size="16" font-weight="bold" fill="#3498db">M</text>
'''
    
    # 旋转射线 ON (红色虚线)
    angle_n = math.radians(-80)
    end_nx = cx + ray_length * math.cos(angle_n)
    end_ny = cy + ray_length * math.sin(angle_n)
    svg += f'''  <line x1="{cx}" y1="{cy}" x2="{end_nx}" y2="{end_ny}" 
        stroke="#e74c3c" stroke-width="2" stroke-dasharray="5" marker-end="url(#arrowhead)"/>
  <text x="{end_nx - 5}" y="{end_ny - 10}" text-anchor="middle" font-size="16" font-weight="bold" fill="#e74c3c">N</text>
'''
    
    # 旋转箭头
    svg += f'''
  <path d="M {cx + 50} {cy - 30} A 50 50 0 0 0 {cx + 30} {cy - 50}" 
        fill="none" stroke="#27ae60" stroke-width="2" marker-end="url(#arrowhead)"/>
  <text x="{cx + 60}" y="{cy - 50}" font-size="12" fill="#27ae60">旋转</text>
'''
    
    # O点
    svg += f'''
  <circle cx="{cx}" cy="{cy}" r="4" fill="#333"/>
  <text x="{cx + 15}" y="{cy + 15}" text-anchor="middle" font-size="16" font-weight="bold">O</text>
'''
    
    # 角度标注
    svg += f'''
  <path d="M {cx + 30} {cy} A 30 30 0 0 0 {cx + 30 * math.cos(math.radians(-120))} {cy + 30 * math.sin(math.radians(-120))}" 
        fill="none" stroke="#666" stroke-width="1"/>
  <text x="{cx - 20}" y="{cy - 40}" font-size="12" fill="#666">120°</text>
'''
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def line_segment_abc(filename):
    """生成线段ABC图"""
    width = 400
    height = 100
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <!-- 线段 -->
  <line x1="50" y1="50" x2="350" y2="50" stroke="#333" stroke-width="2"/>
  
  <!-- 点A -->
  <circle cx="50" cy="50" r="4" fill="#e74c3c"/>
  <text x="50" y="35" text-anchor="middle" font-size="16" font-weight="bold" fill="#e74c3c">A</text>
  
  <!-- 点B -->
  <circle cx="200" cy="50" r="4" fill="#3498db"/>
  <text x="200" y="35" text-anchor="middle" font-size="16" font-weight="bold" fill="#3498db">B</text>
  
  <!-- 点C -->
  <circle cx="350" cy="50" r="4" fill="#27ae60"/>
  <text x="350" y="35" text-anchor="middle" font-size="16" font-weight="bold" fill="#27ae60">C</text>
</svg>'''
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def line_segment_with_midpoints(filename):
    """生成带中点的线段图"""
    width = 500
    height = 100
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <!-- 线段 -->
  <line x1="50" y1="50" x2="450" y2="50" stroke="#333" stroke-width="2"/>
  
  <!-- 点A -->
  <circle cx="50" cy="50" r="4" fill="#e74c3c"/>
  <text x="50" y="35" text-anchor="middle" font-size="14" font-weight="bold" fill="#e74c3c">A</text>
  
  <!-- 点M (AC中点) -->
  <circle cx="150" cy="50" r="4" fill="#9b59b6"/>
  <text x="150" y="75" text-anchor="middle" font-size="14" font-weight="bold" fill="#9b59b6">M</text>
  
  <!-- 点C -->
  <circle cx="250" cy="50" r="4" fill="#3498db"/>
  <text x="250" y="35" text-anchor="middle" font-size="14" font-weight="bold" fill="#3498db">C</text>
  
  <!-- 点N (BC中点) -->
  <circle cx="350" cy="50" r="4" fill="#f39c12"/>
  <text x="350" y="75" text-anchor="middle" font-size="14" font-weight="bold" fill="#f39c12">N</text>
  
  <!-- 点B -->
  <circle cx="450" cy="50" r="4" fill="#27ae60"/>
  <text x="450" y="35" text-anchor="middle" font-size="14" font-weight="bold" fill="#27ae60">B</text>
</svg>'''
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def triangle_with_lines(filename):
    """生成带线段的三角形"""
    width = 300
    height = 250
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <!-- 三角形 -->
  <polygon points="150,30 50,200 250,200" fill="none" stroke="#333" stroke-width="2"/>
  
  <!-- 顶点标记 -->
  <text x="150" y="20" text-anchor="middle" font-size="14" font-weight="bold">A</text>
  <text x="40" y="215" text-anchor="middle" font-size="14" font-weight="bold">B</text>
  <text x="260" y="215" text-anchor="middle" font-size="14" font-weight="bold">C</text>
  
  <!-- 中线 -->
  <line x1="150" y1="30" x2="150" y2="200" stroke="#e74c3c" stroke-width="1.5" stroke-dasharray="4"/>
  <circle cx="150" cy="200" r="3" fill="#e74c3c"/>
  <text x="160" y="215" text-anchor="start" font-size="12" fill="#e74c3c">D</text>
  
  <!-- 高或其他辅助线 -->
  <line x1="50" y1="200" x2="250" y2="200" stroke="#3498db" stroke-width="1"/>
</svg>'''
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def angle_aob_with_bisector(filename, main_angle=150):
    """生成∠AOB及其平分线"""
    width = 400
    height = 300
    cx, cy = 80, 250
    ray_length = 250
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#333"/>
    </marker>
  </defs>
'''
    
    # 射线 OA (水平)
    svg += f'''  <line x1="{cx}" y1="{cy}" x2="{cx + ray_length}" y2="{cy}" 
        stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
  <text x="{cx + ray_length + 12}" y="{cy + 5}" font-size="16" font-weight="bold">A</text>
'''
    
    # 射线 OB
    angle_b = math.radians(-main_angle)
    end_bx = cx + ray_length * math.cos(angle_b)
    end_by = cy + ray_length * math.sin(angle_b)
    svg += f'''  <line x1="{cx}" y1="{cy}" x2="{end_bx}" y2="{end_by}" 
        stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
  <text x="{end_bx + 8}" y="{end_by - 5}" font-size="16" font-weight="bold">B</text>
'''
    
    # 射线 OC (平分线)
    angle_c = math.radians(-main_angle / 2)
    end_cx = cx + ray_length * 0.85 * math.cos(angle_c)
    end_cy = cy + ray_length * 0.85 * math.sin(angle_c)
    svg += f'''  <line x1="{cx}" y1="{cy}" x2="{end_cx}" y2="{end_cy}" 
        stroke="#e74c3c" stroke-width="2" stroke-dasharray="5" marker-end="url(#arrowhead)"/>
  <text x="{end_cx + 10}" y="{end_cy}" font-size="16" font-weight="bold" fill="#e74c3c">C</text>
'''
    
    # 角度弧
    arc_r = 50
    svg += f'''
  <path d="M {cx + arc_r} {cy} A {arc_r} {arc_r} 0 0 0 {cx + arc_r * math.cos(angle_b)} {cy + arc_r * math.sin(angle_b)}" 
        fill="none" stroke="#666" stroke-width="1"/>
  <text x="{cx + 35}" y="{cy - 35}" font-size="12" fill="#666">{main_angle}°</text>
'''
    
    # O点
    svg += f'''
  <circle cx="{cx}" cy="{cy}" r="4" fill="#333"/>
  <text x="{cx - 12}" y="{cy + 18}" font-size="16" font-weight="bold">O</text>
'''
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def multiple_rays_angle(filename):
    """生成多条射线（5条）从O点发出的图"""
    width = 400
    height = 350
    cx, cy = 80, 300
    ray_length = 280
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#333"/>
    </marker>
  </defs>
'''
    
    rays = [
        ('A', 0, '#333'),
        ('B', -30, '#e74c3c'),
        ('C', -60, '#3498db'),
        ('D', -90, '#27ae60'),
        ('E', -120, '#f39c12'),
    ]
    
    for label, deg, color in rays:
        angle = math.radians(deg)
        length = ray_length if label in ['A', 'E'] else ray_length * 0.85
        end_x = cx + length * math.cos(angle)
        end_y = cy + length * math.sin(angle)
        
        dash = '' if label in ['A', 'B', 'E'] else 'stroke-dasharray="5"'
        svg += f'''  <line x1="{cx}" y1="{cy}" x2="{end_x}" y2="{end_y}" 
        stroke="{color}" stroke-width="2" {dash} marker-end="url(#arrowhead)"/>
  <text x="{end_x + 12 * math.cos(angle)}" y="{end_y + 12 * math.sin(angle) - 3}" 
        text-anchor="middle" font-size="16" font-weight="bold" fill="{color}">{label}</text>
'''
    
    # O点
    svg += f'''
  <circle cx="{cx}" cy="{cy}" r="4" fill="#333"/>
  <text x="{cx - 15}" y="{cy + 18}" font-size="16" font-weight="bold">O</text>
'''
    
    svg += '</svg>'
    
    with open(os.path.join(SVG_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filename}")

def generate_all():
    """生成所有几何SVG"""
    ensure_dir()
    
    # 角度图
    angle_rays_from_point("angle-rays-5.svg", 5, 150)
    angle_rays_from_point("angle-rays-4.svg", 4, 120)
    angle_rays_from_point("angle-rays-3.svg", 3, 90)
    
    # 角平分线
    angle_bisector("angle-bisector.svg")
    
    # 旋转角度
    rotating_angle("rotating-angle.svg")
    
    # 线段图
    line_segment_abc("segment-abc.svg")
    line_segment_with_midpoints("segment-midpoints.svg")
    
    # 三角形
    triangle_with_lines("triangle-lines.svg")
    
    # 角AOB及平分线
    angle_aob_with_bisector("angle-aob-150.svg", 150)
    angle_aob_with_bisector("angle-aob-120.svg", 120)
    
    # 多射线
    multiple_rays_angle("rays-abcde.svg")
    
    print("\n✅ All geometry SVG files generated successfully!")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    generate_all()


