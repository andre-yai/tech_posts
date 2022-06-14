from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime

chromeDriver = ChromeDriverManager().install()



class LinkedIn:
    def __init__(self):
        URL = "https://linkedin.com/"
        self.driver = webdriver.Chrome(chromeDriver)
        self.driver.get(URL)
        sleep(3)
    def fill_login_form(self,email_string, password_string):
        email = self.driver.find_element_by_xpath("//input[@name ='session_key']")
        password = self.driver.find_element_by_xpath("//input[@name ='session_password']")
        email.send_keys(email_string)
        password.send_keys(password_string)
        sleep(2)
        submit = self.driver.find_element_by_xpath("//button[@type = 'submit']").click()
        sleep(3)
    
    def post_linkdin(self,text):
        self.init_post()
        self.posting(text)
    
    def init_post(self):
        box_post = self.driver.find_element_by_xpath('//*[@id = "main"]/div[1]/div/div[1]/button').click()
        sleep(2)
        pass
    
    def posting(self,text):
        post_input = self.driver.find_element_by_class_name("ql-editor.ql-blank")
        post_input.send_keys(text)
        sleep(3)
        
    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    text = "Data is a precious thing and will last longer than system themselfs. -Tim Berners-Lee"
    user = LinkedIn()
    user.fill_login_form(email,password)
    user.post_linkdin(text)
    user.quit()

# driver.get("https://google.com")
# driver.implicitly_wait(0.5)
# search_box = driver.find_element(by=By.NAME, value="q")
# search_button = driver.find_element(by=By.NAME, value="btnK")
# search_box.send_keys("Selenium")
# search_button.click()
# driver.implicitly_wait(5)
# search_box = driver.find_element(by=By.NAME, value="q")
# value = search_box.get_attribute("value")
# assert value == "Selenium"
