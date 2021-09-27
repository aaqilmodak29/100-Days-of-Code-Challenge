from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def root_page():
    return '<h1>Guess a number between 0 and 9 and enter that number in the URL above!</h1>' \
           '<img src="https://media2.giphy.com/media/8Lc5xmvzRhlLy/100.webp?cid' \
           '=ecf05e47xde56j1u0vv9vrjqcj38kizribkcj54311nfbjmu&rid=100.webp&ct=g"' \
           'width=400px; height=auto> '


number = random.randint(0, 9)


@app.route('/<int:guess>')
def higher_or_lower(guess):
    if guess < number:
        return '<h1 style="color: red;">Too low, try again!</h1>' \
               '<img src="https://media1.giphy.com/media/8GAjKbr1gu3MA/200w.webp?cid' \
               '=ecf05e47xde56j1u0vv9vrjqcj38kizribkcj54311nfbjmu&rid=200w.webp&ct=g" width=400px; height=auto> '
    elif guess > number:
        return '<h1 style="color: red;">Too high, try again!</h1>' \
               '<img src="https://media1.giphy.com/media/HyOOyynWxMxig/200w.webp?cid' \
               '=ecf05e47xde56j1u0vv9vrjqcj38kizribkcj54311nfbjmu&rid=200w.webp&ct=g" width=400px; height=auto> '
    else:
        return '<h1 style="color: green;">That is correct!</h1>' \
               '<img src="https://media3.giphy.com/media/f4V2mqvv0wT9m/giphy.gif?cid' \
               '=ecf05e47r4ekboo70vzpmcsjk8z6m2utv7azpjz3iykf6tzs&rid=giphy.gif&ct=g" width=400px; height=auto> '


if __name__ == "__main__":
    app.run(debug=True)
