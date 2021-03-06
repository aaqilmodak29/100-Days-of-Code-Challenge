import requests
import smtplib
import lxml
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=bmx_dp_m06t6qvo" \
      "_1/147-2934311-5792667?pd_rd_w=uVGiM&pf_rd_p=f43599e0-aaab-4357-b62a-afc3efe44d3b&pf_rd_" \
      "r=P1HKWDRSPP1KBZVT0MCR&pd_rd_r=d884ca12-d681-44d0-b7e8-af23502c8da3&pd_rd_wg=N2N7i&pd_rd_i=B00FLYWNYQ&psc=1"
MY_EMAIL = ""
PASSWORD = ""

# http://myhttpheader.com/ - visit this website for your headers

headers = {
    "User-Agent": "",
    "Accept-Language": ""
}

response = requests.get(url=URL, headers=headers)
amazon_price = response.text.encode('utf8').decode('ascii', 'ignore')

soup = BeautifulSoup(amazon_price, "lxml")
price = soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString")
title = soup.find(name="span", id="productTitle")

price_of_product = float(price.getText().split("$")[1])
title_of_product = title.getText()

if price_of_product < 80:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="",
                            msg="Subject:Amazon Price Alert!\n\n"
                                f"{title_of_product} is now ${price_of_product}. Buy Now!\n{URL}")
