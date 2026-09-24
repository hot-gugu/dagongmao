# -*- coding: utf-8 -*-
HTML = r'D:\天泽智联\大工贸\数智大脑\综合监管大屏.单位实时监测详情工作稿.html'
with open(HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 修复openCameraLive函数，把event作为参数传入
old_func = """function openCameraLive(btn,type){
  event.stopPropagation();
  event.preventDefault();
  var selector = type==='camera' ? '.camera-info strong' : '.video-wall-meta strong';
  var parent = type==='camera' ? '.camera' : '.video-wall-feed';
  var name = btn.closest(parent)?.querySelector(selector)?.textContent || '摄像头';
  openLiveModal(name + ' - 直播调阅');
}"""

new_func = """function openCameraLive(btn,type,e){
  if(e){e.stopPropagation();e.preventDefault();}
  var selector = type==='camera' ? '.camera-info strong' : '.video-wall-meta strong';
  var parent = type==='camera' ? '.camera' : '.video-wall-feed';
  var name = '摄像头';
  var parentEl = btn.closest(parent);
  if(parentEl){
    var nameEl = parentEl.querySelector(selector);
    if(nameEl) name = nameEl.textContent;
  }
  openLiveModal(name + ' - 直播调阅');
}"""

assert old_func in content, '未找到openCameraLive函数'
content = content.replace(old_func, new_func)
print('[1] openCameraLive函数已修复')

# 2. 修改按钮onclick，传入event
old_btn = "onclick=\"event.stopPropagation();openCameraLive(this,'wall')\""
new_btn = "onclick=\"openCameraLive(this,'wall',event)\""

if old_btn in content:
    content = content.replace(old_btn, new_btn)
    print('[2] 按钮onclick已更新')

# 3. 给视频详情加一个简单的包装函数，确保能执行
old_detail = 'onclick="window.openVideoDetail(${company.id},${index+1})"'
new_detail = 'onclick="try{window.openVideoDetail(${company.id},${index+1})}catch(err){console.log(err);}"'

if old_detail in content:
    content = content.replace(old_detail, new_detail)
    print('[3] 视频详情加了错误捕获')

with open(HTML, 'w', encoding='utf-8') as f:
    f.write(content)
print('完成')
