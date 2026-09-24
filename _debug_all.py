# -*- coding: utf-8 -*-
HTML = r'D:\天泽智联\大工贸\数智大脑\综合监管大屏.单位实时监测详情工作稿.html'
with open(HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 检查当前video-wall-feed的完整HTML
print("=== 1. video-wall-feed HTML ===")
idx = content.find('class="video-wall-feed"')
if idx >= 0:
    end = content.find('</div>', idx) + 6
    print(content[idx:end])
else:
    print("未找到")

print()
print("=== 2. openCameraLive函数 ===")
idx = content.find('function openCameraLive')
if idx >= 0:
    end = content.find('function openLiveModal', idx)
    print(content[idx:end])
else:
    print("未找到")

print()
print("=== 3. openVideoDetail函数开头 ===")
idx = content.find('window.openVideoDetail=')
if idx >= 0:
    print(content[idx:idx+300])
else:
    print("未找到")
