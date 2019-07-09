from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime as dt

class InstaBot():
    def __init__(self,email,password):
        self.email = email
        self.password = password
        self.bot = webdriver.Firefox()
    
    def login(self):
        bot = self.bot
        bot.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        time.sleep(1)

        #get username and password feild.
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')

        email.clear()
        password.clear()

        email.send_keys(self.email)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(2)
    
    def hashtag_search(self,hashtag):
        bot = self.bot
        url = "https://www.instagram.com/explore/tags/"+hashtag
        bot.get(url)

    def like_post(self,hashtag):
        bot = self.bot
        self.hashtag_search(hashtag)
        time.sleep(2)

        for i in range(1,10):
            posts = bot.find_elements_by_css_selector('a')
            links = [elem.get_attribute('href')
                        for elem in posts]
            
            
            for link in links:
                bot.get(link)
                heart = bot.find_element_by_xpath("//span[@class='fr66n']")
                ActionChains(bot).move_to_element(heart).click(heart).perform()
                time.sleep(5)
    




bot = InstaBot("username","password")
bot.login()
bot.like_post('love')
