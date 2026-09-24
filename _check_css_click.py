# -*- coding: utf-8 -*-
HTML = r'D:\天泽智联\大工贸\数智大脑\综合监管大屏.单位实时监测详情工作稿.html'
with open(HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 检查video-wall相关的pointer-events
import re
for m in re.finditer(r'video-wall[^{]*\{[^}]*pointer-events[^}]*\}', content):
    print(m.group())
    print()

# 检查camera-live-btn的完整CSS
idx = content.find('.camera-live-btn{')
if idx >= 0:
    end = content.find('}', idx) + 1
    print("=== camera-live-btn CSS ===")
    print(content[idx:end])

# 检查video-wall-feed的完整CSS
idx2 = content.find('.video-wall-feed{')
if idx2 >= 0:
    end2 = content.find('}', idx2) + 1
    print()
    print("=== video-wall-feed CSS ===")
    print(content[idx2:end2])
