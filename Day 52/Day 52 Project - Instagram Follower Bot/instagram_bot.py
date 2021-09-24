from selenium import webdriver
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException

URL = "https://www.instagram.com/"
CHROME_DRIVER_PATH = "A:/Software/Chrome Driver/chromedriver.exe"
INSTA_EMAIL = ""  #your email
INSTA_PASSWORD = ""  #your password
ACCOUNT_TO_FOLLOW = ""  #account whose followers you want to follow


class InstaFollowerBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.get(URL)

    def login(self):
        sleep(3)
        email_input = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[1]/div/label/input'
        )
        email_input.click()

        sleep(2)
        email_input.send_keys(INSTA_EMAIL)

        sleep(2)
        pwd_input = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label/input'
        )
        pwd_input.click()

        sleep(2)
        pwd_input.send_keys(INSTA_PASSWORD)

        sleep(2)
        login_button = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[3]/button'
        )
        login_button.click()

        sleep(7)

    def find_followers(self):
        self.driver.get(f"{URL}{ACCOUNT_TO_FOLLOW}")
        sleep(3)
        follower_count = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'
        )
        follower_count.click()

        sleep(2)
        popup = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0],scrollTop = arguments[0].scrollHeight", popup)
            sleep(2)

    def follow(self):
        buttons = self.driver.find_elements_by_class_name("sqdOP")
        for button in buttons:
            try:
                follow_button = button
                sleep(2)
                follow_button.click()

            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath(
                    '/html/body/div[7]/div/div/div/div[3]/button[2]'
                )
                sleep(2)
                cancel_button.click()
                sleep(2)
                follow_button = button
                follow_button.click()

            else:
                sleep(2)
