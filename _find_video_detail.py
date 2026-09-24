# -*- coding: utf-8 -*-
HTML = r'D:\天泽智联\大工贸\数智大脑\综合监管大屏.单位实时监测详情工作稿.html'
with open(HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 找openVideoDetail函数
idx = content.find('openVideoDetail')
for i in range(3):
    idx = content.find('openVideoDetail', idx + 1)
    if idx < 0: break
    start = max(0, idx - 100)
    end = min(len(content), idx + 300)
    print(f"--- 位置 {idx} ---")
    print(content[start:end])
    print()
