import pyautogui
import time
import keyboard
import pyperclip
initial_values = [1340, 600]#这是左上角的位置
result = []
for _ in range(60):
    result.append(initial_values.copy())
    initial_values[1] += 50
    if _ % 5 == 4:
        initial_values[0] += 50
        initial_values[1] = 600
run_script = False
def toggle_run_script():
    global run_script
    run_script = not run_script
keyboard.add_hotkey("t", toggle_run_script)

while True:
    if run_script:
        for coordinates in result:
            x, y = coordinates
            # 移动鼠标到坐标位置
            pyautogui.moveTo(x, y, duration=0.05)
            # 模拟按下Ctrl+C（复制操作）
            pyautogui.hotkey('ctrl', 'c')
            # 读取剪切板内容
            clipboard_text = pyperclip.paste()
            # 如果'泥滩'不在剪切板内容中
            while ('赤红' not in clipboard_text and '远古' not in clipboard_text and  '剧毒' not in clipboard_text and '城中' not in clipboard_text):
                # 移动到(580, 460)位置，右键点击
                pyautogui.moveTo(580, 400, duration=0.05)
                pyautogui.click(button='right')
                # 移动到坐标位置，左键点击
                pyautogui.moveTo(x, y, duration=0.05)
                pyautogui.click(button='left')
                # 等待0.05秒
                time.sleep(0.05)
                # 模拟按下Ctrl+C（复制操作）
                pyautogui.hotkey('ctrl', 'c')
                # 读取剪切板内容
                clipboard_text = pyperclip.paste()