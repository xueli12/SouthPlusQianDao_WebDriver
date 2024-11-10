from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json
import requests
import time
import os

# 获取系统变量serverKey
serverKey = os.environ.get('serverKey')


# 获取 COOKIE 环境变量
cookie_json = os.environ.get('COOKIE')


if cookie_json:
    try:
        # 解析 JSON 字符串
        cookie_data = json.loads(cookie_json)
        print(cookie_data)  # 打印解析后的列表
    except json.JSONDecodeError:
        print("错误：无法解析 COOKIE 环境变量为 JSON。")
else:
    print("错误：COOKIE 环境变量未设置。")

chrome_options = Options()
chrome_options.add_argument("--headless")  # 如果你在无头模式下运行
chrome_options.add_argument("--no-sandbox")  # 解决一些权限问题
chrome_options.add_argument("--disable-dev-shm-usage")  # 解决共享内存问题

service = Service(rf'/usr/local/bin/chromedriver')  # 确保路径正确
web = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://www.south-plus.net/plugin.php?H_name-tasks.html.html'
web.get(url)
print(web.title)
time.sleep(1)
# # 保存cookies为json格式
# cookies = web.get_cookies()
# print(cookies)
# with open('cookies.json', 'w') as f:
#     json.dump(cookies, f)


# 将cookies添加到webdriver中   
for cookie in cookie_data:
    web.add_cookie(cookie)

# 重新加载页面
web.get(url)

# 领取周常
try:
    web.find_element(By.XPATH, '//*[@id="p_14"]/a/img').click()
    print('周常任务已领取')
except:
    print('周常暂未刷新')

try:
    web.find_element(By.XPATH, '//*[@id="p_15"]/a/img').click()
    print('日常任务已领取')
    # 切换到进行中的人物
    web.find_element(By.XPATH, '//*[@id="main"]/table/tbody/tr/td[1]/div[2]/table/tbody/tr[3]/td').click()
    # 点击进行中的任务
    # 完成日常
    web.find_element(By.XPATH, '//*[@id="both_15"]/a/img').click()
    time.sleep(3)
    try:
        web.find_element(By.XPATH, '//*[@id="both_15"]/a/img').click()
    except:
        print('日常领取成功')
        # 用urlencode编码中文内容
        messagecontent = '日常领取成功'
        messagecontent = requests.utils.quote(messagecontent)
        # 通过server酱发送通知
        url = f"https://sctapi.ftqq.com/{serverKey}.send?title={messagecontent}&desp=messagecontent"

        payload={}
        headers = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        
    try:
        # 尝试点击周常,没有就跳了
        web.find_element(By.XPATH, '//*[@id="both_14"]/a/img').click()
    except:
        pass


except:
    # 用urlencode编码中文内容
    messagecontent = '日常领取失败'
    messagecontent = requests.utils.quote(messagecontent)
    # 通过server酱发送通知
    url = f"https://sctapi.ftqq.com/{serverKey}.send?title={messagecontent}&desp=messagecontent"
    print(url)

    payload={}
    headers = {
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response)
    print('日常暂未刷新或领取失败')


web.quit()
# 
