# -*- coding: utf-8 -*-
HTML = r'D:\天泽智联\大工贸\数智大脑\综合监管大屏.单位实时监测详情工作稿.html'
with open(HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 检查是否还有video-detail-modal相关代码
print("=== 检查视频详情弹窗代码 ===")
if 'video-detail-modal' in content:
    print("✓ video-detail-modal CSS存在")
else:
    print("✗ video-detail-modal 不存在")

if 'openVideoDetail' in content:
    print("✓ openVideoDetail函数存在")
else:
    print("✗ openVideoDetail函数不存在")

# 找openVideoDetail函数
idx = content.find('function openVideoDetail')
if idx >= 0:
    end = content.find('}', idx)
    print(content[idx:end+1])
