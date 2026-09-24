# -*- coding: utf-8 -*-
HTML = r'D:\天泽智联\大工贸\数智大脑\综合监管大屏.单位实时监测详情工作稿.html'
with open(HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 去掉video-wall-feed里的直播按钮
import re
# 匹配 <button class="camera-live-btn" ...>...</button>
pattern = r'<button class="camera-live-btn"[^>]*>[^<]*</button>'
matches = re.findall(pattern, content)
print(f"找到 {len(matches)} 个直播按钮")

content = re.sub(pattern, '', content)
print('[1] 直播按钮HTML已删除')

# 2. 去掉cameraCard里的直播按钮（如果有的话）
pattern2 = r'<button class="camera-live-btn"[^>]*>[^<]*</button>'
content = re.sub(pattern2, '', content)

with open(HTML, 'w', encoding='utf-8') as f:
    f.write(content)
print('完成')
