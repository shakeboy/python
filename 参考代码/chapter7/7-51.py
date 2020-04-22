import imageio,os,numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

tiger_jpg=imageio.imread(os.getcwd()+"\\resource\\tiger.jpg")    #读取图片.
print("图片的数据类型:", tiger_jpg.dtype)                                   #获取图片数据类型.
img_shape = tiger_jpg.shape                                                   #获取图片大小.
print("(图片大小, 通道数):", tiger_jpg.shape)
imageio.imwrite("tiger_mc.jpg", tiger_jpg * [1, 0.5, 0.5] )  #修改图片颜色并保存.
imageio.imwrite("timg_ms.jpg",numpy.array(Image.fromarray(tiger_jpg).resize
((120,70))))                                                                 #修改图片大小并保存.
imageio.imwrite("timg_mi.jpg", tiger_jpg[50:130, 100:240])    #裁剪图片并保存.
"""-------------------------绘制图片--------------------------"""
plt.figure()
plt.subplot(2, 2, 1)
tiger_jpg1 = mpimg.imread(os.getcwd()+"\\resource\\tiger.jpg")        #读取图片.
plt.imshow(tiger_jpg1)                                                               #显示图片.
plt.axis('off')
plt.subplot(2, 2, 2)
tiger_jpg2 = mpimg.imread("tiger_mc.jpg")
plt.imshow(tiger_jpg2)
plt.axis('off')
plt.subplot(2, 2, 3)
tiger_jpg3 = mpimg.imread("timg_ms.jpg")
plt.imshow(tiger_jpg3)
plt.axis('off')
plt.subplot(2, 2, 4)
tiger_jpg4 = mpimg.imread("timg_mi.jpg")
plt.imshow(tiger_jpg4)
plt.axis('off')
plt.show()
