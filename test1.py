from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')
baidu_img = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.index-logo-src'))
)
driver.save_screenshot("screenshot.png")  # 对整个浏览器页面进行截图
left = baidu_img.location['x']
top = baidu_img.location['y']
right = baidu_img.location['x'] + baidu_img.size['width']
bottom = baidu_img.location['y'] + baidu_img.size['height']

im = Image.open('screenshot.png')
im = im.crop((left, top, right, bottom))  # 对浏览器截图进行裁剪
im.save('baidu.png')
driver.quit()
print("爬取完成")
