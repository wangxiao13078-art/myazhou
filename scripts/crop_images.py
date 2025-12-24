#!/usr/bin/env python3
"""
自动裁剪PDF图片脚本
将每张图片裁剪为上半部分（例题）和下半部分（习题）
"""

import os
from PIL import Image
from pathlib import Path

# 配置
SOURCE_DIR = Path("/Users/youyou/Downloads/M压轴/packages/图片")
OUTPUT_DIR = Path("/Users/youyou/Downloads/M压轴/packages/图片_裁剪")

# 裁剪比例配置
# 例题部分占图片的前50%，习题部分占后50%
# "针对训练"标题通常在页面中间位置
EXAMPLE_RATIO = 0.48  # 例题占比（稍微靠上）
EXERCISE_RATIO = 0.52  # 习题占比

def ensure_dir(path):
    """确保目录存在"""
    path.mkdir(parents=True, exist_ok=True)

def crop_image(image_path, output_dir):
    """
    裁剪单张图片
    返回: (例题图片路径, 习题图片路径) 或 None
    """
    try:
        img = Image.open(image_path)
        width, height = img.size
        
        # 计算裁剪位置
        # 找到"针对训练"分隔线的位置（大约在图片的50-60%处）
        split_point = int(height * EXAMPLE_RATIO)
        
        # 裁剪例题部分（上半部分）
        example_img = img.crop((0, 0, width, split_point))
        
        # 裁剪习题部分（下半部分）
        exercise_img = img.crop((0, split_point, width, height))
        
        # 生成输出文件名
        filename = image_path.stem
        ext = image_path.suffix
        
        example_path = output_dir / f"{filename}_例题{ext}"
        exercise_path = output_dir / f"{filename}_习题{ext}"
        
        # 保存裁剪后的图片
        example_img.save(example_path, quality=95)
        exercise_img.save(exercise_path, quality=95)
        
        return example_path, exercise_path
        
    except Exception as e:
        print(f"  ❌ 处理失败: {image_path.name} - {e}")
        return None

def main():
    print("=" * 60)
    print("📷 图片裁剪工具")
    print("=" * 60)
    print(f"源目录: {SOURCE_DIR}")
    print(f"输出目录: {OUTPUT_DIR}")
    print(f"裁剪比例: 例题 {EXAMPLE_RATIO*100:.0f}% / 习题 {EXERCISE_RATIO*100:.0f}%")
    print("=" * 60)
    
    # 确保输出目录存在
    ensure_dir(OUTPUT_DIR)
    
    # 获取所有图片文件
    image_files = sorted(SOURCE_DIR.glob("*.jpg"))
    total = len(image_files)
    
    print(f"\n找到 {total} 张图片")
    print("-" * 60)
    
    success_count = 0
    fail_count = 0
    
    for i, img_path in enumerate(image_files, 1):
        print(f"[{i}/{total}] 处理: {img_path.name}", end=" ")
        result = crop_image(img_path, OUTPUT_DIR)
        if result:
            print("✅")
            success_count += 1
        else:
            fail_count += 1
    
    print("-" * 60)
    print(f"\n✅ 成功: {success_count} 张")
    print(f"❌ 失败: {fail_count} 张")
    print(f"\n裁剪后的图片保存在: {OUTPUT_DIR}")
    
    # 统计输出
    example_count = len(list(OUTPUT_DIR.glob("*_例题.jpg")))
    exercise_count = len(list(OUTPUT_DIR.glob("*_习题.jpg")))
    print(f"  - 例题图片: {example_count} 张")
    print(f"  - 习题图片: {exercise_count} 张")

if __name__ == "__main__":
    main()

