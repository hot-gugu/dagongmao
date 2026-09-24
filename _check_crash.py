# -*- coding: utf-8 -*-
HTML = r'D:\天泽智联\大工贸\数智大脑\综合监管大屏.单位实时监测详情工作稿.html'
with open(HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 找openCameraLive函数
idx = content.find('function openCameraLive')
if idx >= 0:
    end = content.find('function openLiveModal', idx)
    print("=== openCameraLive函数 ===")
    print(content[idx:end])
    print()

# 检查是否有重复定义
count = content.count('function openCameraLive')
print(f"openCameraLive定义次数: {count}")

# 检查onclick
count2 = content.count('openCameraLive(this')
print(f"openCameraLive调用次数: {count2}")
