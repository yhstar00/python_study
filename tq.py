
import os
from PIL import Image
from PIL import ImageFile

# 跳过“损坏”图片
ImageFile.LOAD_TRUNCATED_IMAGES = True


# 用于判断哪里放图片，哪里放空白图像
def images_position(x, y):
    if x == 0 and y in [1, 2, 6, 7]:
        return True
    elif x == 1 and y not in [3, 4, 5]:
        return True
    elif x == 2 and y != 4:
        return True
    elif x in [3, 4]:
        return True
    elif x >= 5 and (x - 5) < y < (13 - x):
        return True
image_list = os.listdir(r"C:\Users\Administrator\Desktop\0420\123")

# 定义正方形照片墙的边长
lines = 9
# 定义一个新的照片墙
heart_image = Image.new('RGB', (192 * lines, 192 * lines))
# 定义宽和高两个参数
row = col = 0
for side in range(lines * lines):
    # 判断该放图片还是空白图
    print(image_list[side])
    if images_position(col, row):
        # 读取图像，这里素材是用爬虫爬取的，命名已经有规律了，直接读取
        img = Image.open("C:/Users/Administrator/Desktop/0420/123/{}".format(image_list[side]))
        # 调整图片大小
        img = img.resize((192, 192), Image.ANTIALIAS)
    else:
        # 空白图像
        img = Image.new("RGB", (192, 192), (255, 255, 255))
    # 往照片墙上粘贴照片
    heart_image.paste(img, (row * 192, col * 192))
    col += 1
    if col == lines:
        col = 0
        row += 1
    # 行数等于列数，跳出循环
    if row == col == lines:
        break
heart_image.show()
#heart_image.save("C:/Users/Administrator/Desktop/0420/heart_image.png")
