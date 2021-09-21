from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
articles_texts = []
articles_links = []

for article_tag in articles:
    texts = article_tag.getText()
    articles_texts.append(texts)

    links = article_tag.get("href")
    articles_links.append(links)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(articles_texts)
# print(articles_links)
# print(article_upvotes)

max_upvote = max(article_upvotes)
max_upvote_index = article_upvotes.index(max_upvote)

print(articles_texts[max_upvote_index])
print(articles_links[max_upvote_index])


















# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
#
# # print(soup.prettify())
#
# print(soup.a)
# print(soup.li)
# print(soup.p)
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# all_para_tags = soup.find_all(name="p")
# print(all_para_tags)
#
# for tag in all_anchor_tags:
#     print(tag.string)
#     # or print(tag.gettexts())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# company_url = soup.select_one(selector="#name")
# print(company_url)
#
# headings = soup.select(".heading")
# print(headings)
