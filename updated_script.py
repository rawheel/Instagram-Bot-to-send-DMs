from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time
import os
class instabot:
	def __init__(self,username,password,dm_accounts,message):
		self.username = username
		self.password = password
		self.dm_accounts = dm_accounts
		self.message = message
		self.bot = webdriver.Chrome("chromedriver.exe")
		self.login()

	def login(self):
		bot = self.bot

		bot.get("https://www.instagram.com/")
		time.sleep(6)


		user = bot.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
		user.send_keys(self.username)
		pw = bot.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
		pw.send_keys(self.password)
		login_btn = bot.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
		login_btn.click()
		time.sleep(6)

		self.send_messages()
	def send_messages(self):
		bot = self.bot
		bot.get("https://www.instagram.com/direct/new/")

		time.sleep(3)

		try: 
			not_now = bot.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
			not_now.click()
			
		except:
			pass

		time.sleep(5)

		for account in self.dm_accounts:

			search_bar = bot.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/div/div[2]/input")
			search_bar.send_keys(account)
			time.sleep(5)
			check = bot.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div")
			c = check.text
			if "No account found" not in c: 
				sel_account = bot.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div")
				sel_account.click()
				time.sleep(3)
			else:
				for i in range(len(account)):
					search_bar.send_keys(Keys.BACKSPACE)



		time.sleep(2)    

		next_btn = bot.find_element_by_xpath("html/body/div[2]/div/div/div[1]/div/div[2]/div/button")
		next_btn.click()
		time.sleep(5)

		message_text = bot.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
		message_text.send_keys(self.message)

		send_btn = bot.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")
		send_btn.click()







#username = os.environ.get('INSTA_USERNAME')
#password = os.environ.get('INSTA_PASSWORD')



account_1 = instabot(username,password,["selenagomez","llllkjjjo","justinbieber"],"https://www.instagram.com/justinbieber/")



























