from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # 如果你在无头模式下运行
chrome_options.add_argument("--no-sandbox")  # 解决一些权限问题
chrome_options.add_argument("--disable-dev-shm-usage")  # 解决共享内存问题

service = Service('/usr/local/bin/chromedriver')  # 确保路径正确
web = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://www.south-plus.net/plugin.php?H_name-tasks.html.html'
web.get(url)
print(web.title)