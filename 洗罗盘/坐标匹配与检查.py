import tkinter as tk
import pyautogui

def update_mouse_position():
    x, y = pyautogui.position()
    mouse_position_label.config(text=f"鼠标坐标: ({x}, {y})")
    position_window.geometry(f"+{x+10}+{y+10}")
    position_window.after(100, update_mouse_position)

root = tk.Tk()
root.withdraw()  # 隐藏主窗口

position_window = tk.Toplevel(root)
position_window.overrideredirect(True)  # 创建无边框窗口
position_window.attributes("-topmost", True)  # 窗口保持在最顶层

mouse_position_label = tk.Label(position_window, text="")
mouse_position_label.pack()

update_mouse_position()
root.mainloop()
