import cv2
import numpy as np
from PIL import ImageGrab

# # 截取屏幕图像
# screenshot = ImageGrab.grab()

# # 将PIL图像转换为OpenCV图像
# screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)


import cv2
import numpy as np

# 加载原始图像和模板
original_image = cv2.imread('./assets/interastral_guide/highlight.png')
template = cv2.imread('./assets/nameless_honor_tags/tile_0.png')
cv2.imshow('Match Result', original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 使用模板匹配
match_result = cv2.matchTemplate(original_image, template, cv2.TM_CCOEFF_NORMED)

# 查找匹配的最高值和位置
_, max_val, _, max_loc = cv2.minMaxLoc(match_result)

# 输出匹配的位置
print(f"Template found at position: {max_loc}")

# 显示匹配结果
cv2.imshow('Match Result', match_result)
cv2.waitKey(0)
cv2.destroyAllWindows()






def main():
    pass

if __name__ == "__main__":
    main()