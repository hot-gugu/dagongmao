# -*- coding: utf-8 -*-
HTML = r'D:\天泽智联\大工贸\数智大脑\综合监管大屏.单位实时监测详情工作稿.html'
with open(HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 把cameraCard里的复杂onclick改成简单函数调用
old1 = 'onclick="event.stopPropagation();event.preventDefault();openLiveModal((this.closest(\'.camera\')?.querySelector(\'.camera-info strong\')?.textContent||\'摄像头\')+\' - 直播调阅\')"'
new1 = 'onclick="openCameraLive(this,\'camera\')"'

if old1 in content:
    content = content.replace(old1, new1)
    print('[1] cameraCard onclick已简化')

# 2. 把video-wall-feed里的复杂onclick改成简单函数调用
old2 = 'onclick="event.stopPropagation();event.preventDefault();openLiveModal((this.closest(\'.video-wall-feed\')?.querySelector(\'.video-wall-meta strong\')?.textContent||\'摄像头\')+\' - 直播调阅\')"'
new2 = 'onclick="openCameraLive(this,\'wall\')"'

if old2 in content:
    content = content.replace(old2, new2)
    print('[2] video-wall onclick已简化')

# 3. 在openLiveModal函数旁边加一个openCameraLive函数
old_func = "function openLiveModal(camName){"
new_func = """function openCameraLive(btn,type){
  event.stopPropagation();
  event.preventDefault();
  var selector = type==='camera' ? '.camera-info strong' : '.video-wall-meta strong';
  var parent = type==='camera' ? '.camera' : '.video-wall-feed';
  var name = btn.closest(parent)?.querySelector(selector)?.textContent || '摄像头';
  openLiveModal(name + ' - 直播调阅');
}
function openLiveModal(camName){"""

if old_func in content:
    content = content.replace(old_func, new_func)
    print('[3] openCameraLive函数已添加')

with open(HTML, 'w', encoding='utf-8') as f:
    f.write(content)
print('完成')
