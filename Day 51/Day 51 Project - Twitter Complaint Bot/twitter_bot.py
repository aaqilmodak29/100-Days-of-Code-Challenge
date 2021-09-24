from selenium import webdriver
from time import sleep
# from selenium.common.exceptions import NoSuchElementException

SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/home"
PROMISED_DOWN = 150.0
PROMISED_UP = 75.0
CHROME_DRIVER_PATH = "A:/Software/Chrome Driver/chromedriver.exe"
TWITTER_EMAIL = ""  # your email
TWITTER_PASSWORD = ""  # your password


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.get(SPEED_TEST_URL)
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP
        self.download_speed = ""
        self.upload_speed = ""

    def get_internet_speed(self):
        sleep(5)
        check_speed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                        'div[1]/a/span[4]')
        check_speed.click()
        sleep(50)
        self.download_speed = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/'
            'div[1]/div[2]/div/div[2]/span'
        ).text
        print(self.download_speed)

        self.upload_speed = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/'
            'div[1]/div[3]/div/div[2]/span'
        ).text
        print(self.upload_speed)
        # try:
        #     popup = self.driver.find_element_by_xpath(
        #         '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a/svg'
        #     )
        # except NoSuchElementException:
        #     pass
        # else:
        #     popup.click()

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)

        sleep(10)
        email_input = self.driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/'
            'label/div/div[2]/div/input'
        )
        email_input.send_keys(TWITTER_EMAIL)
        next_button = self.driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/'
            'div/div/div[2]/div[2]/div[2]/div/div'
        )
        sleep(3)
        next_button.click()

        sleep(5)
        pwd_input = self.driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/'
            'label/div/div[2]/div/input'
        )
        pwd_input.send_keys(TWITTER_PASSWORD)
        sleep(3)
        login_button = self.driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div'
        )
        login_button.click()

        sleep(7)
        tweet = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/'
            'div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
        )
        tweet.click()

        sleep(5)
        self.download_speed = float(self.download_speed)
        self.upload_speed = float(self.upload_speed)
        tweet.send_keys(
            f"Hey Internet Provider, why is my internet speed {self.download_speed} down/{self.upload_speed} up"
            f" when I payed for {PROMISED_DOWN} down/{PROMISED_UP} up?"
        )

        sleep(5)
        send_tweet = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/'
            'div[3]/div/div/div[2]/div[3]/div/span'
        )
        send_tweet.click()
