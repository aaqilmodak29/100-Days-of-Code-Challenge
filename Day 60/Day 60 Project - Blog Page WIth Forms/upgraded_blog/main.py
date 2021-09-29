from flask import Flask, render_template, request
from post import Post
import smtplib

all_posts = Post().posts()
MY_EMAIL = ""  # your email
PASSWORD = ""  #your password


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


@app.route('/contact.html', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['username']
        mail = request.form['email']
        number = request.form['phone-no']
        message = request.form['msg']

        print(name)
        print(mail)
        print(number)
        print(message)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="",  # recipient's email
                                msg=f"Subject: New Message\n\n{name}\n{mail}\n{number}\n{message}")

        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route('/post.html/<int:number>')
def posts(number):
    return render_template("post.html", posts=all_posts, num=number)


if __name__ == "__main__":
    app.run(debug=True)

