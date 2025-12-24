#!/usr/bin/env python3
"""
智能裁剪脚本 - 使用OCR检测"针对训练"位置并精确裁剪
"""

import os
import sys
from pathlib import Path

try:
    from PIL import Image
    import pytesseract
    import cv2
    import numpy as np
except ImportError as e:
    print(f"缺少依赖: {e}")
    print("\n请运行以下命令安装依赖:")
    print("  pip3 install pillow pytesseract opencv-python numpy")
    print("\n还需要安装Tesseract OCR:")
    print("  macOS: brew install tesseract tesseract-lang")
    print("  Ubuntu: sudo apt install tesseract-ocr tesseract-ocr-chi-sim")
    sys.exit(1)

# 配置
SOURCE_DIR = Path("/Users/youyou/Downloads/M压轴/packages/图片")
OUTPUT_DIR = Path("/Users/youyou/Downloads/M压轴/packages/图片_智能裁剪")

# 要检测的关键词
KEYWORDS = ["针对训练", "对训练", "训练"]

def find_keyword_position(image_path):
    """
    使用OCR检测图片中"针对训练"的位置
    返回: y坐标（从顶部开始），如果未找到返回None
    """
    try:
        # 读取图片
        img = cv2.imread(str(image_path))
        if img is None:
            return None
            
        # 转为灰度图
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # 获取图片尺寸
        height, width = gray.shape
        
        # 使用Tesseract进行OCR，获取每个字符的位置
        # 配置为中文识别
        custom_config = r'--oem 3 --psm 6 -l chi_sim+eng'
        
        # 获取详细的OCR数据（包含位置信息）
        data = pytesseract.image_to_data(gray, config=custom_config, output_type=pytesseract.Output.DICT)
        
        # 搜索关键词
        text = ' '.join(data['text'])
        
        for keyword in KEYWORDS:
            if keyword in text:
                # 找到关键词的位置
                for i, word in enumerate(data['text']):
                    if keyword in word or (i > 0 and keyword in data['text'][i-1] + word):
                        # 返回该词的顶部y坐标
                        return data['top'][i]
        
        # 如果没找到关键词，尝试在图片中部区域搜索
        # 扫描图片的40%-60%区域
        scan_start = int(height * 0.35)
        scan_end = int(height * 0.65)
        
        for keyword in KEYWORDS:
            # 在扫描区域内逐行搜索
            for y in range(scan_start, scan_end, 30):
                roi = gray[y:min(y+60, height), :]
                roi_text = pytesseract.image_to_string(roi, config=custom_config)
                if keyword in roi_text:
                    return y
        
        return None
        
    except Exception as e:
        print(f"  OCR错误: {e}")
        return None

def detect_horizontal_line(image_path):
    """
    检测图片中的水平分隔线位置
    返回: y坐标，如果未找到返回None
    """
    try:
        img = cv2.imread(str(image_path))
        if img is None:
            return None
            
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        height, width = gray.shape
        
        # 边缘检测
        edges = cv2.Canny(gray, 50, 150, apertureSize=3)
        
        # 霍夫线变换检测水平线
        lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, 
                                minLineLength=width*0.5, maxLineGap=10)
        
        if lines is not None:
            horizontal_lines = []
            for line in lines:
                x1, y1, x2, y2 = line[0]
                # 检查是否为水平线（y坐标差异小于10像素）
                if abs(y2 - y1) < 10:
                    # 只考虑图片中间区域的线（35%-65%）
                    avg_y = (y1 + y2) // 2
                    if height * 0.35 < avg_y < height * 0.65:
                        horizontal_lines.append(avg_y)
            
            if horizontal_lines:
                # 返回最接近中间的水平线
                center = height * 0.5
                return min(horizontal_lines, key=lambda y: abs(y - center))
        
        return None
        
    except Exception as e:
        print(f"  线检测错误: {e}")
        return None

def smart_crop(image_path, output_dir):
    """
    智能裁剪图片
    1. 首先尝试OCR检测"针对训练"位置
    2. 如果失败，尝试检测水平分隔线
    3. 如果都失败，使用默认比例(48%)
    """
    try:
        img = Image.open(image_path)
        width, height = img.size
        
        # 方法1: OCR检测关键词位置
        split_y = find_keyword_position(image_path)
        method = "OCR"
        
        # 方法2: 检测水平分隔线
        if split_y is None:
            split_y = detect_horizontal_line(image_path)
            method = "线检测"
        
        # 方法3: 默认比例
        if split_y is None:
            split_y = int(height * 0.48)
            method = "默认"
        
        # 确保分割点在合理范围内
        split_y = max(int(height * 0.3), min(split_y, int(height * 0.7)))
        
        # 裁剪
        example_img = img.crop((0, 0, width, split_y))
        exercise_img = img.crop((0, split_y, width, height))
        
        # 保存
        filename = image_path.stem
        ext = image_path.suffix
        
        example_path = output_dir / f"{filename}_例题{ext}"
        exercise_path = output_dir / f"{filename}_习题{ext}"
        
        example_img.save(example_path, quality=95)
        exercise_img.save(exercise_path, quality=95)
        
        return method, split_y, height
        
    except Exception as e:
        print(f"  处理失败: {e}")
        return None, None, None

def main():
    print("=" * 60)
    print("🎯 智能裁剪工具")
    print("=" * 60)
    print(f"源目录: {SOURCE_DIR}")
    print(f"输出目录: {OUTPUT_DIR}")
    print("=" * 60)
    
    # 检查Tesseract是否安装
    try:
        pytesseract.get_tesseract_version()
        print("✅ Tesseract OCR 已安装")
    except:
        print("❌ Tesseract OCR 未安装")
        print("\n请安装Tesseract:")
        print("  macOS: brew install tesseract tesseract-lang")
        return
    
    # 确保输出目录存在
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # 获取所有图片
    image_files = sorted(SOURCE_DIR.glob("*.jpg"))
    total = len(image_files)
    
    print(f"\n找到 {total} 张图片")
    print("-" * 60)
    
    stats = {"OCR": 0, "线检测": 0, "默认": 0, "失败": 0}
    
    for i, img_path in enumerate(image_files, 1):
        print(f"[{i}/{total}] {img_path.name}", end=" ")
        method, split_y, height = smart_crop(img_path, OUTPUT_DIR)
        
        if method:
            ratio = split_y / height * 100 if height else 0
            print(f"✅ [{method}] 分割位置: {ratio:.1f}%")
            stats[method] += 1
        else:
            print("❌ 失败")
            stats["失败"] += 1
    
    print("-" * 60)
    print("\n📊 统计:")
    for method, count in stats.items():
        if count > 0:
            print(f"  {method}: {count} 张")
    
    print(f"\n裁剪完成！输出目录: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()





