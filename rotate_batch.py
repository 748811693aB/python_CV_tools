import os
from PIL import Image

def read_path(file_pathname):                       # 函数的输入是图片所在的路径
    for filename in os.listdir(file_pathname):
        print(filename)                             # 所操作图片的名称可视化
        img = Image.open(file_pathname+'/'+filename)            # 读取文件
        im_rotate = img.rotate(45)                              #图像旋转
        im_rotate.save(r"E:\209laboratory\dataset\k210datasets\k210datasets\images\7_rotate\r+315" + "/" + filename)  # 图片保存

read_path(r"E:\209laboratory\dataset\k210datasets\k210datasets\images\7_rotate")
