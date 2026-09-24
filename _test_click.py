# -*- coding: utf-8 -*-
HTML = r'D:\天泽智联\大工贸\数智大脑\综合监管大屏.单位实时监测详情工作稿.html'
with open(HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 先替换成最简单的测试代码，确认点击事件能不能触发
old_script_start = '<script id="video-wall-click-fix">'
old_script_end = '</script>'

# 找到并删除旧的script
start_idx = content.find(old_script_start)
if start_idx >= 0:
    end_idx = content.find(old_script_end, start_idx) + len(old_script_end)
    content = content[:start_idx] + content[end_idx:]
    print('[1] 旧script已删除')

# 加最简单的测试script
test_script = '''
<script id="video-click-test">
(function(){
  function bindClick(){
    console.log('=== 开始绑定视频点击事件 ===');
    
    // 监听所有点击
    document.addEventListener('click', function(e){
      var target = e.target;
      console.log('点击元素:', target);
      
      var feed = target.closest('.video-wall-feed');
      if(feed){
        console.log('✓ 找到video-wall-feed:', feed);
        console.log('  data-video-wallRecord:', feed.dataset.videoWallRecord);
        
        // 先弹个alert确认事件触发了
        alert('点击成功！\\n企业ID: ' + feed.dataset.videoWallRecord + '\\n摄像头号: ' + feed.dataset.videoWallCamera);
        
        // 然后尝试打开详情
        try{
          if(typeof window.openVideoDetail === 'function'){
            console.log('调用openVideoDetail...');
            window.openVideoDetail(feed.dataset.videoWallRecord, feed.dataset.videoWallCamera);
          } else {
            alert('错误: openVideoDetail函数不存在');
          }
        }catch(err){
          alert('打开详情出错: ' + err.message);
          console.error(err);
        }
      }
    }, true);  // 用捕获阶段，确保最先执行
    
    console.log('=== 视频点击事件绑定完成 ===');
  }
  
  if(document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', bindClick);
  } else {
    bindClick();
  }
})();
</script>'''

body_end = content.rfind('</body>')
content = content[:body_end] + test_script + content[body_end:]
print('[2] 测试script已添加')

with open(HTML, 'w', encoding='utf-8') as f:
    f.write(content)
print('完成')
