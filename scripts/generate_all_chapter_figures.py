#!/usr/bin/env python3
"""
完整的章节图形生成脚本

按照扫描文件夹的章节格式组织：
- 专题一：有理数 (第1-3页)
  - 考法1-7：数轴问题、绝对值等
- 专题二：有理数的运算 (第4-10页)
  - 考点1-5：运算技巧、数轴问题、新定义
- 专题三：代数式 (第11-14页)
  - 考点1-5：字母表示数、求值、规律探究
- 专题四：整式的加减 (第15-19页)
  - 考法1-4：整体思想、数轴化简、分类讨论
- 专题五：一元一次方程 (第20-26页)
  - 考点1-4：解方程、应用问题
- 专题六：几何图形初步 (第27-33页)
  - 考点1：线段计算（整体思想、方程思想、分类讨论、数形结合）
  - 考点2：角度计算
"""

import os
import math
from pathlib import Path

# 输出目录
OUTPUT_DIR = Path(__file__).parent.parent / "apps" / "miniprogram" / "images" / "svg"

def ensure_dir():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ============== 通用SVG生成器 ==============

class SvgBuilder:
    """SVG构建器"""
    
    def __init__(self, width=400, height=80):
        self.width = width
        self.height = height
        self.elements = []
    
    def add_line(self, x1, y1, x2, y2, stroke="#333", stroke_width=2, dash=None):
        attrs = f'x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{stroke_width}"'
        if dash:
            attrs += f' stroke-dasharray="{dash}"'
        self.elements.append(f'  <line {attrs}/>')
    
    def add_circle(self, cx, cy, r=4, fill="#333", stroke=None):
        attrs = f'cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"'
        if stroke:
            attrs += f' stroke="{stroke}" stroke-width="1"'
        self.elements.append(f'  <circle {attrs}/>')
    
    def add_text(self, x, y, text, font_size=14, anchor="middle", fill="#333", font_family="Arial"):
        self.elements.append(f'  <text x="{x}" y="{y}" font-family="{font_family}" font-size="{font_size}" text-anchor="{anchor}" fill="{fill}">{text}</text>')
    
    def add_polygon(self, points, fill="#333", stroke=None):
        points_str = " ".join(f"{p[0]},{p[1]}" for p in points)
        attrs = f'points="{points_str}" fill="{fill}"'
        if stroke:
            attrs += f' stroke="{stroke}"'
        self.elements.append(f'  <polygon {attrs}/>')
    
    def add_path(self, d, fill="none", stroke="#333", stroke_width=1.5):
        self.elements.append(f'  <path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"/>')
    
    def add_rect(self, x, y, width, height, fill="#fff", stroke=None, rx=0):
        attrs = f'x="{x}" y="{y}" width="{width}" height="{height}" fill="{fill}"'
        if stroke:
            attrs += f' stroke="{stroke}"'
        if rx:
            attrs += f' rx="{rx}"'
        self.elements.append(f'  <rect {attrs}/>')
    
    def build(self):
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.width} {self.height}">\n'
        svg += '\n'.join(self.elements)
        svg += '\n</svg>'
        return svg


# ============== 专题一：有理数 ==============

def gen_numberline_basic(min_v=-5, max_v=5, points=None, width=400, height=80):
    """生成基础数轴"""
    svg = SvgBuilder(width, height)
    margin = 40
    line_y = height // 2
    scale = (width - 2 * margin) / (max_v - min_v)
    
    def val_to_x(v): return margin + (v - min_v) * scale
    
    # 主轴
    svg.add_line(margin - 10, line_y, width - margin + 10, line_y)
    # 箭头
    svg.add_polygon([(width - margin + 10, line_y), (width - margin, line_y - 5), (width - margin, line_y + 5)])
    
    # 刻度
    for i in range(min_v, max_v + 1):
        x = val_to_x(i)
        svg.add_line(x, line_y - 5, x, line_y + 5, stroke_width=1.5)
        svg.add_text(x, line_y + 20, str(i), font_size=12)
    
    # 原点O
    if min_v <= 0 <= max_v:
        svg.add_text(val_to_x(0), line_y + 32, "O", font_size=11, fill="#666")
    
    # 标记点
    if points:
        for i, p in enumerate(points):
            x = val_to_x(p['value'])
            color = p.get('color', '#2196F3')
            svg.add_circle(x, line_y, 4, fill=color)
            if p.get('label'):
                y = line_y - 12 if i % 2 == 0 else line_y + 28
                svg.add_text(x, y, p['label'], font_size=13, fill=color)
    
    return svg.build()


def gen_segment_line(points, width=400, height=80):
    """生成线段图"""
    svg = SvgBuilder(width, height)
    margin = 40
    line_y = height // 2
    line_len = width - 2 * margin
    
    def pos_to_x(pos): return margin + (pos / 100) * line_len
    
    positions = [p['position'] for p in points]
    svg.add_line(pos_to_x(min(positions)), line_y, pos_to_x(max(positions)), line_y)
    
    for p in points:
        x = pos_to_x(p['position'])
        is_end = p['position'] in [0, 100]
        color = p.get('color', '#333' if is_end else '#2196F3')
        svg.add_circle(x, line_y, 4 if is_end else 3, fill=color)
        svg.add_text(x, line_y + 22, p['name'], font_size=14, fill=color)
    
    return svg.build()


def gen_angle_figure(vertex, rays, width=300, height=200, arc_radius=30):
    """生成角度图"""
    svg = SvgBuilder(width, height)
    ray_len = 100
    
    def get_end(angle):
        rad = math.radians(angle)
        return (vertex['x'] + ray_len * math.cos(rad), 
                vertex['y'] - ray_len * math.sin(rad))
    
    # 顶点
    svg.add_circle(vertex['x'], vertex['y'], 4)
    svg.add_text(vertex['x'], vertex['y'] + 20, vertex.get('label', 'O'))
    
    # 射线
    for ray in rays:
        end = get_end(ray['angle'])
        color = ray.get('color', '#333')
        dash = ray.get('dash')
        svg.add_line(vertex['x'], vertex['y'], end[0], end[1], stroke=color, dash=dash)
        
        # 标签
        label_dist = ray_len + 15
        label_x = vertex['x'] + label_dist * math.cos(math.radians(ray['angle']))
        label_y = vertex['y'] - label_dist * math.sin(math.radians(ray['angle']))
        svg.add_text(label_x, label_y, ray.get('label', ''), fill=color)
    
    # 角度弧
    if len(rays) >= 2:
        angles = sorted([r['angle'] for r in rays[:2]])
        start_rad = -angles[1] * math.pi / 180
        end_rad = -angles[0] * math.pi / 180
        
        sx = vertex['x'] + arc_radius * math.cos(start_rad)
        sy = vertex['y'] + arc_radius * math.sin(start_rad)
        ex = vertex['x'] + arc_radius * math.cos(end_rad)
        ey = vertex['y'] + arc_radius * math.sin(end_rad)
        
        large_arc = 1 if (angles[1] - angles[0]) > 180 else 0
        svg.add_path(f"M {sx} {sy} A {arc_radius} {arc_radius} 0 {large_arc} 1 {ex} {ey}", stroke="#2196F3")
    
    return svg.build()


def gen_circle_on_numberline(center=0, radius=1, min_v=-5, max_v=5, mark_angle=180, mark_label='A', width=400, height=120):
    """生成圆在数轴上的图形"""
    svg = SvgBuilder(width, height)
    margin = 40
    line_y = height - 30
    scale = (width - 2 * margin) / (max_v - min_v)
    r_scaled = radius * scale
    
    def val_to_x(v): return margin + (v - min_v) * scale
    
    cx = val_to_x(center)
    cy = line_y - r_scaled
    
    # 数轴
    svg.add_line(margin - 10, line_y, width - margin + 10, line_y)
    svg.add_polygon([(width - margin + 10, line_y), (width - margin, line_y - 4), (width - margin, line_y + 4)])
    
    for i in range(min_v, max_v + 1):
        x = val_to_x(i)
        svg.add_line(x, line_y - 4, x, line_y + 4, stroke_width=1.5)
        svg.add_text(x, line_y + 18, str(i), font_size=11)
    
    # 圆
    svg.add_circle(cx, cy, r_scaled, fill="none", stroke="#2196F3")
    
    # 标记点
    rad = math.radians(mark_angle)
    mx = cx + r_scaled * math.cos(rad)
    my = cy - r_scaled * math.sin(rad)
    svg.add_circle(mx, my, 4, fill="#E91E63")
    svg.add_text(mx, my - 8, mark_label, font_size=12, fill="#E91E63")
    
    return svg.build()


# ============== 生成所有图形 ==============

def generate_all_figures():
    """生成所有章节图形"""
    ensure_dir()
    
    figures = {}
    
    # ===== 专题一：有理数 =====
    # t1: 数轴整点与动点问题
    figures['t1_example'] = gen_numberline_basic(-10, 12, [
        {'value': -8, 'label': 'A', 'color': '#E91E63'},
        {'value': 10, 'label': 'B', 'color': '#E91E63'}
    ], width=450)
    
    figures['t1_train_1'] = gen_circle_on_numberline(-1, 1, -5, 5, 180, 'A')
    figures['t1_train_2'] = gen_numberline_basic(-8, 4, [
        {'value': -6, 'label': '甲', 'color': '#2196F3'},
        {'value': 0, 'label': 'O', 'color': '#333'}
    ])
    figures['t1_train_5'] = gen_numberline_basic(-10, 12, [
        {'value': -8, 'label': 'A', 'color': '#2196F3'},
        {'value': 10, 'label': 'B', 'color': '#4CAF50'}
    ], width=450)
    figures['t1_train_6'] = gen_numberline_basic(-8, 8, [
        {'value': -5, 'label': 'A', 'color': '#2196F3'},
        {'value': 5, 'label': 'B', 'color': '#4CAF50'}
    ])
    figures['t1_train_7'] = gen_numberline_basic(-6, 6, [
        {'value': -3, 'label': 'P', 'color': '#E91E63'}
    ])
    
    # t2: 数轴规律探究
    figures['t2_example'] = gen_numberline_basic(-2, 8, [
        {'value': 0, 'label': 'O', 'color': '#333'},
        {'value': 1, 'label': 'A₁', 'color': '#2196F3'},
        {'value': 3, 'label': 'A₂', 'color': '#4CAF50'},
        {'value': 6, 'label': 'A₃', 'color': '#FF9800'}
    ])
    figures['t2_train_1'] = gen_numberline_basic(-1, 10, [
        {'value': 0, 'label': 'A₀', 'color': '#333'},
        {'value': 2, 'label': 'A₁', 'color': '#2196F3'},
        {'value': 4, 'label': 'A₂', 'color': '#2196F3'},
        {'value': 8, 'label': 'A₃', 'color': '#2196F3'}
    ])
    
    # t3-t7: 绝对值相关
    figures['t5_example'] = gen_numberline_basic(-5, 5, [
        {'value': -3, 'label': 'a', 'color': '#2196F3'},
        {'value': 2, 'label': 'b', 'color': '#4CAF50'}
    ])
    figures['t5_train_1'] = gen_numberline_basic(-4, 4, [
        {'value': -2, 'label': 'a', 'color': '#2196F3'},
        {'value': 1, 'label': 'b', 'color': '#4CAF50'},
        {'value': 3, 'label': 'c', 'color': '#E91E63'}
    ])
    
    # ===== 专题二：有理数的运算 =====
    # t12: 数轴折叠
    figures['t12_example'] = gen_numberline_basic(-4, 8, [
        {'value': -2, 'label': 'A', 'color': '#2196F3'},
        {'value': 3, 'label': 'M', 'color': '#E91E63'},
        {'value': 8, 'label': 'B', 'color': '#2196F3'}
    ])
    figures['t12_train_1'] = gen_numberline_basic(-3, 5, [
        {'value': -1, 'label': 'A', 'color': '#2196F3'},
        {'value': 2, 'label': 'C', 'color': '#E91E63'},
        {'value': 5, 'label': 'B', 'color': '#2196F3'}
    ])
    figures['t12_train_2'] = gen_numberline_basic(-5, 7, [
        {'value': -3, 'label': 'P', 'color': '#2196F3'},
        {'value': 1, 'label': 'O', 'color': '#333'},
        {'value': 5, 'label': 'Q', 'color': '#4CAF50'}
    ])
    
    # t13: 数轴动点
    figures['t13_example'] = gen_numberline_basic(-6, 10, [
        {'value': -4, 'label': 'A', 'color': '#2196F3'},
        {'value': 0, 'label': 'O', 'color': '#333'},
        {'value': 8, 'label': 'B', 'color': '#2196F3'}
    ])
    figures['t13_train_1'] = gen_numberline_basic(-5, 8, [
        {'value': -2, 'label': 'P', 'color': '#E91E63'},
        {'value': 3, 'label': 'M', 'color': '#4CAF50'},
        {'value': 6, 'label': 'Q', 'color': '#E91E63'}
    ])
    
    # ===== 专题六：几何图形初步 =====
    # t32: 线段中点 - 整体思想
    figures['t32_example'] = gen_segment_line([
        {'name': 'A', 'position': 0},
        {'name': 'M', 'position': 25, 'color': '#2196F3'},
        {'name': 'C', 'position': 50, 'color': '#4CAF50'},
        {'name': 'N', 'position': 75, 'color': '#2196F3'},
        {'name': 'B', 'position': 100}
    ])
    figures['t32_train_1'] = gen_segment_line([
        {'name': 'A', 'position': 0},
        {'name': 'M', 'position': 22, 'color': '#2196F3'},
        {'name': 'C', 'position': 45},
        {'name': 'N', 'position': 72, 'color': '#2196F3'},
        {'name': 'B', 'position': 100}
    ])
    figures['t32_train_2'] = gen_segment_line([
        {'name': 'A', 'position': 0},
        {'name': 'M', 'position': 28, 'color': '#2196F3'},
        {'name': 'C', 'position': 57, 'color': '#4CAF50'},
        {'name': 'N', 'position': 78, 'color': '#2196F3'},
        {'name': 'B', 'position': 100}
    ])
    
    # t33: 方程思想
    figures['t33_example'] = gen_segment_line([
        {'name': 'A', 'position': 0},
        {'name': 'D', 'position': 18, 'color': '#E91E63'},
        {'name': 'E', 'position': 50, 'color': '#2196F3'},
        {'name': 'B', 'position': 80},
        {'name': 'C', 'position': 100}
    ])
    figures['t33_train_1'] = gen_segment_line([
        {'name': 'A', 'position': 0},
        {'name': 'M', 'position': 33, 'color': '#2196F3'},
        {'name': 'C', 'position': 66, 'color': '#4CAF50'},
        {'name': 'N', 'position': 83, 'color': '#2196F3'},
        {'name': 'B', 'position': 100}
    ])
    figures['t33_train_2'] = gen_segment_line([
        {'name': 'A', 'position': 0},
        {'name': 'M', 'position': 50, 'color': '#2196F3'},
        {'name': 'B', 'position': 75},
        {'name': 'N', 'position': 88, 'color': '#2196F3'},
        {'name': 'C', 'position': 100}
    ])
    
    # t34: 分类讨论
    figures['t34_example'] = gen_segment_line([
        {'name': 'A', 'position': 0},
        {'name': 'C', 'position': 28, 'color': '#4CAF50'},
        {'name': 'P', 'position': 45, 'color': '#E91E63'},
        {'name': 'Q', 'position': 65, 'color': '#9C27B0'},
        {'name': 'B', 'position': 100}
    ])
    figures['t34_train_1'] = gen_segment_line([
        {'name': 'A', 'position': 0},
        {'name': 'D', 'position': 30, 'color': '#2196F3'},
        {'name': 'C', 'position': 60, 'color': '#4CAF50'},
        {'name': 'B', 'position': 100}
    ])
    figures['t34_train_2'] = gen_segment_line([
        {'name': 'A', 'position': 0},
        {'name': 'C', 'position': 67, 'color': '#4CAF50'},
        {'name': 'B', 'position': 100}
    ])
    
    # t35: 数形结合
    figures['t35_example'] = gen_numberline_basic(-12, 22, [
        {'value': -10, 'label': 'A', 'color': '#2196F3'},
        {'value': -8, 'label': 'B', 'color': '#2196F3'},
        {'value': 16, 'label': 'C', 'color': '#4CAF50'},
        {'value': 20, 'label': 'D', 'color': '#4CAF50'}
    ], width=500)
    figures['t35_train_1'] = gen_numberline_basic(-8, 15, [
        {'value': -5, 'label': 'A', 'color': '#2196F3'},
        {'value': -2, 'label': 'B', 'color': '#2196F3'},
        {'value': 10, 'label': 'C', 'color': '#4CAF50'},
        {'value': 14, 'label': 'D', 'color': '#4CAF50'}
    ], width=480)
    figures['t35_train_2'] = gen_numberline_basic(-6, 12, [
        {'value': -4, 'label': 'A', 'color': '#2196F3'},
        {'value': 0, 'label': 'O', 'color': '#333'},
        {'value': 8, 'label': 'B', 'color': '#4CAF50'}
    ])
    figures['t35_train_3'] = gen_segment_line([
        {'name': 'A', 'position': 0},
        {'name': 'P', 'position': 40, 'color': '#E91E63'},
        {'name': 'B', 'position': 100}
    ])
    figures['t35_train_4'] = gen_numberline_basic(-5, 10, [
        {'value': -3, 'label': 'M', 'color': '#2196F3'},
        {'value': 2, 'label': 'O', 'color': '#333'},
        {'value': 7, 'label': 'N', 'color': '#4CAF50'}
    ])
    
    # t36: 角度计算 - 整体思想
    figures['t36_example'] = gen_angle_figure(
        {'x': 150, 'y': 150, 'label': 'O'},
        [
            {'angle': 0, 'label': 'A'},
            {'angle': 150, 'label': 'B'},
            {'angle': 90, 'label': 'D', 'color': '#2196F3'},
            {'angle': 45, 'label': 'C', 'color': '#4CAF50'},
            {'angle': 120, 'label': 'E', 'color': '#E91E63'}
        ]
    )
    figures['t36_train_1'] = gen_angle_figure(
        {'x': 150, 'y': 150, 'label': 'O'},
        [
            {'angle': 0, 'label': 'A'},
            {'angle': 130, 'label': 'B'},
            {'angle': 65, 'label': 'C', 'color': '#2196F3', 'dash': '5,3'}
        ]
    )
    figures['t36_train_2'] = gen_angle_figure(
        {'x': 150, 'y': 150, 'label': 'O'},
        [
            {'angle': 0, 'label': 'A'},
            {'angle': 90, 'label': 'D', 'color': '#2196F3'},
            {'angle': 140, 'label': 'B'}
        ]
    )
    
    # t37: 旋转角度
    figures['t37_example'] = gen_angle_figure(
        {'x': 150, 'y': 150, 'label': 'O'},
        [
            {'angle': 0, 'label': 'A'},
            {'angle': 120, 'label': 'B'},
            {'angle': 50, 'label': 'M', 'color': '#2196F3'},
            {'angle': 80, 'label': 'N', 'color': '#E91E63'}
        ]
    )
    figures['t37_train_1'] = gen_angle_figure(
        {'x': 150, 'y': 150, 'label': 'O'},
        [
            {'angle': 0, 'label': 'A'},
            {'angle': 90, 'label': 'C', 'color': '#2196F3'},
            {'angle': 150, 'label': 'B'}
        ]
    )
    figures['t37_train_2'] = gen_angle_figure(
        {'x': 150, 'y': 150, 'label': 'O'},
        [
            {'angle': 0, 'label': 'A'},
            {'angle': 60, 'label': 'E', 'color': '#E91E63'},
            {'angle': 120, 'label': 'B'},
            {'angle': 90, 'label': 'C', 'color': '#2196F3'}
        ]
    )
    figures['t37_train_3'] = gen_angle_figure(
        {'x': 150, 'y': 150, 'label': 'O'},
        [
            {'angle': 0, 'label': 'A'},
            {'angle': 45, 'label': 'M', 'color': '#2196F3'},
            {'angle': 90, 'label': 'B'},
            {'angle': 135, 'label': 'N', 'color': '#E91E63'},
            {'angle': 180, 'label': 'C'}
        ]
    )
    
    # 保存所有图形
    for name, content in figures.items():
        path = OUTPUT_DIR / f"{name}.svg"
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ {name}.svg")
    
    print(f"\n共生成 {len(figures)} 个SVG图形")
    return figures


if __name__ == '__main__':
    generate_all_figures()

