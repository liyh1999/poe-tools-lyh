import pyautogui
import time
import keyboard
initial_values = [1340, 600]#这是左上角的位置
result = []
for _ in range(60):
    result.append(initial_values.copy())
    initial_values[1] += 50
    if _ % 5 == 4:
        initial_values[0] += 50
        initial_values[1] = 600
# 定义起始格子的坐标
start_x, start_y = 60, 300
# 定义每个格子的坐标差
delta = 40
# 定义行数和列数
rows, cols = 6, 12  # 例如，这里我们假设有5行4列的格子
# 初始化格子位置列表
grid_positions = []
# 生成每个格子的中心位置坐标
for row in range(rows):
    for col in range(cols):
        # 计算当前格子的中心坐标
        x = start_x + col * delta
        y = start_y + row * delta
        # 将坐标添加到列表中
        grid_positions.append((x, y))
run_script = False
def toggle_run_script():
    global run_script
    run_script = not run_script
keyboard.add_hotkey("t", toggle_run_script)
while True:
    if run_script:
        for i in range(1,60):
            pyautogui.moveTo(result[i], duration=0.05)
            pyautogui.click(button='left')
            pyautogui.moveTo(grid_positions[i], duration=0.05)
            pyautogui.click(button='left')

