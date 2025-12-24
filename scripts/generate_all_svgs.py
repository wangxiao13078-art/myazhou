#!/usr/bin/env python3
"""
为所有题目生成SVG图形
"""

from pathlib import Path

OUTPUT_DIR = Path("/Users/youyou/Downloads/M压轴/packages/svg_figures")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def svg(width, height, content):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<style>
text {{ font-family: -apple-system, 'Helvetica Neue', sans-serif; }}
.axis {{ stroke: #333; stroke-width: 2; fill: none; }}
.tick {{ stroke: #333; stroke-width: 1.5; }}
.grid {{ stroke: #ddd; stroke-width: 0.5; }}
.point {{ fill: #e74c3c; }}
.point-blue {{ fill: #667eea; }}
.label {{ font-size: 14px; fill: #333; font-weight: 500; }}
.small {{ font-size: 12px; fill: #666; }}
.shape {{ stroke: #667eea; stroke-width: 2; fill: none; }}
.shape-fill {{ stroke: #667eea; stroke-width: 2; fill: rgba(102,126,234,0.1); }}
.segment {{ stroke: #667eea; stroke-width: 3; }}
.arrow {{ fill: #333; }}
</style>
<defs>
<marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
<path d="M0,0 L0,6 L9,3 z" class="arrow"/>
</marker>
<marker id="arrow-blue" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
<path d="M0,0 L0,6 L9,3 z" fill="#667eea"/>
</marker>
</defs>
{content}
</svg>'''

def save(filename, content):
    (OUTPUT_DIR / filename).write_text(content, encoding='utf-8')
    print(f"  ✅ {filename}")

# ========== 数轴类图形 ==========

def numberline(start, end, points=None, width=400, height=80):
    """基础数轴 points: [(val, label), ...]"""
    m = 40
    y = height / 2
    s = (width - 2*m) / (end - start)
    c = [f'<line x1="{m}" y1="{y}" x2="{width-m+10}" y2="{y}" class="axis" marker-end="url(#arrow)"/>']
    for i in range(start, end + 1):
        x = m + (i - start) * s
        c.append(f'<line x1="{x}" y1="{y-5}" x2="{x}" y2="{y+5}" class="tick"/>')
        c.append(f'<text x="{x}" y="{y+20}" text-anchor="middle" class="small">{i}</text>')
    if points:
        for val, label in points:
            x = m + (val - start) * s
            c.append(f'<circle cx="{x}" cy="{y}" r="5" class="point"/>')
            if label:
                c.append(f'<text x="{x}" y="{y-12}" text-anchor="middle" class="label">{label}</text>')
    return svg(width, height, '\n'.join(c))

def numberline_segment(start, end, pts, width=450, height=90):
    """带线段的数轴 pts: [(val, label), ...]"""
    m, y = 40, height - 30
    s = (width - 2*m) / (end - start)
    c = [f'<line x1="{m}" y1="{y}" x2="{width-m+10}" y2="{y}" class="axis" marker-end="url(#arrow)"/>']
    for i in range(start, end + 1):
        x = m + (i - start) * s
        c.append(f'<line x1="{x}" y1="{y-4}" x2="{x}" y2="{y+4}" class="tick"/>')
        c.append(f'<text x="{x}" y="{y+18}" text-anchor="middle" class="small">{i}</text>')
    for val, label in pts:
        x = m + (val - start) * s
        c.append(f'<circle cx="{x}" cy="{y-20}" r="4" class="point-blue"/>')
        c.append(f'<text x="{x}" y="{y-32}" text-anchor="middle" class="label">{label}</text>')
    if len(pts) >= 2:
        x1 = m + (pts[0][0] - start) * s
        x2 = m + (pts[1][0] - start) * s
        c.append(f'<line x1="{x1}" y1="{y-20}" x2="{x2}" y2="{y-20}" class="segment"/>')
    return svg(width, height, '\n'.join(c))

def numberline_letters(letters, width=400, height=80):
    """字母标记数轴 letters: [(pos_ratio, label), ...]"""
    m, y = 40, height / 2
    L = width - 2*m
    c = [f'<line x1="{m-10}" y1="{y}" x2="{width-m+10}" y2="{y}" class="axis" marker-end="url(#arrow)"/>']
    for pos, label in letters:
        x = m + pos * L
        c.append(f'<line x1="{x}" y1="{y-5}" x2="{x}" y2="{y+5}" class="tick"/>')
        c.append(f'<text x="{x}" y="{y+20}" text-anchor="middle" class="label">{label}</text>')
    return svg(width, height, '\n'.join(c))

def numberline_fold(width=400, height=100):
    """折叠数轴"""
    m, y = 40, height/2 + 10
    s = 30
    c = [f'<line x1="{m}" y1="{y}" x2="{width-m}" y2="{y}" class="axis" marker-end="url(#arrow)"/>']
    for i in range(-3, 8):
        x = m + 40 + (i+3) * s
        c.append(f'<line x1="{x}" y1="{y-4}" x2="{x}" y2="{y+4}" class="tick"/>')
        c.append(f'<text x="{x}" y="{y+18}" text-anchor="middle" class="small">{i}</text>')
    # 折叠标记
    x_a, x_b = m + 40 + 5*s, m + 40 + 9*s
    c.append(f'<circle cx="{x_a}" cy="{y}" r="5" class="point"/>')
    c.append(f'<circle cx="{x_b}" cy="{y}" r="5" class="point-blue"/>')
    c.append(f'<text x="{x_a}" y="{y-12}" text-anchor="middle" class="label">A</text>')
    c.append(f'<text x="{x_b}" y="{y-12}" text-anchor="middle" class="label">B</text>')
    # 折叠弧线
    mid = (x_a + x_b) / 2
    c.append(f'<path d="M{x_a},{y-8} Q{mid},{y-40} {x_b},{y-8}" class="shape" fill="none"/>')
    c.append(f'<text x="{mid}" y="{y-45}" text-anchor="middle" class="small">折叠</text>')
    return svg(width, height, '\n'.join(c))

# ========== 几何图形 ==========

def triangle_on_axis(width=400, height=120):
    """数轴上的等边三角形"""
    m, y = 40, height - 30
    s = 40
    c = [f'<line x1="{m}" y1="{y}" x2="{width-m}" y2="{y}" class="axis" marker-end="url(#arrow)"/>']
    for i in range(-2, 6):
        x = m + 50 + (i+2) * s
        c.append(f'<line x1="{x}" y1="{y-4}" x2="{x}" y2="{y+4}" class="tick"/>')
        c.append(f'<text x="{x}" y="{y+18}" text-anchor="middle" class="small">{i}</text>')
    cx, ax = m + 50 + s, m + 50 + 2*s
    bx, by = (cx + ax)/2, y - s * 0.866
    c.append(f'<polygon points="{ax},{y} {cx},{y} {bx},{by}" class="shape"/>')
    c.append(f'<text x="{ax+8}" y="{y-5}" class="label">A</text>')
    c.append(f'<text x="{cx-12}" y="{y-5}" class="label">C</text>')
    c.append(f'<text x="{bx}" y="{by-8}" text-anchor="middle" class="label">B</text>')
    return svg(width, height, '\n'.join(c))

def rectangle(w=120, h=80, labels=['A','B','C','D']):
    """矩形"""
    pw, ph = w + 60, h + 60
    ox, oy = 30, 30
    c = [f'<rect x="{ox}" y="{oy}" width="{w}" height="{h}" class="shape-fill"/>']
    pts = [(ox,oy,-10,-5), (ox+w,oy,5,-5), (ox+w,oy+h,5,15), (ox,oy+h,-10,15)]
    for i, (x, y, dx, dy) in enumerate(pts):
        c.append(f'<circle cx="{x}" cy="{y}" r="3" class="point-blue"/>')
        if i < len(labels):
            c.append(f'<text x="{x+dx}" y="{y+dy}" class="label">{labels[i]}</text>')
    return svg(pw, ph, '\n'.join(c))

def coordinate(xr=(-5,5), yr=(-5,5), pts=None, width=280, height=280):
    """坐标系 pts: [(label, x, y), ...]"""
    m = 35
    cx, cy = width/2, height/2
    sx = (width - 2*m) / (xr[1] - xr[0])
    sy = (height - 2*m) / (yr[1] - yr[0])
    c = []
    # X轴
    c.append(f'<line x1="{m}" y1="{cy}" x2="{width-m+10}" y2="{cy}" class="axis" marker-end="url(#arrow)"/>')
    c.append(f'<text x="{width-m+5}" y="{cy-10}" class="label">x</text>')
    # Y轴
    c.append(f'<line x1="{cx}" y1="{height-m}" x2="{cx}" y2="{m-10}" class="axis" marker-end="url(#arrow)"/>')
    c.append(f'<text x="{cx+12}" y="{m}" class="label">y</text>')
    c.append(f'<text x="{cx-12}" y="{cy+15}" class="small">O</text>')
    # 刻度
    for i in range(xr[0], xr[1]+1):
        if i == 0: continue
        x = cx + i * sx
        c.append(f'<line x1="{x}" y1="{cy-3}" x2="{x}" y2="{cy+3}" class="tick"/>')
        c.append(f'<text x="{x}" y="{cy+15}" text-anchor="middle" class="small" font-size="10">{i}</text>')
    for i in range(yr[0], yr[1]+1):
        if i == 0: continue
        y = cy - i * sy
        c.append(f'<line x1="{cx-3}" y1="{y}" x2="{cx+3}" y2="{y}" class="tick"/>')
        c.append(f'<text x="{cx-12}" y="{y+4}" text-anchor="end" class="small" font-size="10">{i}</text>')
    if pts:
        for label, px, py in pts:
            x, y = cx + px * sx, cy - py * sy
            c.append(f'<circle cx="{x}" cy="{y}" r="4" class="point"/>')
            c.append(f'<text x="{x+8}" y="{y-5}" class="label">{label}</text>')
    return svg(width, height, '\n'.join(c))

def angle_figure(deg=60, width=180, height=150):
    """角"""
    import math
    ox, oy = 40, height - 40
    L = 100
    rad = math.radians(deg)
    x2, y2 = ox + L, oy
    x3, y3 = ox + L * math.cos(rad), oy - L * math.sin(rad)
    c = []
    c.append(f'<line x1="{ox}" y1="{oy}" x2="{x2}" y2="{y2}" class="axis"/>')
    c.append(f'<line x1="{ox}" y1="{oy}" x2="{x3}" y2="{y3}" class="axis"/>')
    # 角弧
    r = 25
    arcx = ox + r * math.cos(rad/2)
    arcy = oy - r * math.sin(rad/2)
    c.append(f'<path d="M{ox+r},{oy} A{r},{r} 0 0 0 {ox+r*math.cos(rad)},{oy-r*math.sin(rad)}" class="shape" fill="none"/>')
    c.append(f'<circle cx="{ox}" cy="{oy}" r="3" class="point-blue"/>')
    c.append(f'<text x="{ox-12}" y="{oy+15}" class="label">O</text>')
    c.append(f'<text x="{x2+8}" y="{y2+5}" class="label">A</text>')
    c.append(f'<text x="{x3+5}" y="{y3-5}" class="label">B</text>')
    c.append(f'<text x="{ox+35}" y="{oy-15}" class="small">{deg}°</text>')
    return svg(width, height, '\n'.join(c))

def gear_pattern(n=3, width=200, height=200):
    """齿轮/图案规律"""
    import math
    cx, cy = width/2, height/2
    r1, r2 = 30, 50
    c = []
    # 内圆
    c.append(f'<circle cx="{cx}" cy="{cy}" r="{r1}" class="shape-fill"/>')
    # 齿
    teeth = 8
    for i in range(teeth):
        a = 2 * math.pi * i / teeth
        x1 = cx + r1 * math.cos(a)
        y1 = cy + r1 * math.sin(a)
        x2 = cx + r2 * math.cos(a)
        y2 = cy + r2 * math.sin(a)
        c.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="shape"/>')
    c.append(f'<text x="{cx}" y="{height-10}" text-anchor="middle" class="small">图{n}</text>')
    return svg(width, height, '\n'.join(c))

def table_figure(width=300, height=150):
    """表格"""
    c = []
    c.append(f'<rect x="20" y="20" width="260" height="110" class="shape" fill="white"/>')
    # 横线
    for i in range(4):
        y = 20 + i * 36.7
        c.append(f'<line x1="20" y1="{y}" x2="280" y2="{y}" class="tick"/>')
    # 竖线
    for i in range(5):
        x = 20 + i * 65
        c.append(f'<line x1="{x}" y1="20" x2="{x}" y2="130" class="tick"/>')
    # 表头
    headers = ['项目', 'A', 'B', 'C']
    for i, h in enumerate(headers):
        c.append(f'<text x="{52+i*65}" y="{45}" text-anchor="middle" class="small">{h}</text>')
    return svg(width, height, '\n'.join(c))

# ========== 主函数 ==========

def main():
    print("=" * 60)
    print("🎨 为所有题目生成SVG图形")
    print("=" * 60)
    
    # t1: 数轴动点
    print("\n📚 t1: 数轴动点问题")
    save("t1_example.svg", numberline_segment(-5, 15, [(-2, 'B'), (10, 'A')], width=500))
    save("t1_train.svg", numberline_segment(-5, 15, [(-2, 'B'), (10, 'A')], width=500))
    
    # t2: 规律探究
    print("\n📚 t2: 规律探究")
    save("t2_example.svg", triangle_on_axis())
    save("t2_train.svg", triangle_on_axis())
    
    # t3: 比较大小
    print("\n📚 t3: 比较有理数大小")
    save("t3_example.svg", numberline_letters([(0.15,'a'), (0.35,'b'), (0.55,'0'), (0.75,'1')]))
    save("t3_train.svg", numberline(-5, 5, [(-4,''), (-1.5,''), (0,'0'), (2.5,'')]))
    
    # t4: 绝对值性质
    print("\n📚 t4: 绝对值性质")
    save("t4_example.svg", numberline(-5, 5, [(-3,'a'), (2,'b')]))
    save("t4_train.svg", numberline(-5, 5, [(-3,'a'), (2,'b')]))
    
    # t5: 几何意义
    print("\n📚 t5: 几何意义")
    save("t5_example.svg", numberline(-4, 4, [(-2,''), (1,'')]))
    save("t5_train.svg", numberline(-4, 4, [(-2,'-2'), (1,'1')]))
    
    # t6: 新定义
    print("\n📚 t6: 新定义问题")
    save("t6_example.svg", table_figure())
    
    # t7: 实际应用
    print("\n📚 t7: 实际应用")
    save("t7_example.svg", coordinate((-3,3), (-3,3), [('P',1,2), ('Q',-1,-1)]))
    
    # t8: 拼凑法
    print("\n📚 t8: 拼凑法")
    save("t8_example.svg", numberline(-5, 5, []))
    
    # t9: 裂项法
    print("\n📚 t9: 裂项法")
    save("t9_example.svg", rectangle(100, 60, ['1','2','3','4']))
    
    # t10: 倒数法
    print("\n📚 t10: 倒数法")
    save("t10_example.svg", numberline(-3, 3, [(0,'0'), (1,'1')]))
    
    # t11: 混合运算
    print("\n📚 t11: 混合运算")
    save("t11_example.svg", numberline(-5, 5, []))
    
    # t12: 折叠
    print("\n📚 t12: 折叠问题")
    save("t12_example.svg", numberline_fold())
    save("t12_train.svg", numberline_fold())
    
    # t13: 动点
    print("\n📚 t13: 动点问题")
    save("t13_example.svg", numberline_segment(-10, 10, [(-6, 'A'), (4, 'B')], width=500))
    save("t13_train.svg", numberline_segment(-10, 10, [(-6, 'A'), (4, 'B')], width=500))
    
    # t16: 用字母表示数
    print("\n📚 t16: 用字母表示数")
    save("t16_example.svg", rectangle(120, 80, ['客厅','次卧','主卧','厨房']))
    
    # t17: 代数式的值
    print("\n📚 t17: 代数式求值")
    save("t17_example.svg", table_figure())
    
    # t18: 整体思想
    print("\n📚 t18: 整体思想")
    save("t18_example.svg", numberline(-5, 5, [(2,'x')]))
    
    # t19: 归纳猜想
    print("\n📚 t19: 归纳猜想")
    save("t19_example.svg", gear_pattern(1))
    save("t19_train.svg", gear_pattern(2))
    
    # t20: 代数式新定义
    print("\n📚 t20: 代数式新定义")
    save("t20_example.svg", table_figure())
    
    # t21: 化简求值
    print("\n📚 t21: 化简求值")
    save("t21_example.svg", numberline(-3, 3, [(0,'0')]))
    
    # t22: 数轴化简绝对值
    print("\n📚 t22: 数轴化简绝对值")
    save("t22_example.svg", numberline_letters([(0.2,'a'), (0.5,'0'), (0.8,'b')]))
    save("t22_train.svg", numberline_letters([(0.2,'a'), (0.5,'0'), (0.8,'b')]))
    
    # t23: 分类讨论
    print("\n📚 t23: 分类讨论")
    save("t23_example.svg", numberline_letters([(0.15,'a'), (0.4,'0'), (0.65,'b'), (0.9,'c')]))
    save("t23_train.svg", numberline(-5, 5, [(-3,''), (0,'0'), (2,'')]))
    
    # t24: 新定义问题
    print("\n📚 t24: 新定义问题")
    save("t24_example.svg", gear_pattern(3))
    
    # t25: 整体思想解方程
    print("\n📚 t25: 整体思想解方程")
    save("t25_example.svg", numberline(-5, 5, []))
    
    # t26: 特殊化思想
    print("\n📚 t26: 特殊化思想")
    save("t26_example.svg", table_figure())
    
    # t27: 含绝对值方程
    print("\n📚 t27: 含绝对值方程")
    save("t27_example.svg", numberline(-5, 5, [(-2,''), (3,'')]))
    save("t27_train.svg", numberline(-5, 5, [(-2,'-2'), (3,'3')]))
    
    print("\n" + "=" * 60)
    total = len(list(OUTPUT_DIR.glob("*.svg")))
    print(f"✅ 完成！共生成 {total} 个SVG图形")
    print(f"📁 输出目录: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()





