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
    

    #a method to open instagram and login to the site.
    def login(self):
        bot = self.bot
        bot.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        time.sleep(1)

        #get username and password feild.
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')

        email.clear()
        password.clear()

        #sends the credentials provided to the input fields in the form
        email.send_keys(self.email)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(2)
    
    #a method to search the posts by hastags and return the page.
    def hashtag_search(self,hashtag):
        bot = self.bot
        url = "https://www.instagram.com/explore/tags/"+hashtag
        bot.get(url)


    #method to like the post by hashtag
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
                try:
                    ActionChains(bot).move_to_element(heart).click(heart).perform()
                    time.sleep(5)
                except:
                    time.sleep(60)
    
    #method to follow the users by hashtags.
    def follow_with_hashtag(self,hashtag):
        bot = self.bot
        self.hashtag_search(hashtag)
        time.sleep(2)

        for i in range(1,10):
            posts = bot.find_elements_by_css_selector('a')
            links = [elem.get_attribute('href')
                        for elem in posts]
            
            for link in links:
                bot.get(link)
                follow_btn = bot.find_element_by_css_selector('button')
                
                if(follow_btn.text != 'Following'):

                    try:
                        follow_btn.click()
                        time.sleep(2)
                    except:
                        time.sleep(60)
                else:
                    print("You are already following the user.")


    #follow with username, supports continious operations
    def follow_with_username(self,user_to_follow):
        bot = self.bot
        url = "https://www.instagram.com/" + user_to_follow
        bot.get(url)
        time.sleep(2)
        follow_btn = bot.find_element_by_css_selector('button')
        if ( follow_btn != 'Following'):
            try:
                follow_btn.click()
                time.sleep(5)
            except:
                time.sleep(60)
        else:
            print("You are already following this user")
    
    #unfollow with username, supports continious operations
    def unfollow_with_username(self,user_to_unfollow):
        bot = self.bot
        url = "https://www.instagram.com/" + user_to_unfollow + "/"
        bot.get(url)
        time.sleep(2)
        follow_btn = bot.find_element_by_css_selector('button')

        if ( follow_btn.text == "Following"):
            try:
                follow_btn.click()
                time.sleep(5)
                confirm_op = bot.find_element_by_xpath('//button[text() = "Unfollow"]')
                confirm_op.click()
            except:
                time.sleep(60)
        else:
            print("You are not following this user.")

    
    #close browser
    def close_bot(self):
        bot = self.bot
        bot.close()
    
    #close browser upon exit
    def __exit__(self,exc_type,exc_value,traceback):
        bot = self.bot
        bot.close()

        



bot = InstaBot("#","#")
bot.login()

bot.unfollow_with_username('mkesh_gh')
