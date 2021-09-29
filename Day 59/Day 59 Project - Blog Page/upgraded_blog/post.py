import requests

BLOG_URL = "https://api.npoint.io/ed99320662742443cc5b"


class Post:
    def __init__(self):
        response = requests.get(url=BLOG_URL)
        self.all_posts = response.json()

    def posts(self):
        return self.all_posts

