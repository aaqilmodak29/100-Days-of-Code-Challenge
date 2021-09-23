from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

URL = "https://tinder.com/"
EMAIL = "aaqilmodak@gmail.com"
PASSWORD = "1ntel2002"

chrome_driver_path = "A:/Software/Chrome Driver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)

try:
    log_in = driver.find_element_by_xpath(
        '//*[@id="s-2061886532"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
except NoSuchElementException:
    time.sleep(3)
    log_in = driver.find_element_by_xpath(
        '//*[@id="s-2061886532"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
    log_in.click()
else:
    log_in.click()

try:
    time.sleep(3)
    login_with_fb = driver.find_element_by_xpath('//*[@id="s192874960"]/div/div/div[1]/div/div[3]/span/'
                                                 'div[2]/button/span[2]')
except NoSuchElementException:
    time.sleep(3)
    more_options = driver.find_element_by_xpath('//*[@id="s192874960"]/div/div/div[1]/div/div[3]/span/button')
    more_options.click()
    time.sleep(3)
    login_with_fb = driver.find_element_by_xpath('//*[@id="s192874960"]/div/div/div[1]/div/div[3]/span/'
                                                 'div[2]/button/span[2]')
    login_with_fb.click()
else:
    login_with_fb.click()

time.sleep(3)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email_input = driver.find_element_by_xpath('//*[@id="email"]')
email_input.send_keys(EMAIL)
time.sleep(3)

pwd_input = driver.find_element_by_xpath('//*[@id="pass"]')
pwd_input.send_keys(PASSWORD)
time.sleep(3)

submit_button = driver.find_element_by_css_selector("#buttons .uiButton input")
submit_button.click()

driver.switch_to.window(base_window)
print(driver.title)

time.sleep(5)
try:
    location_popup = driver.find_element_by_xpath('//*[@id="s192874960"]/div/div/div/div/div[3]/button[1]/span')
except NoSuchElementException:
    time.sleep(3)
    location_popup = driver.find_element_by_xpath('//*[@id="s192874960"]/div/div/div/div/div[3]/button[1]/span')
    location_popup.click()
else:
    location_popup.click()

time.sleep(3)
notification_popup = driver.find_element_by_xpath('//*[@id="s192874960"]/div/div/div/div/div[3]/button[2]/span')
notification_popup.click()

buttons = driver.find_elements_by_tag_name('button')
# time.sleep(3)
# premium_popup = driver.find_element_by_xpath('//*[@id="s192874960"]/div/div/div[1]/div[2]/button[2]/span')
# premium_popup.click()

for n in range(100):
    try:
        time.sleep(3)
        like = driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
        like.click()
    except NoSuchElementException:
        time.sleep(3)
        like = driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        like.click()
    except ElementClickInterceptedException:
        time.sleep(3)
        popup = driver.find_element_by_xpath('//*[@id="s192874960"]/div/div/div[2]/button[2]/span')
        popup.click()
