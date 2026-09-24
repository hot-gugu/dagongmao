# -*- coding: utf-8 -*-
HTML = r'D:\天泽智联\大工贸\数智大脑\综合监管大屏.单位实时监测详情工作稿.html'
with open(HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 找window.openVideoDetail的定义
import re
for m in re.finditer(r'window\.openVideoDetail\s*=|function\s+openVideoDetail', content):
    start = m.start()
    end = min(len(content), start + 500)
    print(f"--- 位置 {start} ---")
    print(content[start:end])
    print()
