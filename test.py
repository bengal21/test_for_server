import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


option = Options()
option.add_argument("--headless")
s = Service('/usr/bin/geckodriver')
driver = webdriver.Firefox(service=s, options=option)


driver.get('https://mail.ru/')
time.sleep(1)
driver.get_full_page_screenshot_as_file('t2.png')

driver.quit()
