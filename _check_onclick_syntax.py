# -*- coding: utf-8 -*-
HTML = r'D:\天泽智联\大工贸\数智大脑\综合监管大屏.单位实时监测详情工作稿.html'
with open(HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 找我加的onclick代码，检查是否有语法问题
idx = content.find('onclick="event.stopPropagation()')
if idx >= 0:
    print("=== 第一个onclick ===")
    print(content[idx:idx+300])
    print()

# 找第二个
idx2 = content.find('onclick="event.stopPropagation()', idx+1)
if idx2 >= 0:
    print("=== 第二个onclick ===")
    print(content[idx2:idx2+300])
    print()

# 检查是否有未闭合的引号
print("=== 检查引号 ===")
onclick_count = content.count('onclick="event.stopPropagation()')
print(f"onclick出现次数: {onclick_count}")
