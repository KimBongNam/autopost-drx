from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from riotwatcher import LolWatcher, ApiError
from apscheduler.schedulers.blocking import BlockingScheduler
import os

member = ['모찌피치모찌피치', 'DRX 홍창현', '요붕스1', 'DRX Deft', 'DRX Keria']
api_key = os.environ.get('apikey')
dcid = str(os.environ.get('dcid'))
dcpw = str(os.environ.get('dcpw'))
watcher = LolWatcher(api_key)
my_region = 'kr'

rank = [0,0,0,0,0]
point = [0,0,0,0,0]

for i, name in enumerate(member):
    me = watcher.summoner.by_name(my_region, name)
    result = watcher.league.by_summoner(my_region, me['id'])
    rank[i] = result[0]['tier']
    point[i] = result[0]['leaguePoints']

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--disable-dev-shm-usage")
op.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)

driver.get('https://gall.dcinside.com/mgallery/board/lists?id=longzhugaming')
driver.find_element_by_class_name('user_info').click()
print(driver.page_source)
driver.find_element_by_id('id').send_keys(dcid)
driver.find_element_by_id('pw').send_keys(dcpw)
driver.find_element_by_xpath('//*[@id="container"]/div/article/section/div/div[1]/div/form/fieldset/button').click()
driver.implicitly_wait(20)
try:
    driver.find_element_by_xpath('//*[@id="contbox"]/div/div[3]/button[2]').click()
except:
    pass
driver.implicitly_wait(20)
driver.find_element_by_id('btn_write').click()
driver.implicitly_wait(20)
driver.find_element_by_id('subject').send_keys('선수들 솔랭 점수.bot')
driver.switch_to_frame(driver.find_element_by_xpath("//*[@id='tx_canvas_wysiwyg']"))

for i in range(5):
    driver.find_element_by_tag_name("body").send_keys(f'{member[i]} {rank[i]} {point[i]} \n')
driver.switch_to_default_content()
driver.find_element_by_xpath('//*[@id="write"]/div[5]/button[2]').click()

