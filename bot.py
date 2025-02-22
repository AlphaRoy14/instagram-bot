from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
import os
import time

class InstaBot:
    def __init__(self,username, password):

        '''
            Initalting and instance of instagram bot class
            calls the login method to authenticate a user
         args: 
            #* username:str : the username for instagram
            #* password :str :the password for instagram
        attrib:
            #* Driver : selenium.webdriver.Chrome : The driver that is used to automate
            
        
        '''
        self.baseURL="https://www.instagram.com/"
        self.username = username  
        self.password = password
        self.chrome_options=Options()
        self.chrome_options.add_argument("--disable-infobars")
        self.driver = webdriver.Chrome(executable_path="./chromedriver",\
            options=self.chrome_options)
        self.login()
        self.search_tags="https://www.instagram.com/explore/tags/{}/"
        
        

    def login(self):
        
        self.driver.get(f"{self.baseURL}accounts/login/")
        self.driver.find_element_by_name("username").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys(self.password)
        self.driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click() 
        #?why is Log in working with single quote and not double quote? WTF? 
        #* Its to avoid confusion when closing the quotes LOL.
        self.driver.get(f'{self.baseURL}alpharoy14')
   
    def nav_user(self,user):
        """
        navigates to the users page
        """
        self.driver.get(f'{self.baseURL}{user}')
    
    def follow_user(self,user):
        self.nav_user(user)
        '''
        follows a user by clicking the follow button
        args:
            user:str: user id of the user
        '''
        buttons=self.find_button("Follow")
        for btn in buttons:
            print(f"{btn}\n")
            btn.click()
    def unfollow_user(self,user):
        '''
        unfollows a user
        arg:
            user:str: the user name of the user
        '''
        self.nav_user(user)
        buttons=self.find_button("Following")
        for btn in buttons:
            btn.click()
        unfollow_button=self.find_button("Unfollow")
        unfollow_button[0].click()

    def search_tag(self,tag):
        '''
        search instagram with a specific tag 

        arg:
            tag:str: the tag that you want to search 
        '''
        self.driver.get(self.search_tags.format(tag))


    def find_button(self,button_name):
        ''' 
        find the button by searching by the name
        arg:
            #* button_name:str: name of the button
        
        '''
        button=self.driver.find_elements_by_xpath("//*[(text()='{}')]".format(button_name))

        return button



    def download_all_images(self,user):
        #TODO neeed to do thissss!!!!!!
        self.nav_user(user)
        img_srcs=[]
        finished=False
        while not finished:
            finished=self.infinite_scroll(user)
            
            for img in self.driver.find_elements_by_class_name('_9AhH0'):
                print(img.__dict__)
        





    def infinite_scroll(self,user):

        '''
            scrolls all the to the bottom of the sea
            arg:
                user:str: enter the instagram user id
        '''
        pause_time=1
        self.last_height=self.driver.execute_script("return document.body.scrollHeight")
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(pause_time)
        self.new_hight=self.driver.execute_script("document.body.scrollHeight")

        if self.new_hight==self.last_height:
            return True
        
        self.last_height=self.new_hight
        return False
        
        

if __name__ == "__main__":
    ig_bot=InstaBot("temp","Temp")
    #time.sleep(3)̀̀
    ig_bot.nav_user("alpharoy14")
    # time.sleep(5)    # ig_bot.follow_user("selenagomez")
    # time.sleep(2)
    #ig_bot.unfollow_user("selenagomez")
    # ig_bot.search_tag("piano")
    ig_bot.download_all_images("alpharoy14")
    print (ig_bot.username)






