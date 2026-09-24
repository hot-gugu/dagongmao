# -*- coding: utf-8 -*-
HTML = r'D:\天泽智联\大工贸\数智大脑\综合监管大屏.单位实时监测详情工作稿.html'
with open(HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 检查script标签数量
import re
scripts = re.findall(r'<script[^>]*>', content)
closes = re.findall(r'</script>', content)
print(f"<script>开始标签: {len(scripts)}")
print(f"</script>结束标签: {len(closes)}")

# 检查style标签
styles = re.findall(r'<style[^>]*>', content)
style_closes = re.findall(r'</style>', content)
print(f"<style>开始标签: {len(styles)}")
print(f"</style>结束标签: {len(style_closes)}")

# 检查最后几个script标签
print()
print("=== 最后5个script标签位置 ===")
positions = [m.start() for m in re.finditer(r'<script', content)]
for pos in positions[-5:]:
    print(f"位置 {pos}: {content[pos:pos+100]}")
