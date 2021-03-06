from selenium import webdriver
import json
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WT
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import random
from pymongo import MongoClient

class CookieObtainer:
	def __init__(self):
		pass



	def get_cookies(self, uname, password):

		driver = webdriver.Remote(
				  command_executor='http://hub:4444/wd/hub',
				  desired_capabilities=DesiredCapabilities.FIREFOX)

		driver.get("https://www.instagram.com/accounts/login/")
		el = WT(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
		el.send_keys(uname)
		driver.find_element_by_name("password").send_keys(password)

		submit = driver.find_elements(
				By.XPATH,
				'/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div'
			)
		if len(submit) > 0:
			submit[0].click()
		else:
			submit = driver.find_elements(
					By.XPATH,
					'/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div'
				)
			if len(submit) > 0:
				submit[0].click()

		try:
			el = WT(driver, 5).until(EC.presence_of_element_located(
					(
						By.XPATH,
						'/html/body/div[1]/section/main/div/div/div/div/button'
					)
				))
			el.click()
		except TimeoutException as e:
			print(f"No remember login popup found or error {e}")

		try:
			el = WT(driver, 5).until(EC.presence_of_element_located(
					(
						By.XPATH,
						'/html/body/div[4]/div/div/div/div[3]/button[2]'
					)
				))
			el.click()
		except TimeoutException as e:
			print(f"No notification popup found or error {e}")

		dct = map(lambda x: (x['name'], x['value']), driver.get_cookies())
		cookies = dict(list(dct))
		driver.quit()

		return cookies
