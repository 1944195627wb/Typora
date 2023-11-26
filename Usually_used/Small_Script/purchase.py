import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

purchase_time = '2023-11-11 13:22:00.000000'
webdriver_handle = webdriver.Chrome()
webdriver_handle.get('https://shop.samsung.com.cn/')
time.sleep(3)
# webdriver_handle.find_element(By.LINK_TEXT,"你好，请登录").click()
print("请扫码登录")
time.sleep(20)
webdriver_handle.get("https://shop.samsung.com.cn/shoppingCart")
#勾选商品
time.sleep(5)
while True:
    # try:
    #     if webdriver_handle.find_element(By.CLASS_NAME,"btn"):
    #         webdriver_handle.find_element(By.CLASS_NAME,"btn").click()
    #         break
    # except:
    #     print("找不到购买按钮")

    time_now = datetime.datetime.now().strftime(('%Y-%m-%d %H:%M:%S.%f'))
    print(time_now)
    if time_now>purchase_time:
        while True:
            try:
                if webdriver_handle.find_element(By.LINK_TEXT,"去结算"):
                    print("here")
                    webdriver_handle.find_element(By.LINK_TEXT,"去结算").click()
                    print("主人，结算提交成功，我已帮你抢到商品啦，请及时支付订单")
                    break
            except:
                print("未成功")

        while True:
            try:
                if webdriver_handle.find_element(By.LINK_TEXT,"提交订单"):
                    webdriver_handle.find_element(By.LINK_TEXT,"提交订单").click()
                    print("抢购成功，请尽快付款")
            except:
                print("主人，结算提交成功，我已帮你抢到商品啦，请及时支付订单")
                break
        time.sleep(0.01)