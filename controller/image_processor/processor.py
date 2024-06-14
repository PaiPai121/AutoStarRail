import cv2
import numpy as np
from PIL import Image
import os
# 指定原始图片的路径
image_path = 'assets/Interastral Guide/d2.png'

# 读取原始图片
image = cv2.imread(image_path)

# 创建一个新文件夹来保存截取的图片
output_folder = 'output_images2'
os.makedirs(output_folder, exist_ok=True)

tile_paths = []
# 9.33,5.17 2.32 2.32 * 2560/54
x0 = int(430)
y0 = int(230)
tile_size = int(109)
tile_interval = int(159)
def get_pic(x,y):
    sub_image = image[y:y+tile_size, x:x+tile_size]
    output_path = os.path.join(output_folder, f'tile_{len(tile_paths)}.png')
    cv2.imwrite(output_path, sub_image)
    tile_paths.append(output_path)
for i in range(0,5):
    get_pic(x0+i*tile_interval,y0)