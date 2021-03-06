# author: zephyr ji
# time: 2020/10/01
# Update By donald Tang :2022_1_2
# pip install selenium
# download chromedriver：http://chromedriver.storage.googleapis.com/index.html
# https://www.cnblogs.com/lfri/p/10542797.html

import time
from selenium import webdriver
import requests
import re

def login(username, password):
    url = 'https://drcom.szu.edu.cn/a70.htm'  # url中指明定位到校园网登陆界面
    # chrome_driver = r'F:\software\Anaconda\envs\carla\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe'
    chrome_driver = r'D:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'  #更换成你的安装地址

    #隐藏浏览器
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")
    
    # driver = webdriver.Chrome(executable_path=chrome_driver,chrome_options=option)
    driver = webdriver.Chrome(executable_path=chrome_driver)
    driver.get(url)
    print(driver.title)
    name_input = driver.find_element_by_css_selector('[placeholder ="请输入账号"]')  # 找到用户名的框框
    pass_input = driver.find_element_by_css_selector('[placeholder ="请输入密码"]')  # 找到输入密码的框框
    login_button = driver.find_element_by_css_selector('[value = " 登 录（Login）"]')  # 找到登录按钮
    # reset_button = driver.find_element_by_id('VipResetButton')  # 找到reset按钮

    name_input.clear()
    name_input.send_keys(username)  # 填写用户名
    time.sleep(0.2)
    pass_input.clear()
    pass_input.send_keys(password)  # 填写密码
    time.sleep(0.2)
    login_button.click()  # 点击登录

    time.sleep(10)
    print(driver.title)
    driver.close()

def canConnect():
    try:
        q = requests.get("http://www.baidu.com", timeout=5)
        m = re.search(r'STATUS OK', q.text)
        if m:
            return True
        else:
            return False
    except:
        print('error')
        return False


if __name__ == "__main__":
    user = "322159"  # 输入账号
    pw = "**********"  # 输入密码

    while True:
        can_connect = canConnect()
        getCurrentTime = time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))
        if not can_connect:
            print(getCurrentTime, u"断网了...")
            login(user, pw)
            print(getCurrentTime, u"诶，我又好了...")
            time.sleep(10)
        else:
            print(getCurrentTime, u"一切正常...")
            time.sleep(600)
