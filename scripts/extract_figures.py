#!/usr/bin/env python3
"""
智能图形提取工具
从PDF图片中精确检测并裁剪出图形区域（数轴、几何图形、表格等）
"""

import os
import sys
from pathlib import Path

try:
    from PIL import Image
    import cv2
    import numpy as np
except ImportError as e:
    print(f"缺少依赖: {e}")
    print("请运行: pip3 install pillow opencv-python numpy")
    sys.exit(1)

# 配置
SOURCE_DIR = Path("/Users/youyou/Downloads/M压轴/packages/图片")
OUTPUT_DIR = Path("/Users/youyou/Downloads/M压轴/packages/提取图形")

def find_figure_regions(image_path):
    """
    检测图片中的图形区域
    返回: [(x, y, w, h, type), ...] 图形区域列表
    """
    img = cv2.imread(str(image_path))
    if img is None:
        return []
    
    height, width = img.shape[:2]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 二值化
    _, binary = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
    
    # 形态学操作，连接相近的元素
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
    dilated = cv2.dilate(binary, kernel, iterations=2)
    
    # 查找轮廓
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    figures = []
    min_area = width * height * 0.01  # 最小面积阈值（1%）
    max_area = width * height * 0.5   # 最大面积阈值（50%）
    
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        area = w * h
        
        # 过滤太小或太大的区域
        if area < min_area or area > max_area:
            continue
        
        # 过滤太窄的区域（可能是文字行）
        aspect_ratio = w / h if h > 0 else 0
        if aspect_ratio > 10 or aspect_ratio < 0.1:
            continue
        
        # 检测图形类型
        fig_type = detect_figure_type(gray[y:y+h, x:x+w])
        
        figures.append({
            'x': x, 'y': y, 'w': w, 'h': h,
            'type': fig_type,
            'area': area
        })
    
    # 按y坐标排序
    figures.sort(key=lambda f: f['y'])
    
    return figures

def detect_figure_type(roi):
    """
    检测图形类型
    """
    if roi.size == 0:
        return 'unknown'
    
    # 边缘检测
    edges = cv2.Canny(roi, 50, 150)
    
    # 霍夫线变换检测直线
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, 
                            minLineLength=30, maxLineGap=10)
    
    if lines is None:
        return 'shape'
    
    # 分析线条角度
    horizontal_count = 0
    vertical_count = 0
    
    for line in lines:
        x1, y1, x2, y2 = line[0]
        angle = np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi
        
        if abs(angle) < 10 or abs(angle) > 170:
            horizontal_count += 1
        elif 80 < abs(angle) < 100:
            vertical_count += 1
    
    # 判断图形类型
    if horizontal_count > 3 and vertical_count < 2:
        return 'number_line'  # 数轴
    elif horizontal_count > 2 and vertical_count > 2:
        return 'table'  # 表格
    elif len(lines) > 5:
        return 'geometry'  # 几何图形
    else:
        return 'shape'

def extract_number_line(image_path, output_dir):
    """
    专门提取数轴图形
    """
    img = cv2.imread(str(image_path))
    if img is None:
        return []
    
    height, width = img.shape[:2]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 边缘检测
    edges = cv2.Canny(gray, 50, 150)
    
    # 检测水平线
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100,
                            minLineLength=width*0.3, maxLineGap=20)
    
    number_lines = []
    
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            # 检查是否为水平线
            if abs(y2 - y1) < 10:
                # 扩展区域以包含刻度和标签
                y_center = (y1 + y2) // 2
                y_top = max(0, y_center - 60)
                y_bottom = min(height, y_center + 40)
                x_left = max(0, min(x1, x2) - 20)
                x_right = min(width, max(x1, x2) + 20)
                
                number_lines.append({
                    'x': x_left,
                    'y': y_top,
                    'w': x_right - x_left,
                    'h': y_bottom - y_top,
                    'type': 'number_line'
                })
    
    return number_lines

def extract_all_figures(image_path, output_dir, filename_prefix):
    """
    从图片中提取所有图形
    """
    img = Image.open(image_path)
    
    # 方法1: 通用图形检测
    figures = find_figure_regions(image_path)
    
    # 方法2: 专门检测数轴
    number_lines = extract_number_line(image_path, output_dir)
    
    # 合并结果，去重
    all_figures = figures + number_lines
    
    # 去除重叠区域
    filtered_figures = []
    for fig in all_figures:
        is_duplicate = False
        for existing in filtered_figures:
            # 检查重叠
            overlap_x = max(0, min(fig['x']+fig['w'], existing['x']+existing['w']) - max(fig['x'], existing['x']))
            overlap_y = max(0, min(fig['y']+fig['h'], existing['y']+existing['h']) - max(fig['y'], existing['y']))
            overlap_area = overlap_x * overlap_y
            
            if overlap_area > fig['w'] * fig['h'] * 0.5:
                is_duplicate = True
                break
        
        if not is_duplicate:
            filtered_figures.append(fig)
    
    # 保存提取的图形
    saved_files = []
    for i, fig in enumerate(filtered_figures):
        # 裁剪图形
        cropped = img.crop((fig['x'], fig['y'], 
                           fig['x'] + fig['w'], fig['y'] + fig['h']))
        
        # 添加白色边距
        padded = Image.new('RGB', (fig['w'] + 20, fig['h'] + 20), 'white')
        padded.paste(cropped, (10, 10))
        
        # 保存
        output_name = f"{filename_prefix}_fig{i+1}_{fig['type']}.png"
        output_path = output_dir / output_name
        padded.save(output_path)
        saved_files.append(output_path)
    
    return saved_files

def main():
    print("=" * 60)
    print("🎨 智能图形提取工具")
    print("=" * 60)
    print(f"源目录: {SOURCE_DIR}")
    print(f"输出目录: {OUTPUT_DIR}")
    print("=" * 60)
    
    # 确保输出目录存在
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # 获取所有图片
    image_files = sorted(SOURCE_DIR.glob("*.jpg"))
    total = len(image_files)
    
    print(f"\n找到 {total} 张图片")
    print("-" * 60)
    
    total_figures = 0
    
    for i, img_path in enumerate(image_files, 1):
        print(f"[{i}/{total}] {img_path.name}", end=" ")
        
        prefix = img_path.stem
        figures = extract_all_figures(img_path, OUTPUT_DIR, prefix)
        
        print(f"✅ 提取了 {len(figures)} 个图形")
        total_figures += len(figures)
    
    print("-" * 60)
    print(f"\n✅ 完成！共提取 {total_figures} 个图形")
    print(f"输出目录: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()





