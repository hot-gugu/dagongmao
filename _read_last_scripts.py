# -*- coding: utf-8 -*-
HTML = r'D:\天泽智联\大工贸\数智大脑\综合监管大屏.单位实时监测详情工作稿.html'
with open(HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 找最后一个script标签的完整内容
idx = content.rfind('<script')
end = content.find('</script>', idx) + 9
print("=== 最后一个script ===")
print(content[idx:end])
print()

# 找倒数第二个
idx2 = content.rfind('<script', 0, idx)
end2 = content.find('</script>', idx2) + 9
print("=== 倒数第二个script ===")
print(content[idx2:end2])
