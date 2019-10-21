from selenium import webdriver
import time
from PIL import Image
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from util import Util
import re
from util.BaiduApiUtil import BaiDuApi


def search(name, id_num):
    name_input = driver.find_element_by_xpath("//input[@id='ctl00_ContentPlaceHolder1_txtPersonName']")
    name_input.clear()
    name_input.send_keys(name)
    num_input = driver.find_element_by_xpath("//input[@id='ctl00_ContentPlaceHolder1_txtIdnum']")
    num_input.clear()
    num_input.send_keys(id_num)
    search_btn = driver.find_element_by_xpath("//input[@id='ctl00_ContentPlaceHolder1_btnSearch']")
    verification_code_input = driver.find_element_by_xpath("//input[@id='ctl00_ContentPlaceHolder1_txtCheckCode']")
    verification_code = driver.find_element_by_xpath("//a/img[@id='CheckCodeImage']")
    driver.save_screenshot("screenshot.png")
    location = verification_code.location
    size = verification_code.size
    x = location["x"]
    y = location["y"]
    width = size["width"]
    height = size["height"]
    range = (int(x + 160), int(y + 90), int(x + width + 165),
             int(y + height + 85))
    # im = im.crop((left, top, right, bottom))
    im = Image.open("screenshot.png")
    im = im.crop(range)
    im = im.convert("RGB")
    im.save("code.png")
    api = BaiDuApi()
    code = api.read_image("code.png")
    # code = "test"
    verification_code_input.send_keys(code)
    search_btn.click()
    driver.switch_to.alert.accept()
    search(name, id_num)


def get_result(html_str):
    html_str = re.sub('\s+', '', html_str).strip().replace("<tr>", "") \
        .replace("</tr>", "").replace("/", "").split("<td>")
    certificate_name = html_str[1]
    level = html_str[3]
    licence_issuing = html_str[5]
    date = html_str[7]
    validity = html_str[9]
    return certificate_name, level, licence_issuing, date, validity


util = Util.Util()
driver = webdriver.Chrome()
url = "http://113.108.219.40/Dop/Open/PersonList.aspx"
driver.implicitly_wait(10)
driver.maximize_window()
driver.get(url)
time.sleep(1)
try:
    search("韦聪", "440102198311083621")
except NoAlertPresentException as e:
    pass

result_list = driver.find_elements_by_xpath("//table[@class='data-list']/tbody/tr/td/a")
index_handle = driver.current_window_handle
for index, item in enumerate(result_list):
    time.sleep(1)
    item.click()
    util.switch_to_new_window(driver, index_handle)
    company_div = driver.find_element_by_xpath("//div[@class='spec-item-4'][4]/div[@class='spec-item']/h5/a")
    company = company_div.get_attribute("innerHTML")
    print(company)
    infor_div = driver.find_elements_by_xpath("//table[@class='data-list']/tbody/tr")
    for index1, item1 in enumerate(infor_div):
        if index1 is not 0:
            infor = item1.get_attribute("outerHTML")
            print(get_result(infor))
    driver.close()
    driver.switch_to.window(index_handle)

driver.quit()
