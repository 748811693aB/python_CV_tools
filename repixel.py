##本程序用来批量设置图片尺寸
import os
from PIL import Image
fileName1= r"E:\209laboratory\6-6\model\badmintondatasets\images\\"
fileName2= r"E:\209laboratory\6-6\model\badmintondatasets\images2\\" #创建一个新的文件夹存放改变尺寸后的图片
fileName = os.listdir(fileName1) #将文件夹中的图片名称存入 fileName 中
width = 180 #修改图片的宽度
height = 320 #修改图片的高度
os.mkdir(fileName2)
for img in fileName:
    pic = Image.open(fileName1 + img)
    newpic = pic.resize((width, height),Image.ANTIALIAS) #通过循环结构批量修改
    print (newpic)
    newpic.save(fileName2+img)