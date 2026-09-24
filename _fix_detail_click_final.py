# -*- coding: utf-8 -*-
HTML = r'D:\天泽智联\大工贸\数智大脑\综合监管大屏.单位实时监测详情工作稿.html'
with open(HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 先去掉内联onclick，避免冲突
old = 'onclick="try{window.openVideoDetail(${company.id},${index+1})}catch(err){console.log(err);}" style="cursor:pointer;"'
new = 'style="cursor:pointer;"'

if old in content:
    content = content.replace(old, new)
    print('[1] 已去掉内联onclick')

# 2. 在body末尾加一个独立的script，用事件委托绑定点击
script = '''
<script id="video-wall-click-fix">
(function(){
  function init(){
    // 用事件委托，点击video-wall-feed时触发
    document.addEventListener('click', function(e){
      var feed = e.target.closest('.video-wall-feed');
      if(!feed) return;
      // 确保是在视频监管页面
      var videoPage = document.querySelector('#app>.content[data-tab-isolated="video"]');
      if(!videoPage || !videoPage.contains(feed)) return;
      
      var companyId = feed.dataset.videoWallRecord;
      var camera = feed.dataset.videoWallCamera || 1;
      
      try{
        if(typeof window.openVideoDetail === 'function'){
          window.openVideoDetail(companyId, camera);
        } else {
          console.log('openVideoDetail函数不存在');
        }
      }catch(err){
        console.error('打开视频详情失败:', err);
        alert('打开视频详情失败: ' + err.message);
      }
    });
    console.log('[视频详情] 点击事件已绑定');
  }
  
  if(document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
</script>'''

body_end = content.rfind('</body>')
content = content[:body_end] + script + content[body_end:]
print('[2] 事件委托script已添加')

with open(HTML, 'w', encoding='utf-8') as f:
    f.write(content)
print('完成')
