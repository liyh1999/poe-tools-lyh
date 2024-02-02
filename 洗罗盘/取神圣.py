import pyautogui
import time
import keyboard
import pyperclip
#560，340，神圣的位置
initial_values = [1340, 600]#这是左上角的位置
result = []
for _ in range(60):
    result.append(initial_values.copy())
    initial_values[1] += 50
    if _ % 5 == 4:
        initial_values[0] += 50
        initial_values[1] = 600
#移动到神圣位置，按下shift+鼠标左键，按下位移右键，移动到背包位置，按下鼠标左键
run_script = False
def toggle_run_script():
    global run_script
    run_script = not run_script
keyboard.add_hotkey("t", toggle_run_script)
while True:
    if run_script:
        for i in result:
            pyautogui.moveTo(560, 340, duration=0.05)
            pyautogui.keyDown('shift')
            pyautogui.click(button='left')
            pyautogui.keyUp('shift')
            pyautogui.press('right')
            pyautogui.press('enter')
            pyautogui.moveTo(i, duration=0.05)
            pyautogui.click(button='left')


