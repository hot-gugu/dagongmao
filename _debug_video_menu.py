# -*- coding: utf-8 -*-
HTML = r'D:\天泽智联\大工贸\数智大脑\综合监管大屏.单位实时监测详情工作稿.html'
with open(HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 找视频监管菜单
import re
for m in re.finditer(r'视频监管|video.*tab|tab.*video', content):
    s = max(0, m.start()-100)
    e = min(len(content), m.end()+200)
    text = content[s:e]
    if 'data-tab' in text or 'nav' in text.lower() or 'menu' in text.lower():
        print(f"--- at {m.start()} ---")
        print(text)
        print()
