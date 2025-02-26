"""
pip install pillow
Pillow 中最为重要的是Image类，可以通过Image模块的open函数来读取图像并获得Image类型的对象。
正常处理图片可以使用opencv进行处理
"""
import random

from PIL import Image, ImageFilter, ImageDraw, ImageFont


def pic_read():
    # 读取图像获得Image对象
    image = Image.open('D:\project\code\wiscom\单爱军\code\psmp_commonsimple_jiangbei\docs\架构.png')
    # 通过Image对象的format属性获得图像的格式
    print(image.format)  # JPEG
    # 通过Image对象的size属性获得图像的尺寸
    print(image.size)  # (500, 750)
    # 通过Image对象的mode属性获取图像的模式
    print(image.mode)  # RGB
    # 通过Image对象的show方法显示图像
    image.show()

def crop_image():
    image = Image.open('D:\project\code\wiscom\单爱军\code\psmp_commonsimple_jiangbei\docs\架构2.png')
    image.crop((0, 0, 100, 100)).show()

def thum_image():
    image = Image.open('D:\project\code\wiscom\单爱军\code\psmp_commonsimple_jiangbei\docs\架构2.png')
    image.thumbnail((100, 100))
    image.show()

def scale_and_paste_the_image():
    # 读取骆昊的照片获得Image对象
    luohao_image = Image.open('D:\project\code\wiscom\单爱军\code\psmp_commonsimple_jiangbei\docs\架构.png')
    # 读取吉多的照片获得Image对象
    guido_image = Image.open('D:\project\code\wiscom\单爱军\code\psmp_commonsimple_jiangbei\docs\架构2.png')
    # 从吉多的照片上剪裁出吉多的头
    guido_head = guido_image.crop((80, 20, 310, 360))
    width, height = guido_head.size
    # 使用Image对象的resize方法修改图像的尺寸
    # 使用Image对象的paste方法将吉多的头粘贴到骆昊的照片上
    # 这段代码的功能是将吉多的头像缩小1.5倍后粘贴到骆昊的照片上，具体位置为 (172, 40)。
    luohao_image.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))
    luohao_image.show()

def rotate_and_reverse():
    image = Image.open('D:\project\code\wiscom\单爱军\code\psmp_commonsimple_jiangbei\docs\架构.png')
    # 使用Image对象的rotate方法实现图像的旋转
    image.rotate(90).show()
    # 使用Image对象的transpose方法实现图像翻转
    # Image.FLIP_LEFT_RIGHT - 水平翻转
    # Image.FLIP_TOP_BOTTOM - 垂直翻转
    image.transpose(Image.FLIP_LEFT_RIGHT).show()

def manipulating_pixels():
    image = Image.open('D:\project\code\wiscom\单爱军\code\psmp_commonsimple_jiangbei\docs\架构.png')
    for x in range(80, 310):
        for y in range(20, 360):
            # 通过Image对象的putpixel方法修改图像指定像素点
            image.putpixel((x, y), (128, 128, 128))
    image.show()

def filter_effects():
    image = Image.open('D:\project\code\wiscom\单爱军\code\psmp_commonsimple_jiangbei\docs\架构.png')
    # 使用Image对象的filter方法实现滤镜效果
    # Image.BLUR - 模糊滤镜
    # Image.CONTOUR - 边缘检测滤镜
    # Image.DETAIL - 细节增强滤镜
    # Image.EDGE_ENHANCE - 边缘增强滤镜
    # Image.EDGE_ENHANCE_MORE - 更多边缘增强滤镜
    image.filter(ImageFilter.CONTOUR).show()

def draw_image():
    """
    模块的Draw函数会返回一个ImageDraw对象，
    通过ImageDraw对象的arc、line、rectangle、ellipse、polygon等方法，可以在图像上绘制出圆弧、线条、矩形、椭圆、多边形等形状，
    也可以通过该对象的text方法在图像上添加文字。
    :return:
    """
    width, height = 800, 600
    # 创建一个800*600的图像，背景色为白色
    image = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    # 创建一个ImageDraw对象
    drawer = ImageDraw.Draw(image)
    # 通过指定字体和大小获得ImageFont对象
    # font = ImageFont.truetype('Kongxin.ttf', 32)
    # 通过ImageDraw对象的text方法绘制文字
    # drawer.text((300, 50), 'Hello, world!', fill=(255, 0, 0), font=font)
    drawer.text((300, 50), 'Hello, world!', fill=(255, 0, 0))
    # 通过ImageDraw对象的line方法绘制两条对角直线
    drawer.line((0, 0, width, height), fill=(0, 0, 255), width=2)
    drawer.line((width, 0, 0, height), fill=(0, 0, 255), width=2)
    xy = width // 2 - 60, height // 2 - 60, width // 2 + 60, height // 2 + 60
    # 通过ImageDraw对象的rectangle方法绘制矩形
    drawer.rectangle(xy, outline=(255, 0, 0), width=2)
    # 通过ImageDraw对象的ellipse方法绘制椭圆
    for i in range(4):
        left, top, right, bottom = 150 + i * 120, 220, 310 + i * 120, 380
        drawer.ellipse((left, top, right, bottom), outline=random_color(), width=8)
    # 显示图像
    image.show()
    # 保存图像
    image.save('../../data/raw/result.png')

def random_color():
    """生成随机颜色"""
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue

if __name__ == '__main__':
    draw_image()