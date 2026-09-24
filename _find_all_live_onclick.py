# -*- coding: utf-8 -*-
HTML = r'D:\天泽智联\大工贸\数智大脑\综合监管大屏.单位实时监测详情工作稿.html'
with open(HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 找所有包含openLiveModal的onclick
import re
for m in re.finditer(r'onclick="[^"]*openLiveModal[^"]*"', content):
    print(f"--- at {m.start()} ---")
    print(m.group())
    print()
