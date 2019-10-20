import time
import re
import os
import string
import random
import datetime


class Util(object):
    DELAY_TIME = 2  # 操作延迟时间
    KEY_LEN = 10
    LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    file_path = ''

    def __init__(self, file_path=""):
        self.file_path = os.path.realpath(file_path)

    def is_element_exist(self, driver, css):
        try:
            driver.find_element_by_css_selector(css)
            return True
        except:
            return False

    def check_content(self, matcher, string):  # TODO 检查.replace("(", "\(").replace(")", "\)")
        return re.search(str(matcher).replace("(", "\(").replace(")", "\)"), str(string))

    def get_current_time(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def base_str(self):
        return self.LETTERS + string.digits

    def get_random_str(self):
        key_list = [random.choice(self.base_str()) for i in range(self.KEY_LEN)]
        return "".join(key_list)

    def GBK2312(self):
        head = random.randint(0xb0, 0xf7)
        body = random.randint(0xa1, 0xf9)  # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
        val = f'{head:x}{body:x}'
        str = bytes.fromhex(val).decode('gb2312')
        return str

    def get_random_chinese(self):
        temp = []
        i = 0
        while i < 10:
            temp.append(self.GBK2312())
            i += 1
        return ''.join(temp)

    def get_random_chinese_by_length(self, length):
        temp = []
        i = 0
        str_length = random.randint(5, length)
        while i < str_length:
            temp.append(self.GBK2312())
            i += 1
        return ''.join(temp)

    def get_random_num_str(self, n):
        str = ""
        for i in range(n):
            ch = chr(random.randrange(ord('0'), ord('9') + 1))
            str += ch
        return str

    def get_num_in_str(self, string):
        str1 = filter(str.isdigit, string)
        num_str = ''
        for item in str1:
            num_str += item
        return int(num_str)

    def replace_str(self, string, old_string, new_string):
        return string.replace(old_string, new_string)

    def cut_first_str(self, string, key):
        index = string.find(key)
        return string[0:index]

    def cut_between_str(self, string, key1, key2):
        index1 = string.find(key1)
        index2 = string.find(key2)
        return string[index1 + 1:index2]

    def cut_between_str_1(self, string, key1, key2):
        index1 = string.find(key1)
        string = string[index1 + len(key1):]
        index2 = string.find(key2)
        return string[:index2]

    def cut_between_str_by_order(self, string, key1, order1, key2, order2):
        for e in range(order1):
            index1 = string.find(key1)
            string = string[index1 + len(key1):]
        index2 = 0
        for e in range(order2):
            if e == 0:
                index4 = string.find(key2)
            else:
                index4 = string.find(key2, index2 + 1)
            index2 = index4
        return string[:index2]

    def switch_to_new_window(self, driver, current_handle):
        all_handles = driver.window_handles  # 获取全部页面句柄
        for handle in all_handles:  # 遍历全部页面句柄
            if handle != current_handle:  # 判断条件
                driver.switch_to.window(handle)  # 切换到新页面

    def is_equal_date_str(self, date_str1, date_str2):
        strf_date1 = datetime.datetime.strptime(date_str1, "%Y-%m-%d")
        strf_date2 = datetime.datetime.strptime(date_str2, "%Y-%m-%d")
        if strf_date1 == strf_date2:
            return True
        else:
            return False

    def alter_date_str_by_day(self, date_str, add_date=0, reduce_day=0):
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return (datetime.datetime(date.year, date.month, date.day) + datetime.timedelta(
            days=add_date) - datetime.timedelta(
            days=reduce_day)).strftime("%Y-%m-%d")

    def compare_date_str(self, date_str1, date_str2):
        """
        :param date_str1:
        :param date_str2:
        :return: earlier return -1,equal return 0,later return 1
        """
        strf_time1 = datetime.datetime.strptime(date_str1, "%Y-%m-%d")
        strf_time2 = datetime.datetime.strptime(date_str2, "%Y-%m-%d")
        if strf_time1 > strf_time2:
            return 1
        if strf_time1 == strf_time2:
            return 0
        if strf_time1 < strf_time2:
            return -1

    def mkdir(self, path):
        # path = os.getcwd() + path
        is_exists = os.path.exists(path)
        if not is_exists:
            os.makedirs(path)
            print(self.get_current_time(), "创建文件夹", path)
            return True
        else:
            return False
