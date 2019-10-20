from PIL import Image
from selenium import webdriver

url = 'https://weixin.sogou.com/antispider/?from=http%3A%2F%2Fweixin.sogou.com%2Fweixin%3Ftype%3D2%26query%3Dpython'
driver = webdriver.Chrome()
driver.maximize_window()  # 将浏览器最大化
driver.get(url)
# 截取当前网页并放到D盘下命名为printscreen，该网页有我们需要的验证码
driver.save_screenshot('printscreen.png')
imgelement = driver.find_element_by_id('seccodeImage')  # 定位验证码
location = imgelement.location  # 获取验证码x,y轴坐标
print(location)
size = imgelement.size  # 获取验证码的长宽
print(size)
rangle = (int(location['x'] + 110), int(location['y'] + 60), int(location['x'] + size['width'] + 165),
          int(location['y'] + size['height'] + 90))  # 写成我们需要截取的位置坐标
i = Image.open("printscreen.png")  # 打开截图
frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
frame4 = frame4.convert('RGB')
frame4.save('save.jpg')  # 保存我们接下来的验证码图片 进行打码

driver.close()
