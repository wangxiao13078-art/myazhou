#!/usr/bin/env python3
"""
为所有练习题生成SVG图形
根据PDF内容分析每道题需要的图形
"""

from pathlib import Path
import math

OUTPUT_DIR = Path("/Users/youyou/Downloads/M压轴/packages/svg_figures")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def svg(width, height, content):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<style>
text {{ font-family: -apple-system, 'Helvetica Neue', sans-serif; }}
.axis {{ stroke: #333; stroke-width: 2; fill: none; }}
.tick {{ stroke: #333; stroke-width: 1.5; }}
.point {{ fill: #e74c3c; }}
.point-blue {{ fill: #667eea; }}
.point-green {{ fill: #10B981; }}
.label {{ font-size: 14px; fill: #333; font-weight: 500; }}
.small {{ font-size: 12px; fill: #666; }}
.title {{ font-size: 16px; fill: #333; font-weight: 600; }}
.shape {{ stroke: #667eea; stroke-width: 2; fill: none; }}
.shape-fill {{ stroke: #667eea; stroke-width: 2; fill: rgba(102,126,234,0.1); }}
.segment {{ stroke: #667eea; stroke-width: 3; }}
.segment-red {{ stroke: #e74c3c; stroke-width: 2; stroke-dasharray: 5,3; }}
.arrow {{ fill: #333; }}
.table-line {{ stroke: #333; stroke-width: 1; }}
.table-header {{ fill: #f0f4ff; }}
</style>
<defs>
<marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
<path d="M0,0 L0,6 L9,3 z" class="arrow"/>
</marker>
</defs>
{content}
</svg>'''

def save(filename, content):
    (OUTPUT_DIR / filename).write_text(content, encoding='utf-8')
    print(f"  ✅ {filename}")

# ========== 数轴类图形 ==========

def numberline_abc(a_pos, b_pos, c_pos=None, width=450, height=80):
    """带A、B、C三点的数轴"""
    m, y = 40, height / 2
    L = width - 2 * m
    c = [f'<line x1="{m-10}" y1="{y}" x2="{width-m+10}" y2="{y}" class="axis" marker-end="url(#arrow)"/>']
    
    # 原点
    c.append(f'<line x1="{width/2}" y1="{y-5}" x2="{width/2}" y2="{y+5}" class="tick"/>')
    c.append(f'<text x="{width/2}" y="{y+20}" text-anchor="middle" class="small">0</text>')
    
    # 点A、B、C
    points = [('A', a_pos, 'point'), ('B', b_pos, 'point-blue')]
    if c_pos is not None:
        points.append(('C', c_pos, 'point-green'))
    
    for label, pos, color in points:
        x = m + pos * L
        c.append(f'<circle cx="{x}" cy="{y}" r="5" class="{color}"/>')
        c.append(f'<text x="{x}" y="{y-12}" text-anchor="middle" class="label">{label}</text>')
    
    return svg(width, height, '\n'.join(c))

def numberline_aob(width=400, height=80):
    """数轴上A、O、B三点（动点问题）"""
    m, y = 40, height / 2
    L = width - 2 * m
    c = [f'<line x1="{m-10}" y1="{y}" x2="{width-m+10}" y2="{y}" class="axis" marker-end="url(#arrow)"/>']
    
    # 点A(-2)、O(0)、B(4)
    pts = [('A', 0.2, '-2', 'point'), ('O', 0.45, '0', 'point-blue'), ('B', 0.8, '4', 'point')]
    for label, pos, val, color in pts:
        x = m + pos * L
        c.append(f'<circle cx="{x}" cy="{y}" r="5" class="{color}"/>')
        c.append(f'<text x="{x}" y="{y-12}" text-anchor="middle" class="label">{label}</text>')
        c.append(f'<text x="{x}" y="{y+20}" text-anchor="middle" class="small">{val}</text>')
    
    # 挡板标记
    ox = m + 0.45 * L
    c.append(f'<rect x="{ox-3}" y="{y-15}" width="6" height="30" fill="#fbbf24" stroke="#f59e0b"/>')
    
    return svg(width, height, '\n'.join(c))

def numberline_fold_abc(width=450, height=100):
    """数轴折叠：A、B、C三点"""
    m, y = 40, height - 30
    s = 35
    c = [f'<line x1="{m}" y1="{y}" x2="{width-m}" y2="{y}" class="axis" marker-end="url(#arrow)"/>']
    
    # 刻度
    for i in range(-2, 8):
        x = m + 30 + (i + 2) * s
        c.append(f'<line x1="{x}" y1="{y-4}" x2="{x}" y2="{y+4}" class="tick"/>')
        if i in [-2, 0, 5]:
            c.append(f'<text x="{x}" y="{y+18}" text-anchor="middle" class="small">{i}</text>')
    
    # 点 A(0)、B(5)、C(-2折叠后)
    pts = [(2, 'A', 'point'), (7, 'B', 'point-blue'), (4, 'C', 'point-green')]
    for idx, (label, color) in [(p[0], (p[1], p[2])) for p in pts]:
        x = m + 30 + (idx) * s
        c.append(f'<circle cx="{x}" cy="{y}" r="5" class="{color}"/>')
        c.append(f'<text x="{x}" y="{y-12}" text-anchor="middle" class="label">{label}</text>')
    
    return svg(width, height, '\n'.join(c))

def numberline_paper_fold(width=500, height=120):
    """纸面上的数轴折叠"""
    m, y = 40, height - 40
    s = 30
    c = []
    
    # 纸面背景
    c.append(f'<rect x="{m-10}" y="{y-50}" width="{width-2*m+20}" height="70" fill="#fef3c7" stroke="#fbbf24" rx="5"/>')
    
    # 数轴
    c.append(f'<line x1="{m}" y1="{y}" x2="{width-m}" y2="{y}" class="axis" marker-end="url(#arrow)"/>')
    
    # 刻度 -6 到 6
    for i in range(-6, 7):
        x = m + 20 + (i + 6) * s
        c.append(f'<line x1="{x}" y1="{y-4}" x2="{x}" y2="{y+4}" class="tick"/>')
        c.append(f'<text x="{x}" y="{y+18}" text-anchor="middle" class="small">{i}</text>')
    
    # 折叠线
    fold_x = m + 20 + 8 * s
    c.append(f'<line x1="{fold_x}" y1="{y-50}" x2="{fold_x}" y2="{y+25}" class="segment-red"/>')
    c.append(f'<text x="{fold_x}" y="{y-55}" text-anchor="middle" class="small" fill="#e74c3c">折痕</text>')
    
    return svg(width, height, '\n'.join(c))

def numberline_multi_points(points, start=-5, end=5, width=450, height=80):
    """多点数轴 points: [(val, label), ...]"""
    m, y = 40, height / 2
    scale = (width - 2*m) / (end - start)
    c = [f'<line x1="{m}" y1="{y}" x2="{width-m+10}" y2="{y}" class="axis" marker-end="url(#arrow)"/>']
    
    for i in range(start, end + 1):
        x = m + (i - start) * scale
        c.append(f'<line x1="{x}" y1="{y-4}" x2="{x}" y2="{y+4}" class="tick"/>')
        c.append(f'<text x="{x}" y="{y+18}" text-anchor="middle" class="small">{i}</text>')
    
    colors = ['point', 'point-blue', 'point-green']
    for idx, (val, label) in enumerate(points):
        x = m + (val - start) * scale
        c.append(f'<circle cx="{x}" cy="{y}" r="5" class="{colors[idx % 3]}"/>')
        c.append(f'<text x="{x}" y="{y-12}" text-anchor="middle" class="label">{label}</text>')
    
    return svg(width, height, '\n'.join(c))

# ========== 表格类图形 ==========

def table_weekdays(width=420, height=160):
    """星期一到星期日的表格"""
    c = []
    cols = ['星期', '一', '二', '三', '四', '五', '六', '日']
    row2 = ['增减', '+10', '-12', '-4', '+8', '-1', '+6', '0']
    
    col_w = 50
    row_h = 35
    x0, y0 = 20, 20
    
    # 表头背景
    c.append(f'<rect x="{x0}" y="{y0}" width="{col_w*8}" height="{row_h}" class="table-header"/>')
    
    # 表格线
    for i in range(3):
        y = y0 + i * row_h
        c.append(f'<line x1="{x0}" y1="{y}" x2="{x0+col_w*8}" y2="{y}" class="table-line"/>')
    c.append(f'<line x1="{x0}" y1="{y0+row_h*2}" x2="{x0+col_w*8}" y2="{y0+row_h*2}" class="table-line"/>')
    
    for i in range(9):
        x = x0 + i * col_w
        c.append(f'<line x1="{x}" y1="{y0}" x2="{x}" y2="{y0+row_h*2}" class="table-line"/>')
    
    # 表头文字
    for i, text in enumerate(cols):
        x = x0 + i * col_w + col_w/2
        c.append(f'<text x="{x}" y="{y0+row_h/2+5}" text-anchor="middle" class="small">{text}</text>')
    
    # 数据行
    for i, text in enumerate(row2):
        x = x0 + i * col_w + col_w/2
        color = '#10B981' if '+' in text else ('#e74c3c' if '-' in text else '#333')
        c.append(f'<text x="{x}" y="{y0+row_h*1.5+5}" text-anchor="middle" class="small" fill="{color}">{text}</text>')
    
    return svg(width, height, '\n'.join(c))

def table_production(width=350, height=140):
    """产量对比表格"""
    c = []
    cols = ['日期', '计划', '实际', '差额']
    data = [
        ['周一', '180', '175', '-5'],
        ['周二', '180', '186', '+6'],
    ]
    
    col_w = 80
    row_h = 35
    x0, y0 = 20, 15
    
    # 表头背景
    c.append(f'<rect x="{x0}" y="{y0}" width="{col_w*4}" height="{row_h}" class="table-header"/>')
    
    # 表格线
    for i in range(len(data) + 2):
        y = y0 + i * row_h
        c.append(f'<line x1="{x0}" y1="{y}" x2="{x0+col_w*4}" y2="{y}" class="table-line"/>')
    
    for i in range(5):
        x = x0 + i * col_w
        c.append(f'<line x1="{x}" y1="{y0}" x2="{x}" y2="{y0+row_h*(len(data)+1)}" class="table-line"/>')
    
    # 表头
    for i, text in enumerate(cols):
        x = x0 + i * col_w + col_w/2
        c.append(f'<text x="{x}" y="{y0+row_h/2+5}" text-anchor="middle" class="label">{text}</text>')
    
    # 数据
    for row_idx, row in enumerate(data):
        for col_idx, text in enumerate(row):
            x = x0 + col_idx * col_w + col_w/2
            y = y0 + (row_idx + 1) * row_h + row_h/2 + 5
            c.append(f'<text x="{x}" y="{y}" text-anchor="middle" class="small">{text}</text>')
    
    return svg(width, height, '\n'.join(c))

# ========== 几何图形 ==========

def triangle_rotate(width=400, height=150):
    """三角形翻转示意图"""
    c = []
    m, y = 40, height - 40
    s = 40
    
    # 数轴
    c.append(f'<line x1="{m}" y1="{y}" x2="{width-m}" y2="{y}" class="axis" marker-end="url(#arrow)"/>')
    
    for i in range(-2, 6):
        x = m + 40 + (i + 2) * s
        c.append(f'<line x1="{x}" y1="{y-4}" x2="{x}" y2="{y+4}" class="tick"/>')
        c.append(f'<text x="{x}" y="{y+18}" text-anchor="middle" class="small">{i}</text>')
    
    # 原始三角形 (虚线)
    c_x = m + 40 + 1 * s  # -1
    a_x = m + 40 + 2 * s  # 0
    b_x = (c_x + a_x) / 2
    b_y = y - s * 0.866
    c.append(f'<polygon points="{a_x},{y} {c_x},{y} {b_x},{b_y}" stroke="#999" stroke-width="1" stroke-dasharray="3,3" fill="none"/>')
    
    # 翻转后三角形 (实线)
    a2_x = m + 40 + 3 * s  # 1
    c2_x = m + 40 + 2 * s  # 0
    b2_x = (a2_x + c2_x) / 2
    c.append(f'<polygon points="{a2_x},{y} {c2_x},{y} {b2_x},{b_y}" class="shape-fill"/>')
    
    # 箭头
    c.append(f'<path d="M{a_x+10},{y-20} Q{(a_x+a2_x)/2},{y-50} {a2_x-10},{y-20}" stroke="#667eea" fill="none" marker-end="url(#arrow)"/>')
    c.append(f'<text x="{(a_x+a2_x)/2}" y="{y-55}" text-anchor="middle" class="small" fill="#667eea">翻转60°</text>')
    
    return svg(width, height, '\n'.join(c))

def distance_diagram(width=400, height=100):
    """距离示意图 |x-1|+|x-5|"""
    m, y = 40, height / 2 + 10
    scale = 40
    c = [f'<line x1="{m}" y1="{y}" x2="{width-m}" y2="{y}" class="axis" marker-end="url(#arrow)"/>']
    
    for i in range(-1, 8):
        x = m + 30 + (i + 1) * scale
        c.append(f'<line x1="{x}" y1="{y-4}" x2="{x}" y2="{y+4}" class="tick"/>')
        c.append(f'<text x="{x}" y="{y+18}" text-anchor="middle" class="small">{i}</text>')
    
    # 标记1和5
    x1 = m + 30 + 2 * scale
    x5 = m + 30 + 6 * scale
    c.append(f'<circle cx="{x1}" cy="{y}" r="5" class="point"/>')
    c.append(f'<circle cx="{x5}" cy="{y}" r="5" class="point-blue"/>')
    
    # 距离线
    c.append(f'<line x1="{x1}" y1="{y-20}" x2="{x5}" y2="{y-20}" class="segment"/>')
    c.append(f'<text x="{(x1+x5)/2}" y="{y-28}" text-anchor="middle" class="small">距离=4</text>')
    
    return svg(width, height, '\n'.join(c))

# ========== 主函数 ==========

def main():
    print("=" * 60)
    print("🎨 为所有练习题生成SVG图形")
    print("=" * 60)
    
    # t1: 数轴动点问题 - 练习题
    print("\n📚 t1 练习题")
    save("t1_train_1.svg", numberline_multi_points([(-2, 'B'), (10, 'A')], start=-5, end=15, width=500))
    save("t1_train_2.svg", numberline_multi_points([(0, 'P'), (5, 'Q')], start=-3, end=8))
    
    # t2: 规律探究 - 练习题
    print("\n📚 t2 练习题")
    save("t2_train_1.svg", triangle_rotate())
    
    # t3: 比较大小 - 练习题
    print("\n📚 t3 练习题")
    save("t3_train_1.svg", numberline_multi_points([(-3, 'a'), (0, '0'), (2, 'b')], start=-5, end=5))
    
    # t4: 绝对值性质 - 练习题
    print("\n📚 t4 练习题")
    save("t4_train_1.svg", numberline_multi_points([(-3, 'a'), (2, 'b')], start=-5, end=5))
    
    # t5: 几何意义 - 练习题 (第6、7题)
    print("\n📚 t5 练习题")
    save("t5_train_1.svg", numberline_abc(0.15, 0.75, 0.5))  # A、B、C三点
    save("t5_train_2.svg", distance_diagram())  # |x-1|+|x-5|+|x-m|
    
    # t7: 实际应用 - 练习题 (表格)
    print("\n📚 t7 练习题")
    save("t7_train_1.svg", table_weekdays())
    save("t7_train_2.svg", table_production())
    
    # t12: 折叠问题 - 练习题
    print("\n📚 t12 练习题")
    save("t12_train_1.svg", numberline_fold_abc())
    save("t12_train_2.svg", numberline_paper_fold())
    
    # t13: 动点问题 - 练习题
    print("\n📚 t13 练习题")
    save("t13_train_1.svg", numberline_aob())
    save("t13_train_2.svg", numberline_multi_points([(-2, 'A'), (0, 'O'), (4, 'B')], start=-5, end=6))
    
    # t19: 归纳猜想 - 练习题
    print("\n📚 t19 练习题")
    # 围棋图案
    save("t19_train_1.svg", pattern_go_pieces(3))
    
    # t22: 数轴化简绝对值 - 练习题
    print("\n📚 t22 练习题")
    save("t22_train_1.svg", numberline_multi_points([(-3, 'a'), (0, '0'), (1, 'c'), (3, 'b')], start=-5, end=5))
    
    # t23: 分类讨论 - 练习题
    print("\n📚 t23 练习题")
    save("t23_train_1.svg", numberline_multi_points([(-2, '-2'), (4, '4')], start=-4, end=6))
    
    # t27: 含绝对值方程 - 练习题
    print("\n📚 t27 练习题")
    save("t27_train_1.svg", numberline_multi_points([(-2, '-2'), (3, '3')], start=-5, end=5))
    
    print("\n" + "=" * 60)
    print("✅ 练习题SVG图形生成完成！")

def pattern_go_pieces(n, width=200, height=200):
    """围棋图案"""
    c = []
    cx, cy = width/2, height/2
    
    # 网格
    grid_size = 25
    for i in range(-2, 3):
        x = cx + i * grid_size
        c.append(f'<line x1="{x}" y1="{cy-2*grid_size}" x2="{x}" y2="{cy+2*grid_size}" stroke="#ccc" stroke-width="1"/>')
        y = cy + i * grid_size
        c.append(f'<line x1="{cx-2*grid_size}" y1="{y}" x2="{cx+2*grid_size}" y2="{y}" stroke="#ccc" stroke-width="1"/>')
    
    # 黑子 (中心n×n)
    for i in range(-n//2, n//2+1):
        for j in range(-n//2, n//2+1):
            if abs(i) <= n//2 and abs(j) <= n//2:
                x = cx + i * grid_size
                y = cy + j * grid_size
                c.append(f'<circle cx="{x}" cy="{y}" r="10" fill="#333"/>')
    
    # 白子 (外围)
    for i in range(-2, 3):
        for j in range(-2, 3):
            if abs(i) > n//2 or abs(j) > n//2:
                if abs(i) <= 2 and abs(j) <= 2:
                    x = cx + i * grid_size
                    y = cy + j * grid_size
                    c.append(f'<circle cx="{x}" cy="{y}" r="10" fill="white" stroke="#333"/>')
    
    c.append(f'<text x="{cx}" y="{height-15}" text-anchor="middle" class="small">图{n}</text>')
    
    return svg(width, height, '\n'.join(c))

if __name__ == "__main__":
    main()

