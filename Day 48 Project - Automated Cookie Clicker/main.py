from selenium import webdriver
import time

chrome_driver_path = ""
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_id("cookie")

items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60 * 5

while True:
    cookie.click()

    if time.time() > timeout:

        prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []

        for price in prices:
            text = price.text
            if text != "":
                cost = int(text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        money = driver.find_element_by_id("money").text
        if "," in money:
            money = money.replace(",", "")
        cookie_count = int(money)

        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        most_affordable_upgrade = max(affordable_upgrades)
        print(most_affordable_upgrade)
        purchase_id = affordable_upgrades[most_affordable_upgrade]

        driver.find_element_by_id(purchase_id).click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break
