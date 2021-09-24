<<<<<<< HEAD
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import time

URL = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102713980&keywords=python%20developer&location=India"
chrome_driver_path = "A:/Software/Chrome Driver/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--kiosk")
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)


driver.get(URL)
sign_in = driver.find_element_by_class_name("nav__button-secondary")
sign_in.click()

username = driver.find_element_by_id("username")
time.sleep(3)
username.send_keys("your email")

pwd = driver.find_element_by_id("password")
time.sleep(3)
pwd.send_keys("your password")

button = driver.find_element_by_class_name("btn__primary--large")
time.sleep(3)
button.click()

jobs = driver.find_elements_by_class_name("jobs-search-results__list-item")
for job in jobs:
    job.click()
    time.sleep(3)

    save_button = driver.find_element_by_css_selector(".display-flex .jobs-save-button span")
    time.sleep(3)
    save_button.click()

    details = driver.find_element_by_class_name("jobs-search__right-rail")
    details.click()
    html = driver.find_element_by_tag_name("html")
    html.send_keys(Keys.END)
    time.sleep(3)

    try:
        follow_button = driver.find_element_by_class_name("follow")
        follow_button.click()
        time.sleep(3)
    except NoSuchElementException:
        continue
=======
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import time

URL = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102713980&keywords=python%20developer&location=India"
chrome_driver_path = "A:/Software/Chrome Driver/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--kiosk")
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)


driver.get(URL)
sign_in = driver.find_element_by_class_name("nav__button-secondary")
sign_in.click()

username = driver.find_element_by_id("username")
time.sleep(3)
username.send_keys("your email")

pwd = driver.find_element_by_id("password")
time.sleep(3)
pwd.send_keys("your password")

button = driver.find_element_by_class_name("btn__primary--large")
time.sleep(3)
button.click()

jobs = driver.find_elements_by_class_name("jobs-search-results__list-item")
for job in jobs:
    job.click()
    time.sleep(3)

    save_button = driver.find_element_by_css_selector(".display-flex .jobs-save-button span")
    time.sleep(3)
    save_button.click()

    details = driver.find_element_by_class_name("jobs-search__right-rail")
    details.click()
    html = driver.find_element_by_tag_name("html")
    html.send_keys(Keys.END)
    time.sleep(3)

    try:
        follow_button = driver.find_element_by_class_name("follow")
        follow_button.click()
        time.sleep(3)
    except NoSuchElementException:
        continue
>>>>>>> 78227dc25bd1d7f142aebd2a78d7972068b30981
