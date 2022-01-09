import os
from PIL import Image

#通过os库获得文件名列表
filename = os.listdir(".\\firework01")
#图片文件夹路径
base_dir = ".\\firework01\\"
#新图片文件夹路径
new_dir  = ".\\firework\\"
#新图片尺寸
size_m = 45
size_n = 45
 
for img in filename:
#    print(img)
    #更改尺寸
    image = Image.open(base_dir + img)
    image_size = image.resize((size_m, size_n),Image.ANTIALIAS)
    #更改格式
    name,g = img.split('.')
    new = name + ".gif"
    #保存
    image_size.save(new_dir+ new)
