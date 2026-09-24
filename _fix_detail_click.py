# -*- coding: utf-8 -*-
HTML = r'D:\天泽智联\大工贸\数智大脑\综合监管大屏.单位实时监测详情工作稿.html'
with open(HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 修改video-wall-feed：给整个div加onclick
old = '<div class="video-wall-feed" data-video-wall-record="${company.id}" data-video-wall-camera="${index+1}" aria-label="查看${escText(company.name)}视频详情">'

new = '<div class="video-wall-feed" data-video-wall-record="${company.id}" data-video-wall-camera="${index+1}" aria-label="查看${escText(company.name)}视频详情" onclick="window.openVideoDetail(${company.id},${index+1})" style="cursor:pointer;">'

assert old in content, '未找到video-wall-feed标签'
content = content.replace(old, new)
print('[1] video-wall-feed已加onclick')

# 确保直播按钮点击时不冒泡，不会同时触发详情
old_btn = 'onclick="openCameraLive(this,\'wall\')"'
new_btn = 'onclick="event.stopPropagation();openCameraLive(this,\'wall\')"'

if old_btn in content:
    content = content.replace(old_btn, new_btn)
    print('[2] 直播按钮已加stopPropagation')

with open(HTML, 'w', encoding='utf-8') as f:
    f.write(content)
print('完成')
