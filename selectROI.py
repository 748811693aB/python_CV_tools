# 1.17 图像的裁剪 (ROI)
import os
from PIL import Image
fileName1= r"E:\209laboratory\6-6\model\badmintondatasets\images2\\"
fileName2= r"E:\209laboratory\6-6\model\badmintondatasets\images3\\" #创建一个新的文件夹存放改变尺寸后的图片
fileName = os.listdir(fileName1) #将文件夹中的图片名称存入 fileName 中
os.mkdir(fileName2)

for img in fileName:
    pic = Image.open(fileName1 + img)
    imgCut = pic.crop((0, 0, 244, 244))
    imgCut.save(fileName2+img)
  







