from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from typing import Callable

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class MySQLAlchemy(SQLAlchemy):
    Column: Callable
    Integer: Callable
    String: Callable


db = MySQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


# # CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

# Line below only required once, when creating DB.
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get('name')
        mail = request.form.get('email')
        pwd = request.form.get('password')
        hashed_pwd = generate_password_hash(pwd, method='pbkdf2:sha256', salt_length=8)

        user = User.query.filter_by(email=mail).first()
        if user:
            error = "You have already registered using that email, login instead!"
            return render_template('login.html', error=error)
        else:
            new_user = User(
                email=mail,
                password=hashed_pwd,
                name=name
            )
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user)
            return redirect(url_for('secrets'))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["POST", "GET"])
def login():
    error = None
    if request.method == "POST":
        mail = request.form.get('email')
        pwd = request.form.get('password')

        user = User.query.filter_by(email=mail).first()
        if user:
            if check_password_hash(user.password, pwd):
                login_user(user)
                return redirect(url_for('secrets'))
            else:
                error = "Invalid Password"
        else:
            error = "Invalid Email"
    return render_template("login.html", error=error, logged_in=current_user.is_authenticated)


@login_required
@app.route('/secrets')
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@login_required
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@login_required
@app.route('/download')
def download():
    return send_from_directory('static', "files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
