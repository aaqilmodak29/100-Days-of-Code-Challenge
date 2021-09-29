from flask import Flask, render_template
from post import Post

all_posts = Post().posts()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/index.html')
def index():
    return render_template("index.html", posts=all_posts)


@app.route('/about.html')
def about():
    return render_template("about.html")


@app.route('/contact.html')
def contact():
    return render_template("contact.html")


@app.route('/post.html/<int:number>')
def posts(number):
    return render_template("post.html", posts=all_posts, num=number)


if __name__ == "__main__":
    app.run(debug=True)

