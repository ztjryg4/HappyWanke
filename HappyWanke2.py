# -*- coding: utf-8 -*-
import win32api,win32con
import time
from pymouse import PyMouse
from pykeyboard import PyKeyboard

print("程序启动成功，请确认玩课网视频播放页面处于最大化且可见状态。\n")
mouse = PyMouse()
keyboard = PyKeyboard()

x_dim = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
y_dim = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
print("屏幕大小获取成功：X轴大小%d, Y轴大小%d。\n" %(x_dim,y_dim))
print("接下来需要确定“下一节”按钮、播放速度调整按钮、二倍速播放按钮的位置。\n")
print("首先确定“下一节”按钮位置，请将鼠标移动到“下一节”按钮上，十秒后程序将自动读取按钮坐标。")
for i in range(0,10):
    rt = 10-i
    print("%d" % rt)
    time.sleep(1)
x_click, y_click = mouse.position()
print("已确定“下一节”按钮位置：X轴位置%d, Y轴位置%d。\n" %(int(x_click),int(y_click)))

print("接下来确定播放速度调整按钮位置，请将鼠标移动到播放速度调整按钮按钮上，十秒后程序将自动读取按钮坐标。")
for i in range(0,10):
    rt = 10-i
    print("%d" % rt)
    time.sleep(1)
x_double_pre, y_double_pre = mouse.position()
print("已确定播放速度调整按钮位置：X轴位置%d, Y轴位置%d。\n" %(int(x_double_pre),int(y_double_pre)))

print("最后确定二倍速播放按钮位置，请将鼠标移动到二倍速播放按钮上，十秒后程序将自动读取按钮坐标。")
for i in range(0,10):
    rt = 10-i
    print("%d" % rt)
    time.sleep(1)
x_double, y_double = mouse.position()
print("已确定二倍速播放按钮位置：X轴位置%d, Y轴位置%d。\n" %(int(x_double),int(y_double)))

print("接下来请输入程序点击“下一节”按钮的间隔时间，单位为分钟。请注意本程序会自动二倍速播放视频。\n例如：若单节课程视频一般不超过15分钟，二倍速播放单节视频一般不超过7.5分钟，则可设置间隔时间为7.5分钟，程序将每隔7.5分钟点击下一节。")
sleep_time = float(input("请输入间隔分钟数："))
cnt = 0

while(1):
    mouse.click(int(x_click), int(y_click), 1)
    mouse.move(int(x_double_pre),int(y_double_pre))
    time.sleep(1)
    mouse.click(int(x_double),int(y_double), 1)
    print("已调整播放速度为二倍速。")
    cnt = cnt +1
    print("已完成第%d次点击\n" % cnt)
    time.sleep(int(sleep_time*60))