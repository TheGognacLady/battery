from selenium import webdriver
import json
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WT
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import random
from pymongo import MongoClient

class CookieObtainer:
	def __init__(self, uname, password):
		self.uname = uname
		self.password = password


	def refresh_cookies(self, path):


		driver = webdriver.Remote(
				  command_executor='http://hub:4444/wd/hub',
				  desired_capabilities=DesiredCapabilities.FIREFOX)


		driver.get(path)
		el = WT(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
		el.send_keys(self.uname)
		driver.find_element_by_name("password").send_keys(self.password)
		driver.find_element(
				By.XPATH,
				'/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]'
			).click()

		try:
			el = WT(driver, 5).until(EC.presence_of_element_located(
					(
						By.XPATH,
						'/html/body/div[1]/section/main/div/div/div/section/div/button'
					)
				))
			el.click()
		except Exception as e:
			print(f"No popup found or error {e}")


		dct = map(lambda x: (x['name'], x['value']), driver.get_cookies())
		cookies = dict(list(dct))
		driver.quit()
		return cookies
