import threading
import keyboard
import time
from 重构的自动存洗罗盘 import 拓印罗盘,按下键盘右键,按下键盘左键,全程处理
# 全局变量来控制脚本运行
import threading
import keyboard
import time

# 全局变量来控制脚本运行
running = False

def automation_task():
    while True:
        if running:
            # 这里放置您的自动化操作代码
            全程处理()
        else:
            time.sleep(0.1)  # 当脚本不运行时，线程休息以降低CPU占用

def toggle_run_script():
    global running
    running = not running  # 切换脚本的运行状态
    if not running:
        keyboard.release('ctrl')
        keyboard.release('shift')
        print("Ctrl和Shift键已释放")

def listen_for_keys():
    keyboard.add_hotkey('esc', toggle_run_script)
    keyboard.add_hotkey('q', toggle_run_script)
    keyboard.wait('esc')

# 创建自动化操作线程
automation_thread = threading.Thread(target=automation_task)
automation_thread.start()

# 键盘监听线程在主线程中运行
listen_for_keys()

# 等待线程结束（这种情况下实际上不会发生，因为keyboard.wait会阻塞）
automation_thread.join()
