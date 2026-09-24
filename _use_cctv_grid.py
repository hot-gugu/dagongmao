# -*- coding: utf-8 -*-
HTML = r'D:\天泽智联\大工贸\数智大脑\综合监管大屏.单位实时监测详情工作稿.html'
with open(HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 修改video-wall-feed的HTML：用assets网格图
old = """${rows.length?rows.map(({company,index})=>{var scenes=['tank','workshop','warehouse','limit','melt','mine'];var sceneCls='scene-'+scenes[(company.id+index)%6];return `<div class="video-wall-feed" data-video-wall-record="${company.id}" data-video-wall-camera="${index+1}" aria-label="查看${escText(company.name)}视频详情"><span class="video-wall-image camera-scene ${sceneCls}"></span><span class="video-wall-live"><i></i>LIVE</span><button class="camera-live-btn" onclick="openCameraLive(this,'wall')" title="直播调阅">LIVE</button><span class="video-wall-meta"><strong>${escText(company.name)}</strong><span>CAM ${String(index+1).padStart(2,'0')}</span></span></div>`;}).join('')"""

new = """${rows.length?rows.map(({company,index})=>{var cols=3,rows3=3;var col=index%cols,row=Math.floor(index/cols)%rows3;var bgPos=(col*50)+'% '+(row*50)+'%';return `<div class="video-wall-feed" data-video-wall-record="${company.id}" data-video-wall-camera="${index+1}" aria-label="查看${escText(company.name)}视频详情"><span class="video-wall-image cctv-grid-img" style="background-position:${bgPos}"></span><span class="video-wall-live"><i></i>LIVE</span><button class="camera-live-btn" onclick="openCameraLive(this,'wall')" title="直播调阅">LIVE</button><span class="video-wall-meta"><strong>${escText(company.name)}</strong><span>CAM ${String(index+1).padStart(2,'0')}</span></span></div>`;}).join('')"""

assert old in content, '未找到video-wall代码'
content = content.replace(old, new)
print('[1] video-wall已改用assets网格图')

# 添加CSS：设置背景图和尺寸
css = '''
<style>
.cctv-grid-img{background-image:url('assets/industrial-cctv-grid-v2.png')!important;background-size:300% 300%!important;background-repeat:no-repeat;}
</style>'''

body_end = content.rfind('</body>')
content = content[:body_end] + css + content[body_end:]
print('[2] 网格图CSS已添加')

with open(HTML, 'w', encoding='utf-8') as f:
    f.write(content)
print('完成')
