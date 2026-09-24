# -*- coding: utf-8 -*-
HTML = r'D:\天泽智联\大工贸\数智大脑\综合监管大屏.单位实时监测详情工作稿.html'
with open(HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 找到并删除有问题的script
start = content.find('<script id="video-industrial-scenes-v2-script">')
if start >= 0:
    end = content.find('</script>', start) + 9
    problematic_script = content[start:end]
    content = content[:start] + content[end:]
    print('[1] 已删除有问题的 video-industrial-scenes-v2-script')
    print(f'删除内容长度: {len(problematic_script)} 字符')
else:
    print('[1] 未找到该script')

with open(HTML, 'w', encoding='utf-8') as f:
    f.write(content)
print('完成')
