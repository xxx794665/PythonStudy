#encoding=utf-8

from PIL import Image
import argparse

#<--------------命令行输入参数处理---------------->

#创建解析对象
parser = argparse.ArgumentParser()

#在创建的对象中添加关注的命令行参数和选项
parser.add_argument('file') #输入文件
parser.add_argument('-o','--output') #输出文件


parser.add_argument('--width',type = int,default = 180) #输出字符画的宽度

parser.add_argument('--height',type = int,default = 120) #输出字符画的高度

#调用parse_args()方法进行解析


 
   args = parser.parse_args()

#使用
IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

#<-----------------处理图片-------------->

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

#字符与RGB的对应的映射关系
def get_char(r,g,b,alpha=256):
    if alpha == 0 :
        return ' '
    lenght = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1)/lenght
    return ascii_char[int(gray/unit)]

#如果是自己执行的话，就执行下面的，如果是作为导入模块就不执行
if __name__ == '__main__':
    im = Image.open(IMG)
    #这里是转换图片的大小，然后第二个参数表示图片的质量，一共有4种，低质量Image.NEARSET,双线性Image.BILINEAR，三次样条插值Image.BICUBIC，高质量Image.ANTIALIAS
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)
    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            #im.getpixel:根据坐标取得RGB对应的r，g，b三个值,这里的getpixel((i,j))的两个括号非常重要
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    print(txt)

#字符输出到文件
if OUTPUT:
    with open(OUTPUT,'w') as f:
        f.write(txt)
else:
    with open("output.txt",'w') as f:
        f.write(txt)
