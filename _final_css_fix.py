# -*- coding: utf-8 -*-
HTML = r'D:\天泽智联\大工贸\数智大脑\综合监管大屏.单位实时监测详情工作稿.html'
with open(HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 在body末尾加最终的CSS，用!important确保覆盖所有旧样式
final_css = '''
<style id="final-camera-fix">
/* 直播按钮最终修复 */
.camera-live-btn{
  position:absolute!important;
  bottom:30px!important;
  right:8px!important;
  z-index:9999!important;
  height:28px!important;
  min-width:56px!important;
  padding:0 12px!important;
  background:#ff5268!important;
  border:1px solid #ff8a9a!important;
  border-radius:4px!important;
  color:#fff!important;
  font-size:11px!important;
  font-weight:bold!important;
  display:flex!important;
  align-items:center!important;
  justify-content:center!important;
  gap:4px!important;
  cursor:pointer!important;
  opacity:1!important;
  box-shadow:0 2px 12px rgba(255,82,104,0.6)!important;
  pointer-events:auto!important;
}
.camera-live-btn::before{
  content:""!important;
  width:7px!important;
  height:7px!important;
  background:#fff!important;
  border-radius:50%!important;
  animation:liveBlinkFinal 1s infinite!important;
}
@keyframes liveBlinkFinal{
  0%,100%{opacity:1;}
  50%{opacity:0.3;}
}
/* 确保视频窗口可点击 */
.video-wall-feed{
  cursor:pointer!important;
  pointer-events:auto!important;
}
.video-wall-image{
  pointer-events:none!important;
}
.video-wall-live{
  pointer-events:none!important;
}
.video-wall-meta{
  pointer-events:none!important;
}
</style>'''

body_end = content.rfind('</body>')
content = content[:body_end] + final_css + content[body_end:]
print('[1] 最终CSS已添加')

with open(HTML, 'w', encoding='utf-8') as f:
    f.write(content)
print('完成')
