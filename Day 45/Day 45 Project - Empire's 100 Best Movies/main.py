from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.timeout.com/newyork/movies/best-movies-of-all-time")
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")
all_movies = [movie.getText() for movie in soup.find_all(name="h3", class_="_h3_cuogz_1")]
# for movie in all_movies:
#     print(movie.split())

with open("movie.txt", mode="w") as file:
    for movie in all_movies[:-1]:
        file.write(f"{movie}\n")


