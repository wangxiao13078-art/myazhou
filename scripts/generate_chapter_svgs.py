#!/usr/bin/env python3
"""
按章节格式生成SVG图形

根据扫描文件夹里的章节结构：
- 专题一：有理数（数轴问题）
- 专题二：有理数的运算
- 专题三：代数式
- 专题四：整式的加减
- 专题五：一元一次方程
- 专题六：几何图形初步（线段、角度）
"""

import os
import math
from pathlib import Path

# 输出目录
OUTPUT_DIR = Path(__file__).parent.parent / "apps" / "miniprogram" / "images" / "svg"

def ensure_dir():
    """确保输出目录存在"""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ============== 基础图形生成函数 ==============

def generate_number_line(min_val=-5, max_val=5, points=None, width=400, height=80):
    """
    生成数轴SVG
    
    参数:
    - min_val: 数轴最小值
    - max_val: 数轴最大值
    - points: 标记点列表 [{'value': 数值, 'label': '标签', 'color': '颜色'}]
    - width, height: SVG尺寸
    """
    if points is None:
        points = []
    
    margin = 40
    line_y = height // 2
    range_val = max_val - min_val
    scale = (width - 2 * margin) / range_val
    
    def value_to_x(val):
        return margin + (val - min_val) * scale
    
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">\n'
    
    # 主轴线
    svg += f'  <line x1="{margin - 10}" y1="{line_y}" x2="{width - margin + 10}" y2="{line_y}" stroke="#333" stroke-width="2"/>\n'
    
    # 箭头
    svg += f'  <polygon points="{width - margin + 10},{line_y} {width - margin},{line_y - 5} {width - margin},{line_y + 5}" fill="#333"/>\n'
    
    # 刻度线和数字
    for i in range(min_val, max_val + 1):
        x = value_to_x(i)
        svg += f'  <line x1="{x}" y1="{line_y - 5}" x2="{x}" y2="{line_y + 5}" stroke="#333" stroke-width="1.5"/>\n'
        svg += f'  <text x="{x}" y="{line_y + 20}" font-family="Arial" font-size="12" text-anchor="middle">{i}</text>\n'
    
    # 原点O
    if min_val <= 0 <= max_val:
        origin_x = value_to_x(0)
        svg += f'  <text x="{origin_x}" y="{line_y + 32}" font-family="Arial" font-size="11" text-anchor="middle" fill="#666">O</text>\n'
    
    # 标记点
    for idx, point in enumerate(points):
        x = value_to_x(point['value'])
        color = point.get('color', '#2196F3')
        label = point.get('label', '')
        
        svg += f'  <circle cx="{x}" cy="{line_y}" r="4" fill="{color}"/>\n'
        if label:
            label_y = line_y - 12 if idx % 2 == 0 else line_y + 28
            svg += f'  <text x="{x}" y="{label_y}" font-family="Arial" font-size="13" text-anchor="middle" fill="{color}">{label}</text>\n'
    
    svg += '</svg>'
    return svg


def generate_segment(points, width=400, height=80):
    """
    生成线段图SVG
    
    参数:
    - points: 点列表 [{'name': 'A', 'position': 0-100, 'color': '颜色'}]
    """
    margin = 40
    line_y = height // 2
    line_length = width - 2 * margin
    
    def pos_to_x(pos):
        return margin + (pos / 100) * line_length
    
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">\n'
    
    # 主线段
    positions = [p['position'] for p in points]
    start_x = pos_to_x(min(positions))
    end_x = pos_to_x(max(positions))
    svg += f'  <line x1="{start_x}" y1="{line_y}" x2="{end_x}" y2="{line_y}" stroke="#333" stroke-width="2"/>\n'
    
    # 点和标签
    for idx, point in enumerate(points):
        x = pos_to_x(point['position'])
        color = point.get('color', '#333' if point['position'] in [0, 100] else '#2196F3')
        is_endpoint = point['position'] in [0, 100]
        
        svg += f'  <circle cx="{x}" cy="{line_y}" r="{4 if is_endpoint else 3}" fill="{color}"/>\n'
        svg += f'  <text x="{x}" y="{line_y + 22}" font-family="Arial" font-size="14" text-anchor="middle" fill="{color}">{point["name"]}</text>\n'
    
    svg += '</svg>'
    return svg


def generate_angle(vertex, rays, width=300, height=200, show_arc=True, arc_radius=30):
    """
    生成角度图SVG
    
    参数:
    - vertex: 顶点 {'x': x, 'y': y, 'label': 'O'}
    - rays: 射线列表 [{'angle': 角度, 'label': '标签', 'color': '颜色'}]
    """
    ray_length = 100
    
    def get_ray_end(angle_deg):
        angle_rad = math.radians(angle_deg)
        return {
            'x': vertex['x'] + ray_length * math.cos(angle_rad),
            'y': vertex['y'] - ray_length * math.sin(angle_rad)
        }
    
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">\n'
    
    # 顶点
    svg += f'  <circle cx="{vertex["x"]}" cy="{vertex["y"]}" r="4" fill="#333"/>\n'
    svg += f'  <text x="{vertex["x"]}" y="{vertex["y"] + 20}" font-family="Arial" font-size="14" text-anchor="middle">{vertex.get("label", "O")}</text>\n'
    
    # 射线
    for ray in rays:
        end = get_ray_end(ray['angle'])
        color = ray.get('color', '#333')
        
        svg += f'  <line x1="{vertex["x"]}" y1="{vertex["y"]}" x2="{end["x"]}" y2="{end["y"]}" stroke="{color}" stroke-width="2"/>\n'
        
        # 射线标签
        label_dist = ray_length + 15
        label_x = vertex['x'] + label_dist * math.cos(math.radians(ray['angle']))
        label_y = vertex['y'] - label_dist * math.sin(math.radians(ray['angle']))
        svg += f'  <text x="{label_x}" y="{label_y}" font-family="Arial" font-size="14" text-anchor="middle" fill="{color}">{ray.get("label", "")}</text>\n'
    
    # 角度弧线
    if show_arc and len(rays) >= 2:
        angles = sorted([r['angle'] for r in rays])
        start_angle_rad = -angles[1] * math.pi / 180
        end_angle_rad = -angles[0] * math.pi / 180
        
        start_x = vertex['x'] + arc_radius * math.cos(start_angle_rad)
        start_y = vertex['y'] + arc_radius * math.sin(start_angle_rad)
        end_x = vertex['x'] + arc_radius * math.cos(end_angle_rad)
        end_y = vertex['y'] + arc_radius * math.sin(end_angle_rad)
        
        large_arc = 1 if (angles[1] - angles[0]) > 180 else 0
        
        svg += f'  <path d="M {start_x} {start_y} A {arc_radius} {arc_radius} 0 {large_arc} 1 {end_x} {end_y}" fill="none" stroke="#2196F3" stroke-width="1.5"/>\n'
    
    svg += '</svg>'
    return svg


def generate_bisector(main_angle=120, labels=None, width=300, height=200):
    """
    生成角平分线图SVG
    """
    if labels is None:
        labels = {'vertex': 'O', 'rays': ['A', 'B'], 'bisectors': ['C']}
    
    vertex = {'x': 150, 'y': 150}
    ray_length = 100
    
    def get_ray_end(angle_deg):
        angle_rad = math.radians(angle_deg)
        return {
            'x': vertex['x'] + ray_length * math.cos(angle_rad),
            'y': vertex['y'] - ray_length * math.sin(angle_rad)
        }
    
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">\n'
    
    # 顶点
    svg += f'  <circle cx="{vertex["x"]}" cy="{vertex["y"]}" r="4" fill="#333"/>\n'
    svg += f'  <text x="{vertex["x"]}" y="{vertex["y"] + 20}" font-family="Arial" font-size="14" text-anchor="middle">{labels["vertex"]}</text>\n'
    
    # 主射线1 (0度)
    end1 = get_ray_end(0)
    svg += f'  <line x1="{vertex["x"]}" y1="{vertex["y"]}" x2="{end1["x"]}" y2="{end1["y"]}" stroke="#333" stroke-width="2"/>\n'
    svg += f'  <text x="{end1["x"] + 10}" y="{end1["y"]}" font-family="Arial" font-size="14">{labels["rays"][0]}</text>\n'
    
    # 主射线2 (main_angle度)
    end2 = get_ray_end(main_angle)
    svg += f'  <line x1="{vertex["x"]}" y1="{vertex["y"]}" x2="{end2["x"]}" y2="{end2["y"]}" stroke="#333" stroke-width="2"/>\n'
    svg += f'  <text x="{end2["x"] - 5}" y="{end2["y"] - 10}" font-family="Arial" font-size="14">{labels["rays"][1]}</text>\n'
    
    # 平分线
    bisector_angle = main_angle / 2
    end_b = get_ray_end(bisector_angle)
    svg += f'  <line x1="{vertex["x"]}" y1="{vertex["y"]}" x2="{end_b["x"]}" y2="{end_b["y"]}" stroke="#2196F3" stroke-width="2" stroke-dasharray="5,3"/>\n'
    svg += f'  <text x="{end_b["x"] + 5}" y="{end_b["y"] - 5}" font-family="Arial" font-size="14" fill="#2196F3">{labels["bisectors"][0]}</text>\n'
    
    # 角度弧
    arc_r = 30
    arc_end_x = vertex['x'] + arc_r * math.cos(math.radians(main_angle))
    arc_end_y = vertex['y'] - arc_r * math.sin(math.radians(main_angle))
    svg += f'  <path d="M {vertex["x"] + arc_r} {vertex["y"]} A {arc_r} {arc_r} 0 0 0 {arc_end_x} {arc_end_y}" fill="none" stroke="#666" stroke-width="1"/>\n'
    
    svg += '</svg>'
    return svg


def generate_circle_on_line(center=0, radius=1, min_val=-5, max_val=5, marked_angle=180, marked_label='A', width=400, height=120):
    """
    生成圆在数轴上滚动的图形
    """
    margin = 40
    line_y = height - 30
    range_val = max_val - min_val
    scale = (width - 2 * margin) / range_val
    scaled_radius = radius * scale
    
    def value_to_x(val):
        return margin + (val - min_val) * scale
    
    center_x = value_to_x(center)
    circle_y = line_y - scaled_radius
    
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">\n'
    
    # 数轴
    svg += f'  <line x1="{margin - 10}" y1="{line_y}" x2="{width - margin + 10}" y2="{line_y}" stroke="#333" stroke-width="2"/>\n'
    svg += f'  <polygon points="{width - margin + 10},{line_y} {width - margin},{line_y - 4} {width - margin},{line_y + 4}" fill="#333"/>\n'
    
    # 刻度
    for i in range(min_val, max_val + 1):
        x = value_to_x(i)
        svg += f'  <line x1="{x}" y1="{line_y - 4}" x2="{x}" y2="{line_y + 4}" stroke="#333" stroke-width="1.5"/>\n'
        svg += f'  <text x="{x}" y="{line_y + 18}" font-family="Arial" font-size="11" text-anchor="middle">{i}</text>\n'
    
    # 圆
    svg += f'  <circle cx="{center_x}" cy="{circle_y}" r="{scaled_radius}" fill="none" stroke="#2196F3" stroke-width="2"/>\n'
    
    # 圆上标记点
    marked_rad = math.radians(marked_angle)
    marked_x = center_x + scaled_radius * math.cos(marked_rad)
    marked_y = circle_y - scaled_radius * math.sin(marked_rad)
    svg += f'  <circle cx="{marked_x}" cy="{marked_y}" r="4" fill="#E91E63"/>\n'
    svg += f'  <text x="{marked_x}" y="{marked_y - 8}" font-family="Arial" font-size="12" text-anchor="middle" fill="#E91E63">{marked_label}</text>\n'
    
    svg += '</svg>'
    return svg


# ============== 按章节生成图形 ==============

def generate_chapter1_figures():
    """专题一：有理数 - 数轴问题"""
    figures = []
    
    # t1 数轴整点与动点问题
    figures.append(('t1_example', generate_number_line(-10, 10, [
        {'value': -8, 'label': 'A', 'color': '#E91E63'},
        {'value': 10, 'label': 'B', 'color': '#E91E63'}
    ])))
    
    # t1 训练：圆滚动
    figures.append(('t1_train_1', generate_circle_on_line(-1, 1, -5, 5, 180, 'A')))
    
    # t2 数轴规律探究
    figures.append(('t2_example', generate_number_line(-3, 6, [
        {'value': 0, 'label': 'O', 'color': '#333'},
        {'value': 1, 'label': 'A₁', 'color': '#2196F3'},
        {'value': 3, 'label': 'A₂', 'color': '#4CAF50'},
        {'value': 6, 'label': 'A₃', 'color': '#FF9800'}
    ])))
    
    # t5 绝对值几何意义
    figures.append(('t5_example', generate_number_line(-5, 5, [
        {'value': -3, 'label': 'a', 'color': '#2196F3'},
        {'value': 2, 'label': 'b', 'color': '#4CAF50'}
    ])))
    
    return figures


def generate_chapter6_figures():
    """专题六：几何图形初步 - 线段和角度"""
    figures = []
    
    # t32 线段中点 - 整体思想
    figures.append(('t32_example', generate_segment([
        {'name': 'A', 'position': 0},
        {'name': 'M', 'position': 25, 'color': '#2196F3'},
        {'name': 'C', 'position': 50, 'color': '#2196F3'},
        {'name': 'N', 'position': 75, 'color': '#2196F3'},
        {'name': 'B', 'position': 100}
    ])))
    
    figures.append(('t32_train_1', generate_segment([
        {'name': 'A', 'position': 0},
        {'name': 'M', 'position': 20, 'color': '#2196F3'},
        {'name': 'C', 'position': 40, 'color': '#2196F3'},
        {'name': 'N', 'position': 60, 'color': '#2196F3'},
        {'name': 'B', 'position': 100}
    ])))
    
    figures.append(('t32_train_2', generate_segment([
        {'name': 'A', 'position': 0},
        {'name': 'M', 'position': 30, 'color': '#2196F3'},
        {'name': 'C', 'position': 60, 'color': '#4CAF50'},
        {'name': 'N', 'position': 80, 'color': '#2196F3'},
        {'name': 'B', 'position': 100}
    ])))
    
    # t33 方程思想
    figures.append(('t33_example', generate_segment([
        {'name': 'A', 'position': 0},
        {'name': 'D', 'position': 20, 'color': '#E91E63'},
        {'name': 'E', 'position': 50, 'color': '#2196F3'},
        {'name': 'B', 'position': 80, 'color': '#333'},
        {'name': 'C', 'position': 100}
    ])))
    
    figures.append(('t33_train_1', generate_segment([
        {'name': 'A', 'position': 0},
        {'name': 'M', 'position': 30, 'color': '#2196F3'},
        {'name': 'C', 'position': 60, 'color': '#4CAF50'},
        {'name': 'N', 'position': 80, 'color': '#2196F3'},
        {'name': 'B', 'position': 100}
    ])))
    
    # t34 分类讨论
    figures.append(('t34_example', generate_segment([
        {'name': 'A', 'position': 0},
        {'name': 'C', 'position': 30, 'color': '#4CAF50'},
        {'name': 'P', 'position': 50, 'color': '#E91E63'},
        {'name': 'Q', 'position': 70, 'color': '#9C27B0'},
        {'name': 'B', 'position': 100}
    ])))
    
    # t35 数形结合
    figures.append(('t35_example', generate_number_line(-12, 22, [
        {'value': -10, 'label': 'A', 'color': '#2196F3'},
        {'value': -8, 'label': 'B', 'color': '#2196F3'},
        {'value': 16, 'label': 'C', 'color': '#4CAF50'},
        {'value': 20, 'label': 'D', 'color': '#4CAF50'}
    ], width=500)))
    
    # t36 角度计算 - 角平分线
    figures.append(('t36_example', generate_angle(
        {'x': 150, 'y': 150, 'label': 'O'},
        [
            {'angle': 0, 'label': 'A', 'color': '#333'},
            {'angle': 150, 'label': 'B', 'color': '#333'},
            {'angle': 90, 'label': 'D', 'color': '#2196F3'},
            {'angle': 45, 'label': 'C', 'color': '#4CAF50'},
            {'angle': 120, 'label': 'E', 'color': '#E91E63'}
        ]
    )))
    
    figures.append(('t36_train_1', generate_bisector(150, {'vertex': 'O', 'rays': ['A', 'B'], 'bisectors': ['C']})))
    
    # t37 旋转角度
    figures.append(('t37_example', generate_angle(
        {'x': 150, 'y': 150, 'label': 'O'},
        [
            {'angle': 0, 'label': 'A', 'color': '#333'},
            {'angle': 120, 'label': 'B', 'color': '#333'},
            {'angle': 60, 'label': 'M', 'color': '#2196F3'},
            {'angle': 90, 'label': 'N', 'color': '#E91E63'}
        ]
    )))
    
    return figures


def generate_all():
    """生成所有章节的图形"""
    ensure_dir()
    
    all_figures = []
    
    # 专题一
    all_figures.extend(generate_chapter1_figures())
    
    # 专题六
    all_figures.extend(generate_chapter6_figures())
    
    # 保存所有SVG
    for name, svg_content in all_figures:
        filepath = OUTPUT_DIR / f"{name}.svg"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        print(f"生成: {filepath.name}")
    
    print(f"\n共生成 {len(all_figures)} 个SVG图形")


if __name__ == '__main__':
    generate_all()

