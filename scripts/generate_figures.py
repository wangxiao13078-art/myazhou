#!/usr/bin/env python3
"""
自动生成习题SVG图形
为每个题目生成对应的数学图形
"""

import os
from pathlib import Path

# 输出目录
OUTPUT_DIR = Path("/Users/youyou/Downloads/M压轴/packages/svg_figures")

def create_svg(width, height, content):
    """创建SVG字符串"""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
    <style>
        text {{ font-family: -apple-system, sans-serif; }}
        .axis {{ stroke: #333; stroke-width: 2; }}
        .tick {{ stroke: #333; stroke-width: 1; }}
        .point {{ fill: #e74c3c; }}
        .label {{ font-size: 14px; fill: #333; }}
        .small-label {{ font-size: 12px; fill: #666; }}
    </style>
    {content}
</svg>'''

def number_line(start, end, points=None, labels=None, width=400, height=80):
    """
    生成数轴SVG
    start: 起始数值
    end: 结束数值
    points: 要标记的点列表 [(值, 标签), ...]
    labels: 是否显示刻度数字
    """
    margin = 40
    axis_y = height / 2
    range_val = end - start
    scale = (width - 2 * margin) / range_val
    
    content = []
    
    # 箭头定义
    content.append('''<defs>
        <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
            <path d="M0,0 L0,6 L9,3 z" fill="#333"/>
        </marker>
    </defs>''')
    
    # 主轴线
    content.append(f'<line x1="{margin}" y1="{axis_y}" x2="{width-margin+10}" y2="{axis_y}" class="axis" marker-end="url(#arrow)"/>')
    
    # 刻度和数字
    for i in range(start, end + 1):
        x = margin + (i - start) * scale
        content.append(f'<line x1="{x}" y1="{axis_y-5}" x2="{x}" y2="{axis_y+5}" class="tick"/>')
        if labels is None or labels:
            content.append(f'<text x="{x}" y="{axis_y+20}" text-anchor="middle" class="small-label">{i}</text>')
    
    # 标记点
    if points:
        for val, label in points:
            if start <= val <= end:
                x = margin + (val - start) * scale
                content.append(f'<circle cx="{x}" cy="{axis_y}" r="5" class="point"/>')
                if label:
                    content.append(f'<text x="{x}" y="{axis_y-12}" text-anchor="middle" class="label">{label}</text>')
    
    return create_svg(width, height, '\n    '.join(content))

def number_line_with_segment(start, end, seg_start, seg_end, seg_label="AB", width=400, height=80):
    """生成带线段的数轴"""
    margin = 40
    axis_y = height / 2
    range_val = end - start
    scale = (width - 2 * margin) / range_val
    
    content = []
    
    content.append('''<defs>
        <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
            <path d="M0,0 L0,6 L9,3 z" fill="#333"/>
        </marker>
    </defs>''')
    
    # 主轴线
    content.append(f'<line x1="{margin}" y1="{axis_y}" x2="{width-margin+10}" y2="{axis_y}" class="axis" marker-end="url(#arrow)"/>')
    
    # 刻度
    for i in range(start, end + 1):
        x = margin + (i - start) * scale
        content.append(f'<line x1="{x}" y1="{axis_y-5}" x2="{x}" y2="{axis_y+5}" class="tick"/>')
        content.append(f'<text x="{x}" y="{axis_y+20}" text-anchor="middle" class="small-label">{i}</text>')
    
    # 线段
    x1 = margin + (seg_start - start) * scale
    x2 = margin + (seg_end - start) * scale
    content.append(f'<line x1="{x1}" y1="{axis_y-15}" x2="{x2}" y2="{axis_y-15}" stroke="#667eea" stroke-width="3"/>')
    content.append(f'<circle cx="{x1}" cy="{axis_y-15}" r="4" fill="#667eea"/>')
    content.append(f'<circle cx="{x2}" cy="{axis_y-15}" r="4" fill="#667eea"/>')
    content.append(f'<text x="{x1}" y="{axis_y-25}" text-anchor="middle" class="label">{seg_label[0]}</text>')
    content.append(f'<text x="{x2}" y="{axis_y-25}" text-anchor="middle" class="label">{seg_label[1] if len(seg_label) > 1 else "B"}</text>')
    
    return create_svg(width, height, '\n    '.join(content))

def triangle_on_number_line(width=400, height=120):
    """生成数轴上的等边三角形"""
    margin = 40
    axis_y = height - 30
    scale = 50  # 每单位长度的像素
    
    content = []
    
    content.append('''<defs>
        <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
            <path d="M0,0 L0,6 L9,3 z" fill="#333"/>
        </marker>
    </defs>''')
    
    # 数轴
    content.append(f'<line x1="{margin}" y1="{axis_y}" x2="{width-margin}" y2="{axis_y}" class="axis" marker-end="url(#arrow)"/>')
    
    # 刻度 -2 到 5
    for i in range(-2, 6):
        x = margin + 60 + (i + 2) * scale
        content.append(f'<line x1="{x}" y1="{axis_y-4}" x2="{x}" y2="{axis_y+4}" class="tick"/>')
        content.append(f'<text x="{x}" y="{axis_y+18}" text-anchor="middle" class="small-label">{i}</text>')
    
    # 等边三角形 ABC，C在-1，A在0，B在顶点
    c_x = margin + 60 + 1 * scale  # -1的位置
    a_x = margin + 60 + 2 * scale  # 0的位置
    side = scale  # 边长
    b_x = (c_x + a_x) / 2
    b_y = axis_y - side * 0.866  # 等边三角形高度
    
    content.append(f'<polygon points="{a_x},{axis_y} {c_x},{axis_y} {b_x},{b_y}" fill="none" stroke="#667eea" stroke-width="2"/>')
    content.append(f'<text x="{a_x+8}" y="{axis_y-5}" class="label">A</text>')
    content.append(f'<text x="{c_x-12}" y="{axis_y-5}" class="label">C</text>')
    content.append(f'<text x="{b_x}" y="{b_y-8}" text-anchor="middle" class="label">B</text>')
    
    return create_svg(width, height, '\n    '.join(content))

def number_line_with_letters(letters_pos, width=400, height=80):
    """
    生成带字母标记的数轴
    letters_pos: [(字母, 位置比例0-1), ...]
    """
    margin = 40
    axis_y = height / 2
    line_length = width - 2 * margin
    
    content = []
    
    content.append('''<defs>
        <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
            <path d="M0,0 L0,6 L9,3 z" fill="#333"/>
        </marker>
    </defs>''')
    
    # 主轴线（两端都有箭头）
    content.append(f'<line x1="{margin-10}" y1="{axis_y}" x2="{width-margin+10}" y2="{axis_y}" class="axis" marker-end="url(#arrow)"/>')
    
    # 字母标记
    for letter, pos in letters_pos:
        x = margin + pos * line_length
        content.append(f'<line x1="{x}" y1="{axis_y-5}" x2="{x}" y2="{axis_y+5}" class="tick"/>')
        content.append(f'<text x="{x}" y="{axis_y+20}" text-anchor="middle" class="label">{letter}</text>')
    
    return create_svg(width, height, '\n    '.join(content))

def coordinate_system(x_range, y_range, points=None, width=300, height=300):
    """生成坐标系"""
    margin = 40
    center_x = width / 2
    center_y = height / 2
    
    x_min, x_max = x_range
    y_min, y_max = y_range
    scale_x = (width - 2 * margin) / (x_max - x_min)
    scale_y = (height - 2 * margin) / (y_max - y_min)
    
    content = []
    
    content.append('''<defs>
        <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
            <path d="M0,0 L0,6 L9,3 z" fill="#333"/>
        </marker>
    </defs>''')
    
    # X轴
    content.append(f'<line x1="{margin}" y1="{center_y}" x2="{width-margin+10}" y2="{center_y}" class="axis" marker-end="url(#arrow)"/>')
    content.append(f'<text x="{width-margin+5}" y="{center_y-10}" class="label">x</text>')
    
    # Y轴
    content.append(f'<line x1="{center_x}" y1="{height-margin}" x2="{center_x}" y2="{margin-10}" class="axis" marker-end="url(#arrow)"/>')
    content.append(f'<text x="{center_x+15}" y="{margin}" class="label">y</text>')
    
    # 原点
    content.append(f'<text x="{center_x-10}" y="{center_y+15}" class="small-label">O</text>')
    
    # 刻度
    for i in range(x_min, x_max + 1):
        if i == 0: continue
        x = center_x + i * scale_x
        content.append(f'<line x1="{x}" y1="{center_y-3}" x2="{x}" y2="{center_y+3}" class="tick"/>')
        content.append(f'<text x="{x}" y="{center_y+15}" text-anchor="middle" class="small-label" font-size="10">{i}</text>')
    
    for i in range(y_min, y_max + 1):
        if i == 0: continue
        y = center_y - i * scale_y
        content.append(f'<line x1="{center_x-3}" y1="{y}" x2="{center_x+3}" y2="{y}" class="tick"/>')
        content.append(f'<text x="{center_x-15}" y="{y+4}" text-anchor="middle" class="small-label" font-size="10">{i}</text>')
    
    # 点
    if points:
        for label, px, py in points:
            x = center_x + px * scale_x
            y = center_y - py * scale_y
            content.append(f'<circle cx="{x}" cy="{y}" r="4" class="point"/>')
            content.append(f'<text x="{x+10}" y="{y-5}" class="label">{label}</text>')
    
    return create_svg(width, height, '\n    '.join(content))

# 定义每个题目需要的图形
FIGURES = {
    't1': {
        'name': '数轴动点问题',
        'figures': [
            ('numberline_t1_1', lambda: number_line(-5, 15, [(10, 'A'), (-2, 'B')], width=450)),
            ('numberline_t1_2', lambda: number_line_with_segment(-5, 15, -2, 10, 'AB', width=450)),
        ]
    },
    't2': {
        'name': '数轴规律探究',
        'figures': [
            ('triangle_t2', lambda: triangle_on_number_line()),
            ('numberline_t2', lambda: number_line(-2, 5, [(-1, 'C'), (0, 'A'), (1, '')])),
        ]
    },
    't3': {
        'name': '比较有理数大小',
        'figures': [
            ('numberline_t3', lambda: number_line_with_letters([('a', 0.15), ('b', 0.35), ('0', 0.5), ('1', 0.65)])),
        ]
    },
    't4': {
        'name': '绝对值的性质',
        'figures': [
            ('numberline_t4', lambda: number_line(-5, 5, [(-3, 'a'), (2, 'b')])),
        ]
    },
    't5': {
        'name': '几何意义的运用',
        'figures': [
            ('numberline_t5', lambda: number_line(-4, 4, [(1, ''), (-2, '')])),
        ]
    },
}

def main():
    print("=" * 60)
    print("🎨 自动生成习题SVG图形")
    print("=" * 60)
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    total = 0
    for problem_id, data in FIGURES.items():
        print(f"\n📚 {problem_id}: {data['name']}")
        for filename, generator in data['figures']:
            svg_content = generator()
            output_path = OUTPUT_DIR / f"{filename}.svg"
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(svg_content)
            print(f"   ✅ {output_path.name}")
            total += 1
    
    print(f"\n{'=' * 60}")
    print(f"✅ 生成完成！共 {total} 个SVG图形")
    print(f"📁 输出目录: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()





