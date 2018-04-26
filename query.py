#coding:utf-8

from selenium import webdriver
import time
import random
from urllib import request
import chardet
import ssl

def fun():
    while 1:
        with open("query.txt",'r') as f:
            file=f.readlines()
            random.shuffle(file)
            for str1 in file :
                while 1:
                    with open("climb_ip.txt",'r') as f1:
                        f2 = f1.readlines()
                        http_ip = str(random.choice(f2))
                        ip = http_ip.split(":")[0] + ":" + http_ip.split(":")[1]
                        ht = http_ip.split(":")[2].lower().strip("\n") + "://"
                        print ('当前使用ip：' + ht + ip)
                        print("查询词：" + str1)

                    i = random.randint(5, 20)
                    time.sleep(i)
                    # 加启动配置
                    option = webdriver.ChromeOptions()
                    option.add_argument('disable-infobars')
                    option.add_argument('--proxy-server=' + ht + ip)
                    driver = webdriver.Chrome(chrome_options=option)
                    driver.set_page_load_timeout(15)
                    driver.set_script_timeout(15)   #网页15s五响应，则抛出异常，重新选取IP访问
                    try:
                        driver.get("https://www.baidu.com/")
                        time.sleep(10)  # 等待页面加载完成
                        sr = driver.find_element_by_id("kw")
                        sr.send_keys(str1)
                        driver.find_element_by_id("su").click()
                        time.sleep(10) #在结果页面停留10s
                        driver.quit()
                        break
                    except Exception as e:
                        print (e)
                        driver.quit()
                        continue
def run():
    fun()



if __name__ == "__main__":
     fun()
