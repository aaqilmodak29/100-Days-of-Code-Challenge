from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
import requests

CHROME_DRIVER_PATH = ""  # your chrome driver path
GOOGLE_FORM_URL = ""  # your google form path
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C" \
             "%22mapBounds%22%3A%7B%22west%22%3A-122.64481581640625%2C%22east%22%3A-122.22184218359375%2C%22south%22" \
             "%3A37.633501230568804%2C%22north%22%3A37.916810261970156%7D%2C%22isMapVisible%22%3Atrue%2C" \
             "%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22" \
             "%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C" \
             "%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value" \
             "%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc" \
             "%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22" \
             "%3Atrue%2C%22mapZoom%22%3A11%7D "
HEADERS = {
    "User-Agent": "",  # your user-agent
    "Accept-Language": ""  # your accept-language
}

response = requests.get(url=ZILLOW_URL, headers=HEADERS)
rental_listings = response.text
soup = BeautifulSoup(rental_listings, "html.parser")
all_links = soup.select(".list-card-top a")
links = []
for link in all_links:
    href = link["href"]
    if "https" not in href:
        links.append(f"https://www.zillow.com{href}")
    else:
        links.append(href)
print(len(links))

all_addresses = soup.select(".list-card-info address")
addresses = [address.getText() for address in all_addresses]
print(len(addresses))

all_prices = soup.select(".list-card-price")
prices = [price.getText() for price in all_prices]
print(len(prices))

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(GOOGLE_FORM_URL)

for n in range(len(all_links)):
    sleep(2)
    first_question = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )
    first_question.click()
    first_question.send_keys(addresses[n])

    sleep(2)
    second_question = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )
    second_question.click()
    second_question.send_keys(prices[n])

    sleep(2)
    third_question = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )
    third_question.click()
    third_question.send_keys(links[n])

    sleep(2)
    submit_button = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span'
    )
    submit_button.click()

    sleep(3)
    submit_another_response = driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'
    )
    submit_another_response.click()
driver.quit()
