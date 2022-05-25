import sys
import re
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
from bs4 import BeautifulSoup as bs
from time import sleep
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
link= 'http://www.google.com'
driver.get(link)
# driver.implicitly_wait(10)
# sleep(10)
html_source = driver.page_source
soup_source=bs(html_source,'html.parser')