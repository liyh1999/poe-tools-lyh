import pyautogui
from PIL import Image
import keyboard
initial_values = [1340, 600]#这是左上角的位置
result = []
i=0
x=0
y=0
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
keyboard.add_hotkey("q", toggle_run_script)

while True:
    if run_script:
        for coordinates in result:
            pyautogui.keyDown('alt')
            x, y = coordinates
            i = i + 1
            pyautogui.moveTo(x, y, duration=0.05)#鼠标移动到蓝图位置
            if i >= 36:  # 因为从背包第36个往后图像位置在最边缘了不会移动了，gtmdggglzzscl
                if (i - 36) % 5 == 0:
                    x, y = result[35]
                if (i - 36) % 5 == 1:
                    x, y = result[36]
                if (i - 36) % 5 == 2:
                    x, y = result[37]
                if (i - 36) % 5 == 3:
                    x, y = result[38]
                if (i - 36) % 5 == 4:
                    x, y = result[39]
            left = x - 300
            top = y - 200
            # 截取屏幕上指定区域的截图
            screenshot = pyautogui.screenshot(region=(left, top, 600, 150))
            # 保存截图
            screenshot.save(f".\screen\screenshot_{i}.png")
            print("截图已保存为screenshot.png")
            if i ==60:
                pyautogui.keyUp('alt')
                exit()
