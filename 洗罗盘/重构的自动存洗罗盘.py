import pyautogui
import keyboard
import time
import pyperclip
detection_word = ['保险箱','暴怒','庄稼','庄园','塑界','裂界','征服者','词缀腐化','深渊','迷雾','镀金','符纹','基底词缀','走私者','更强大','进度']#罗盘检测词
#(370,600)是六分仪的位置，(400,400)是仓库里正常的六分仪的位置(900,880)是石头的位置,(460,600)是放测绘罗盘的位置，（1500，600）是放拿出来的充能罗盘的位置
def 拓印罗盘():
    pyautogui.moveTo(460, 600)
    pyautogui.click(button='right')
    time.sleep(0.05)
    pyautogui.moveTo(900, 880)
    pyautogui.click(button='left')
    time.sleep(0.05)
    pyautogui.moveTo(1500, 600)
    pyautogui.click(button='left')
    time.sleep(0.05)
def 按下键盘右键(times):
    for _ in range(times):
        pyautogui.press('right')
        time.sleep(0.05)
def 按下键盘左键(times):
    for _ in range(times):
        pyautogui.press('left')
        time.sleep(0.05)
def 存进仓库():
    pyautogui.moveTo(1500, 600)
    time.sleep(0.05)
    pyautogui.keyDown('ctrl')  # 按住ctrl不放
    pyautogui.click(button='left')
    time.sleep(0.05)
    pyautogui.keyUp("ctrl")  # 释放ctrl键
def 全程处理():
    判断词=True
    # 移动鼠标到六分仪并点击右键
    pyperclip.copy('')#清空剪切板
    pyautogui.moveTo(400, 400)
    pyautogui.keyDown('shift')#按住shift
    pyautogui.click(button='right')#按下右键取出六分仪
    time.sleep(0.1)
    pyautogui.moveTo(900, 880)
    time.sleep(0.1)
    while 判断词:
        pyautogui.click(button='left')
        time.sleep(0.1)
        keyboard.press_and_release('ctrl+c')
        time.sleep(0.05)
        clipboard_content = pyperclip.paste()
        time.sleep(0.05)
        for i in detection_word:
            if i in clipboard_content:
                判断词= False
    pyautogui.keyUp("shift")  # 释放shift
    if '走私' in clipboard_content:

        拓印罗盘()
        按下键盘右键(1)
        存进仓库()
        按下键盘左键(1)
    if '保险箱已被腐化' in clipboard_content:

        拓印罗盘()
        按下键盘右键(2)
        存进仓库()
        按下键盘左键(2)
    if '更强大' in clipboard_content:
        拓印罗盘()
        按下键盘右键(3)
        存进仓库()
        按下键盘左键(3)
    if '深渊' in clipboard_content:

        拓印罗盘()
        按下键盘右键(4)
        存进仓库()
        按下键盘左键(4)
    if '暴怒' in clipboard_content:

        拓印罗盘()
        按下键盘右键(5)
        存进仓库()
        按下键盘左键(5)
    if '庄园' in clipboard_content:

        拓印罗盘()
        按下键盘右键(6)
        存进仓库()
        按下键盘左键(6)
    if '迷雾之镜' in clipboard_content:

        拓印罗盘()
        按下键盘右键(7)
        存进仓库()
        按下键盘左键(7)
    if '词缀腐化' in clipboard_content:

        拓印罗盘()
        按下键盘右键(8)
        存进仓库()
        按下键盘左键(8)
    if '镀金' in clipboard_content:

        拓印罗盘()
        按下键盘右键(9)
        存进仓库()
        按下键盘左键(9)
    if '进度加快' in clipboard_content:

        拓印罗盘()
        按下键盘右键(10)
        存进仓库()
        按下键盘左键(10)
    if '伤害总增' in clipboard_content:

        拓印罗盘()
        按下键盘右键(11)
        存进仓库()
        按下键盘左键(11)
    if '符纹' in clipboard_content:

        拓印罗盘()
        按下键盘右键(12)
        存进仓库()
        按下键盘左键(12)
    if '非传奇夺宝' in clipboard_content:

        拓印罗盘()
        按下键盘右键(13)
        存进仓库()
        按下键盘左键(13)
run_script = False
def toggle_run_script():
    global run_script
    run_script = not run_script
keyboard.add_hotkey("q", toggle_run_script)
keyboard.add_hotkey("esc", toggle_run_script)
print("按 'q' 启动/停止，按 'esc' 退出")
while True:
    if run_script:
        全程处理()


