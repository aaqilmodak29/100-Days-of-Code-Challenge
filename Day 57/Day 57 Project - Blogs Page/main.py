from flask import Flask, render_template
from post import Post


app = Flask(__name__)
all_posts = Post().posts()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:number>')
def posts(number):
    return render_template("post.html", posts=all_posts, num=number)


if __name__ == "__main__":
    app.run(debug=True)
