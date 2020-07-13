from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from time import sleep

import os
from dotenv import load_dotenv
load_dotenv()
HANDLE = os.getenv('CF_HANDLE')
PASSWORD = os.getenv('CF_PASSWORD')

CFLIST_BASE_URL='https://codeforces.com/list/'
CF_LOGIN='https://codeforces.com/enter'

class ScrapeList():
	def __init__(self):
		opts=Options()
		opts.add_argument("--headless")
		self.browser = Firefox(firefox_options=opts)
		self.browser.get(CF_LOGIN)
		sleep(1)
		self.browser.find_element_by_id('handleOrEmail').send_keys(HANDLE)
		self.browser.find_element_by_id('password').send_keys(PASSWORD)
		self.browser.find_element_by_class_name('submit').click()
		print("Logged in and Ready:")

	def list_scrape(self,key: str):
		URL = CFLIST_BASE_URL + key
		self.browser.get(URL)
		if self.browser.current_url != URL :
			return ''
		names = self.browser.find_elements_by_css_selector('.rated-user')
		ans = ';'.join(name.get_attribute('text') for name in names)
		return ans

	def __del__(self):
		self.browser.close()
		print("Browser closed:")