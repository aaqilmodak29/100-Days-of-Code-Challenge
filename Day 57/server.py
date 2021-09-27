from flask import Flask, render_template
import random
import requests
import datetime as dt

app = Flask(__name__)
GENDERIZE_URL = "https://api.genderize.io"
AGIFY_URL = "https://api.agify.io"
BLOG_URL = "https://api.npoint.io/ed99320662742443cc5b"


@app.route('/')
def home():
    random_num = random.randint(0, 9)

    now = dt.datetime.now()
    year = now.year

    return render_template('index.html', num=random_num, current_year=year)


@app.route('/guess/<name>')
def name_gender(name):
    name = name.title()
    genderize_params = {
        "name": name
    }

    agify_params = {
        "name": name
    }
    genderize_response = requests.get(url=GENDERIZE_URL, params=genderize_params)
    gender = genderize_response.json()["gender"]

    agify_response = requests.get(url=AGIFY_URL, params=agify_params)
    age = agify_response.json()["age"]

    return render_template('page.html', name=name, gender=gender, age=age)


@app.route('/blog/<num>')
def blog_posts(num):
    print(num)
    response = requests.get(url=BLOG_URL)
    all_posts = response.json()

    return render_template('blog.html', posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
