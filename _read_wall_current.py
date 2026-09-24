# -*- coding: utf-8 -*-
HTML = r'D:\天泽智联\大工贸\数智大脑\综合监管大屏.单位实时监测详情工作稿.html'
with open(HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 找video-wall-feed的HTML生成代码
idx = content.find('data-video-wall-record')
if idx >= 0:
    start = max(0, idx - 200)
    end = min(len(content), idx + 500)
    print(content[start:end])
