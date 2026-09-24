# -*- coding: utf-8 -*-
HTML = r'D:\天泽智联\大工贸\数智大脑\综合监管大屏.单位实时监测详情工作稿.html'
with open(HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 检查依赖的函数和元素
print("=== 检查依赖 ===")
print(f"openAiDetailNew函数: {'存在' if 'function openAiDetailNew' in content or 'openAiDetailNew=' in content else '不存在'}")
print(f"cameraLiveModal元素: {'存在' if 'id="cameraLiveModal"' in content else '不存在'}")
print(f"liveCamTitle元素: {'存在' if 'id="liveCamTitle"' in content else '不存在'}")
print(f"openLiveModal函数: {'存在' if 'function openLiveModal' in content else '不存在'}")

# 找直播弹窗的HTML
idx = content.find('id="cameraLiveModal"')
if idx >= 0:
    start = max(0, idx - 100)
    end = min(len(content), idx + 300)
    print()
    print("=== 直播弹窗HTML ===")
    print(content[start:end])
