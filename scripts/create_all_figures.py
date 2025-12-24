#!/usr/bin/env python3
"""
为所有习题创建SVG图形
"""

from pathlib import Path

OUTPUT_DIR = Path("/Users/youyou/Downloads/M压轴/packages/svg_figures")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def svg_template(width, height, content):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
    <style>
        text {{ font-family: -apple-system, 'Helvetica Neue', sans-serif; }}
        .axis {{ stroke: #333; stroke-width: 2; fill: none; }}
        .tick {{ stroke: #333; stroke-width: 1.5; }}
        .point {{ fill: #e74c3c; }}
        .point-blue {{ fill: #667eea; }}
        .label {{ font-size: 14px; fill: #333; font-weight: 500; }}
        .small {{ font-size: 12px; fill: #666; }}
        .shape {{ stroke: #667eea; stroke-width: 2; fill: none; }}
        .segment {{ stroke: #667eea; stroke-width: 3; }}
    </style>
    <defs>
        <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
            <path d="M0,0 L0,6 L9,3 z" fill="#333"/>
        </marker>
    </defs>
    {content}
</svg>'''

# ============ 数轴生成函数 ============

def create_numberline(filename, start, end, points=None, width=400, height=80):
    """创建数轴 points: [(value, label, color), ...]"""
    margin = 40
    axis_y = height / 2
    scale = (width - 2 * margin) / (end - start)
    
    content = []
    # 主轴
    content.append(f'<line x1="{margin}" y1="{axis_y}" x2="{width-margin+10}" y2="{axis_y}" class="axis" marker-end="url(#arrow)"/>')
    
    # 刻度
    for i in range(start, end + 1):
        x = margin + (i - start) * scale
        content.append(f'<line x1="{x}" y1="{axis_y-5}" x2="{x}" y2="{axis_y+5}" class="tick"/>')
        content.append(f'<text x="{x}" y="{axis_y+20}" text-anchor="middle" class="small">{i}</text>')
    
    # 点
    if points:
        for val, label, color in points:
            x = margin + (val - start) * scale
            color_class = "point-blue" if color == "blue" else "point"
            content.append(f'<circle cx="{x}" cy="{axis_y}" r="5" class="{color_class}"/>')
            if label:
                content.append(f'<text x="{x}" y="{axis_y-12}" text-anchor="middle" class="label">{label}</text>')
    
    svg = svg_template(width, height, '\n    '.join(content))
    (OUTPUT_DIR / filename).write_text(svg, encoding='utf-8')
    print(f"  ✅ {filename}")

def create_numberline_letters(filename, letters, width=400, height=80):
    """创建带字母的数轴 letters: [(position_ratio, label), ...]"""
    margin = 40
    axis_y = height / 2
    line_len = width - 2 * margin
    
    content = []
    content.append(f'<line x1="{margin-10}" y1="{axis_y}" x2="{width-margin+10}" y2="{axis_y}" class="axis" marker-end="url(#arrow)"/>')
    
    for pos, label in letters:
        x = margin + pos * line_len
        content.append(f'<line x1="{x}" y1="{axis_y-5}" x2="{x}" y2="{axis_y+5}" class="tick"/>')
        content.append(f'<text x="{x}" y="{axis_y+20}" text-anchor="middle" class="label">{label}</text>')
    
    svg = svg_template(width, height, '\n    '.join(content))
    (OUTPUT_DIR / filename).write_text(svg, encoding='utf-8')
    print(f"  ✅ {filename}")

def create_numberline_segment(filename, start, end, seg_points, width=450, height=90):
    """创建带线段的数轴 seg_points: [(value, label), ...]"""
    margin = 40
    axis_y = height - 30
    scale = (width - 2 * margin) / (end - start)
    
    content = []
    content.append(f'<line x1="{margin}" y1="{axis_y}" x2="{width-margin+10}" y2="{axis_y}" class="axis" marker-end="url(#arrow)"/>')
    
    for i in range(start, end + 1):
        x = margin + (i - start) * scale
        content.append(f'<line x1="{x}" y1="{axis_y-4}" x2="{x}" y2="{axis_y+4}" class="tick"/>')
        content.append(f'<text x="{x}" y="{axis_y+18}" text-anchor="middle" class="small">{i}</text>')
    
    # 点和连线
    for i, (val, label) in enumerate(seg_points):
        x = margin + (val - start) * scale
        content.append(f'<circle cx="{x}" cy="{axis_y-25}" r="4" class="point-blue"/>')
        content.append(f'<text x="{x}" y="{axis_y-35}" text-anchor="middle" class="label">{label}</text>')
    
    if len(seg_points) >= 2:
        x1 = margin + (seg_points[0][0] - start) * scale
        x2 = margin + (seg_points[1][0] - start) * scale
        content.append(f'<line x1="{x1}" y1="{axis_y-25}" x2="{x2}" y2="{axis_y-25}" class="segment"/>')
    
    svg = svg_template(width, height, '\n    '.join(content))
    (OUTPUT_DIR / filename).write_text(svg, encoding='utf-8')
    print(f"  ✅ {filename}")

def create_triangle_on_axis(filename, width=400, height=120):
    """数轴上的等边三角形"""
    margin = 40
    axis_y = height - 30
    scale = 40
    
    content = []
    content.append(f'<line x1="{margin}" y1="{axis_y}" x2="{width-margin}" y2="{axis_y}" class="axis" marker-end="url(#arrow)"/>')
    
    for i in range(-2, 6):
        x = margin + 50 + (i + 2) * scale
        content.append(f'<line x1="{x}" y1="{axis_y-4}" x2="{x}" y2="{axis_y+4}" class="tick"/>')
        content.append(f'<text x="{x}" y="{axis_y+18}" text-anchor="middle" class="small">{i}</text>')
    
    # 三角形 C(-1), A(0), B(顶点)
    c_x = margin + 50 + 1 * scale
    a_x = margin + 50 + 2 * scale
    b_x = (c_x + a_x) / 2
    b_y = axis_y - scale * 0.866
    
    content.append(f'<polygon points="{a_x},{axis_y} {c_x},{axis_y} {b_x},{b_y}" class="shape"/>')
    content.append(f'<text x="{a_x+8}" y="{axis_y-5}" class="label">A</text>')
    content.append(f'<text x="{c_x-12}" y="{axis_y-5}" class="label">C</text>')
    content.append(f'<text x="{b_x}" y="{b_y-8}" text-anchor="middle" class="label">B</text>')
    
    svg = svg_template(width, height, '\n    '.join(content))
    (OUTPUT_DIR / filename).write_text(svg, encoding='utf-8')
    print(f"  ✅ {filename}")

def create_three_points_axis(filename, width=400, height=80):
    """A、B、C三点在数轴上（用于绝对值几何意义问题）"""
    margin = 40
    axis_y = height / 2
    
    content = []
    content.append(f'<line x1="{margin-10}" y1="{axis_y}" x2="{width-margin+10}" y2="{axis_y}" class="axis" marker-end="url(#arrow)"/>')
    
    # A, O, P, B 四个点
    points = [
        (0.15, 'A', 'red'),
        (0.4, 'O', 'black'),
        (0.55, 'P', 'blue'),
        (0.85, 'B', 'red'),
    ]
    
    line_len = width - 2 * margin
    for pos, label, color in points:
        x = margin + pos * line_len
        content.append(f'<line x1="{x}" y1="{axis_y-5}" x2="{x}" y2="{axis_y+5}" class="tick"/>')
        if label == 'O':
            content.append(f'<text x="{x}" y="{axis_y+20}" text-anchor="middle" class="small">0</text>')
        content.append(f'<text x="{x}" y="{axis_y-10}" text-anchor="middle" class="label">{label}</text>')
    
    svg = svg_template(width, height, '\n    '.join(content))
    (OUTPUT_DIR / filename).write_text(svg, encoding='utf-8')
    print(f"  ✅ {filename}")

def create_abs_distance(filename, width=400, height=100):
    """|x-1|+|x+2|的几何意义"""
    margin = 40
    axis_y = height / 2 + 10
    scale = 50
    
    content = []
    content.append(f'<line x1="{margin}" y1="{axis_y}" x2="{width-margin}" y2="{axis_y}" class="axis" marker-end="url(#arrow)"/>')
    
    for i in range(-3, 4):
        x = margin + 60 + (i + 3) * scale
        content.append(f'<line x1="{x}" y1="{axis_y-4}" x2="{x}" y2="{axis_y+4}" class="tick"/>')
        content.append(f'<text x="{x}" y="{axis_y+18}" text-anchor="middle" class="small">{i}</text>')
    
    # 标记-2和1两个关键点
    x_neg2 = margin + 60 + 1 * scale
    x_1 = margin + 60 + 4 * scale
    content.append(f'<circle cx="{x_neg2}" cy="{axis_y}" r="5" class="point"/>')
    content.append(f'<circle cx="{x_1}" cy="{axis_y}" r="5" class="point"/>')
    content.append(f'<text x="{x_neg2}" y="{axis_y-12}" text-anchor="middle" class="label">-2</text>')
    content.append(f'<text x="{x_1}" y="{axis_y-12}" text-anchor="middle" class="label">1</text>')
    
    # 距离线段
    content.append(f'<line x1="{x_neg2}" y1="{axis_y-25}" x2="{x_1}" y2="{axis_y-25}" class="segment"/>')
    content.append(f'<text x="{(x_neg2+x_1)/2}" y="{axis_y-32}" text-anchor="middle" class="small">距离=3</text>')
    
    svg = svg_template(width, height, '\n    '.join(content))
    (OUTPUT_DIR / filename).write_text(svg, encoding='utf-8')
    print(f"  ✅ {filename}")

# ============ 主函数 ============

def main():
    print("=" * 60)
    print("🎨 生成所有习题SVG图形")
    print("=" * 60)
    
    # t1: 数轴动点问题
    print("\n📚 t1: 数轴动点问题")
    create_numberline_segment("t1_train_1.svg", -5, 15, [(-2, 'B'), (10, 'A')], width=500)
    
    # t2: 数轴规律探究
    print("\n📚 t2: 数轴规律探究")
    create_triangle_on_axis("t2_train_1.svg")
    
    # t3: 比较有理数大小
    print("\n📚 t3: 比较有理数大小")
    create_numberline_letters("t3_train_1.svg", [(0.1, 'a'), (0.3, 'b'), (0.5, '0'), (0.7, '1')])
    
    # t4: 绝对值的性质（文字题为主，可选图）
    print("\n📚 t4: 绝对值性质")
    create_numberline("t4_train_1.svg", -5, 5, [(-3, 'a', 'red'), (2, 'b', 'red')])
    
    # t5: 几何意义的运用
    print("\n📚 t5: 几何意义运用")
    create_abs_distance("t5_train_1.svg")
    create_three_points_axis("t5_train_2.svg")
    
    # t6-t7: 新定义问题、实际应用（文字题）
    print("\n📚 t6-t7: 文字题（无需图形）")
    
    # t8-t11: 有理数运算（文字题为主）
    print("\n📚 t8-t11: 有理数运算（无需图形）")
    
    # t12: 数轴折叠问题
    print("\n📚 t12: 数轴折叠")
    create_numberline_segment("t12_train_1.svg", -5, 10, [(2, 'A'), (6, 'B')], width=450)
    
    # t13: 动点问题
    print("\n📚 t13: 动点问题")
    create_numberline_segment("t13_train_1.svg", -10, 10, [(-6, 'A'), (4, 'B')], width=500)
    
    print("\n" + "=" * 60)
    print(f"✅ 完成！图形保存在: {OUTPUT_DIR}")
    
    # 生成图形映射配置
    mapping = {
        't1': ['t1_train_1.svg'],
        't2': ['t2_train_1.svg'],
        't3': ['t3_train_1.svg'],
        't4': ['t4_train_1.svg'],
        't5': ['t5_train_1.svg', 't5_train_2.svg'],
        't12': ['t12_train_1.svg'],
        't13': ['t13_train_1.svg'],
    }
    
    print("\n📋 图形映射配置:")
    for tid, files in mapping.items():
        print(f"   {tid}: {files}")

if __name__ == "__main__":
    main()





