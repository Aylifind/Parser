from selenium import webdriver   # потому что мы будем использовать брацзер Firefox
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary




class InstagramBot:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.driver = webdriver.Firefox()

	# На случай, если с Firefox что-то не так
	def classBrowser(self):
		self.driver.close()

	# Логинимся на сайте инстаграма, находим окошки с вводом логина и пароля через xPath
	def login(self):
		"""Автоматическое перенаправление и заполнение логинопароля на стартовой странице"""

		driver = self.driver
		driver.get("https://www.instagram.com")
		time.sleep(2)

		login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
		login_button.click()
		time.sleep(2)

		user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
		user_name_elem.clear()
		user_name_elem.send_keys(self.username)

		password_elem = driver.find_element_by_xpath("//input[@name='password']")
		password_elem.clear()
		password_elem.send_keys(self.password)
		password_elem.send_keys(Keys.RETURN)
		time.sleep(2)


username = "andrey1295"
password = "n8UI76xW"


andreyIG = InstagramBot(username, password)
andreyIG.login()
