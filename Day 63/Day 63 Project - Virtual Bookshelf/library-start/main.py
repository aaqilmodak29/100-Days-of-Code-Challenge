from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from typing import Callable
import os

file_path = os.path.abspath(os.getcwd()) + "/book-library.db"

app = Flask(__name__)
app.config['SECRET_KEY'] = ''  # any string
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + file_path
#  if you get a deprecation warning in the console that's related to SQL_ALCHEMY_TRACK_MODIFICATIONS,
#  you can silence it with this line of code
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)


class MySQLAlchemy(SQLAlchemy):
    Column: Callable
    String: Callable
    Integer: Callable


db = MySQLAlchemy(app)


class BookForm(FlaskForm):
    book_name = StringField('Book Name', validators=[DataRequired()])
    book_author = StringField('Book Author', validators=[DataRequired()])
    book_rating = StringField('Book Rating', validators=[DataRequired()])
    submit = SubmitField('Add Book')


class Book(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(250), unique=True, nullable=False)
    author = db.Column("author", db.String(250), nullable=False)
    rating = db.Column("rating", db.Integer, nullable=False)

# # create database by running this line of code
# db.create_all()


@app.route('/')
def home():
    # read all data from database, returns a list
    all_books = db.session.query(Book).all()
    length = len(all_books)
    return render_template('index.html', len_of_books=length, books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    if request.method == 'POST':
        name_of_book = form.book_name.data
        name_of_author = form.book_author.data
        rating_of_book = form.book_rating.data

        # adding entry to the database
        new_book = Book(title=name_of_book, author=name_of_author, rating=rating_of_book)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('add.html', form=form)


@app.route('/edit', methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # id from form in edit.html
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    # id from url passed in index.html on line 12
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template('edit.html', books=book_selected)


@app.route('/delete', methods=["GET", "POST"])
def delete():
    book_id = request.args.get('id')
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

