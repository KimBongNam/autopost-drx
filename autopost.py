from selenium import webdriver
from riotwatcher import LolWatcher, ApiError
from apscheduler.schedulers.blocking import BlockingScheduler
import os

member = ['모찌피치모찌피치', 'DRX 홍창현', '요붕스1', 'DRX Deft', 'DRX Keria']
api_key = os.environ.get('apikey')
dcid = os.environ.get('dcid')
dcpw = os.environ.get('dcpw')
watcher = LolWatcher(api_key)
my_region = 'kr'

rank = [0,0,0,0,0]
point = [0,0,0,0,0]

for i, name in enumerate(member):
    me = watcher.summoner.by_name(my_region, name)
    result = watcher.league.by_summoner(my_region, me['id'])
    rank[i] = result[0]['tier']
    point[i] = result[0]['leaguePoints']

GOOGLE_CHROME_PATH = os.environ.get('GOOGLE_CHROME_BIN')
CHROMEDRIVER_PATH = os.environ.get("CHROMEDRIVER_PATH")
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = GOOGLE_CHROME_PATH
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
driver = webdriver.Chrome(driver)
driver.get('https://gall.dcinside.com/mgallery/board/lists?id=longzhugaming')
driver.find_element_by_class_name('user_info').click()
driver.find_element_by_id('id').send_keys(dcid)
driver.find_element_by_id('pw').send_keys(dcpw)
driver.find_element_by_xpath('//*[@id="container"]/div/article/section/div/div[1]/div/form/fieldset/button').click()

try:
    driver.find_element_by_xpath('//*[@id="contbox"]/div/div[3]/button[2]').click()
except:
    pass

driver.find_element_by_id('btn_write').click()
driver.find_element_by_id('subject').send_keys('선수들 솔랭 점수.bot')
driver.switch_to_frame(driver.find_element_by_xpath("//*[@id='tx_canvas_wysiwyg']"))

for i in range(5):
    driver.find_element_by_tag_name("body").send_keys(f'{member[i]} {rank[i]} {point[i]} \n')
driver.switch_to_default_content()
driver.find_element_by_xpath('//*[@id="write"]/div[5]/button[2]').click()

