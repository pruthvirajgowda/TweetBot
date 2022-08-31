from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

SERVICE = Service(executable_path=ChromeDriverManager().install())
TWITTER_ID = "Twitter_ID"
TWITTER_PASSWORD = "PASSWORD"


class InternetSpeed:
    def __init__(self):
        self.driver = webdriver.Chrome(service=SERVICE)
        self.driver.get("https://www.speedtest.net/")
        sleep(5)

    def check_speed(self):
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
        sleep(60)
        download_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/'
                                                            'div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]'
                                                            '/div[1]/div/div[2]/span').text
        upload_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]'
                                                          '/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]'
                                                          '/div/div[2]/span').text
        speed = [download_speed, upload_speed]
        return speed


class TweetBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=SERVICE)
        self.driver.get('https://twitter.com/i/flow/login')
        sleep(5)

    def login(self):
        user_id = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]'
                                                     '/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        user_id.send_keys(TWITTER_ID, Keys.ENTER)
        sleep(2)
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/'
                                                      'div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/'
                                                      'div[1]/input')
        password.send_keys(TWITTER_PASSWORD, Keys.ENTER)
        sleep(2)

    def tweet(self, speed):
        tweet_input = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/'
                                                         'div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/'
                                                         'div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/'
                                                         'div/div/div/div/div[2]/div')
        if float(speed[0]) < 20.0 and float(speed[1]) < 2.0:
            tweet_input.send_keys(f"Just a Python bot testing Code,\n It's totally normal.\nSpeed of my internet is just"
                                  f" bad It's {speed[0]} Up and {speed[1]} Download")
        else:
            tweet_input.send_keys(
                f"Just a Python bot testing Code,\n It's totally normal.\nSpeed of my internet is pretty"
                f" good It's {speed[0]} Up and {speed[1]} Download")
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/'
                                           'div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/'
                                           'div[3]').click()
        tweet_input.quit()


i_speed = InternetSpeed()
speed = i_speed.check_speed()
tb = TweetBot()
tb.login()
tb.tweet(speed)
