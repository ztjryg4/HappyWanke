# HappyWanke
## 概要
HappyWanke项目主要用于自动播放玩课网的课程视频。  
**本项目的实现方式为鼠标模拟点击。未来计划通过js脚本的方式更优雅地实现相同功能。**
## 使用方法
Windows用户可直接下载HappyWanke2.exe。也可安装pywin32及pyHook依赖后通过python运行HappyWanke2.py。<br>
macOS用户可安装Quartz及AppKit依赖后通过python运行HappyWanke2.py。<br>
Linux用户可安装Xlib(python-xlib)依赖后通过python运行HappyWanke2.py。<br>
*macOS及Linux系统未进行测试。*
### 第一步 确定按钮位置
程序运行后首先需要确定“下一节”按钮、播放速度调整按钮、二倍速播放按钮的位置。<br>
![按钮位置指示](https://github.com/ztjryg4/HappyWanke/raw/master/image/introduction.png)
首先将鼠标移至“下一节”按钮位置，10秒后程序将自动读取坐标。<br>
再将鼠标移至播放速度调整按钮位置，10秒后程序将自动读取坐标。<br>
最后将鼠标移至二倍速播放按钮位置，10秒后程序将自动读取坐标。<br>
不必担心10秒等待时间内进度条消失的问题，确定按钮位置即可。
### 第二步 输入间隔时间
接下来需要输入程序点击“下一节”按钮的间隔时间，单位为分钟。HappyWanke会自动二倍速播放视频。<br>
例如：若单节课程视频一般不超过15分钟，二倍速播放单节视频一般不超过7.5分钟，则可设置间隔时间为7.5分钟，程序将每隔7.5分钟点击下一节。
### 第三步
没有第三步了，把玩课交给HappyWanke吧。
## 说明
**HappyWanke及程序作者不鼓励使用HappyWanke逃避学习任务的行为。**
## 捐助
欢迎通过领取支付宝花呗红包或请我吃鸡排的方式支持HappyWanke。
![捐助](https://github.com/ztjryg4/HappyWanke/raw/master/image/donate.png)
