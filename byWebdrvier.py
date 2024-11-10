from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


url = 'https://www.south-plus.net/plugin.php?H_name-tasks.html.html'
web = webdriver.Chrome()
web.get(url)
print(web.title)