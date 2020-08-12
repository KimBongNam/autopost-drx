from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from riotwatcher import LolWatcher, ApiError
from apscheduler.schedulers.blocking import BlockingScheduler
import os
import random
import time

member = ['모찌피치모찌피치', 'DRX 홍창현', '요붕스1', 'DRX Deft', 'DRX Keria']
api_key = os.environ.get('apikey')
dcid = str(os.environ.get('dcid'))
dcpw = str(os.environ.get('dcpw'))
watcher = LolWatcher(api_key)
my_region = 'kr'

rank = [0,0,0,0,0]
point = [0,0,0,0,0]
success = [1000,1000,1250,1150,1150]
for i, name in enumerate(member):
    me = watcher.summoner.by_name(my_region, name)
    result = watcher.league.by_summoner(my_region, me['id'])
    rank[i] = result[0]['tier']
    point[i] = result[0]['leaguePoints']

options = webdriver.ChromeOptions()
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36")
options.add_argument("lang=ko-KR")
options.add_argument("Accept-Encoding=gzip, deflate, br")
options.add_argument("Cache-Control=max-age=0")
options.add_argument("Connection=keep-alive")
options.add_argument("Host=gall.dcinside.com")
options.add_argument("Sec-Fetch-Dest=documant")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=op)
driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});")
driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")
driver.execute_script("const getParameter = WebGLRenderingContext.getParameter;WebGLRenderingContext.prototype.getParameter = function(parameter) {if (parameter === 37445) {return 'NVIDIA Corporation'} if (parameter === 37446) {return 'NVIDIA GeForce GTX 980 Ti OpenGL Engine';}return getParameter(parameter);};")

driver.get('https://dcid.dcinside.com/join/login.php?s_url=https%3A%2F%2Fgall.dcinside.com%2Fmgallery%2Fboard%2Flists%3Fid%3Dlongzhugaming&s_key=185')
time.sleep(random.randint(1,5))
driver.find_element_by_id('id').send_keys(dcid)
driver.find_element_by_id('pw').send_keys(dcpw)
driver.find_element_by_xpath('//*[@id="container"]/div/article/section/div/div[1]/div/form/fieldset/button').click()
time.sleep(random.randint(1,5))
try:
    driver.find_element_by_xpath('//*[@id="contbox"]/div/div[3]/button[2]').click()
except:
    pass
time.sleep(random.randint(1,5))
driver.find_element_by_id('btn_write').click()
driver.find_element_by_id('subject').send_keys('선수들 솔랭 점수.bot')
driver.switch_to_frame(driver.find_element_by_xpath("//*[@id='tx_canvas_wysiwyg']"))

for i in range(5):
    driver.find_element_by_tag_name("body").send_keys(f'{member[i]} {rank[i]} {point[i]}/{success[i]} \n')

driver.switch_to_default_content()
driver.implicitly_wait(random.randint(1,5))
driver.find_element_by_xpath('//*[@id="write"]/div[5]/button[2]').click()


