# -*- coding: utf-8 -*-
HTML = r'D:\天泽智联\大工贸\数智大脑\综合监管大屏.单位实时监测详情工作稿.html'
with open(HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 检查video-wall-feed的onclick
print("=== 1. video-wall-feed当前代码 ===")
idx = content.find('class="video-wall-feed"')
if idx >= 0:
    end = content.find('</div>', idx) + 6
    print(content[idx:end])
else:
    print("未找到")

print()
print("=== 2. openVideoDetail函数 ===")
idx = content.find('window.openVideoDetail=')
if idx >= 0:
    end = content.find(';', idx + 200)
    print(content[idx:idx+500])
else:
    print("未找到")

print()
print("=== 3. drawer元素 ===")
print(f"#drawer元素: {'存在' if 'id="drawer"' in content else '不存在'}")

print()
print("=== 4. openAiDetailNew函数 ===")
print(f"openAiDetailNew: {'存在' if 'openAiDetailNew' in content else '不存在'}")
