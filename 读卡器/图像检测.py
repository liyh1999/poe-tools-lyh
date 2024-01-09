import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # 放ocr的地方，必须得下载这个才能做图像识别
# Function to find the icon image within the main image
def find_icon(main_image, icon_image, threshold):
    # Convert images to grayscale
    main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
    icon_gray = cv2.cvtColor(icon_image, cv2.COLOR_BGR2GRAY)
    # Apply template matching
    res = cv2.matchTemplate(main_gray, icon_gray, cv2.TM_CCOEFF_NORMED)
    # Threshold for detection
    loc = np.where(res >= threshold)
    # Create a list to hold all detected rectangles
    rectangles = []
    w, h = icon_gray.shape[::-1]
    for pt in zip(*loc[::-1]):  # Switch columns and rows
        rectangles.append([int(pt[0]), int(pt[1]), w, h])
        rectangles.append([int(pt[0]), int(pt[1]), w, h])  # Duplicate the rectangle
    # Aply group rectangles to combine overlapping rectangles
    rectangles, _ = cv2.groupRectangles(rectangles, 1, 0.5)
    return rectangles
# Read the images
# Find the icon in the main image with the specified threshold
threshold = 0.65#0.65个人检测刚刚好，完美！
for i in range(1,60):
    file=f".\screen\screenshot_{i}.png"
    main_image_cv = cv2.imread(file)
    icon_image_cv = cv2.imread('mingyunka.png')
    rectangles = find_icon(main_image_cv, icon_image_cv, threshold)
    # 画出红框标记
    for (x, y, w, h) in rectangles:#x,y,w,h是匹配到的区域的位置
       cv2.rectangle(main_image_cv, (x-35, y), (x-35+ w, y + h), (0, 0, 255), 2)#40和30的经验参数我自己检查了一下应该没问题
    #这个框就是左上角坐标(x-40,y),右下角坐标(x-30+w,y+h)
       left_top_x = x - 35
       left_top_y = y
       right_bottom_x = x - 35 + w
       right_bottom_y = y + h
    # 提取矩形框内的区域
       roi = main_image_cv[left_top_y:right_bottom_y, left_top_x:right_bottom_x]
       #灰度化
       gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
       # 二值化
       # 使用 pytesseract 进行 OCR
       # 配置参数以优化数字识别
       custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789/'
       text = pytesseract.image_to_string(gray, config=custom_config)
       print('第'+str(i)+"张蓝图中的命运卡数量是",text)
    #存储结果
    # output_path = f".\cheak\chkak_{i}.png"
    # cv2.imwrite(output_path, main_image_cv)


