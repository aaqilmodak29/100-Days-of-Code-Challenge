from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from typing import Callable
import requests
import os

API_KEY = ""  # your api key
URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DETAILS_URL = "https://api.themoviedb.org/3/movie/"

file_path = os.path.abspath(os.getcwd()) + "/movies.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + file_path
app.config['SECRET_KEY'] = ''  # any string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)


class MySQLAlchemy(SQLAlchemy):
    Column: Callable
    String: Callable
    Integer: Callable


db = MySQLAlchemy(app)


class Movie(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(250), unique=True, nullable=False)
    year = db.Column("year", db.Integer, nullable=False)
    description = db.Column("description", db.String(250), nullable=False)
    rating = db.Column("rating", db.Integer)
    ranking = db.Column("ranking", db.Integer)
    review = db.Column("review", db.String(250))
    img_url = db.Column("img_url", db.String(250), nullable=False)


class MovieForm(FlaskForm):
    edit_rating = StringField("Your Rating Out of 10 (eg:7.5)", validators=[DataRequired()])
    edit_review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")


class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


# db.create_all()

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's "
#                 "sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to "
#                 "a jaw-dropping climax. ",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    length = len(all_movies)
    for i in range(length):
        all_movies[i].ranking = length - i
    db.session.commit()
    return render_template("index.html", length=length, movies=all_movies)


@app.route('/edit', methods=["GET", "POST"])
def edit():
    form = MovieForm()
    movie_id = request.args.get('id')
    movie_to_update = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie_to_update.rating = float(form.edit_rating.data)
        movie_to_update.review = form.edit_review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form, movie=movie_to_update)


@app.route('/delete', methods=["GET", "POST"])
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        parameters = {
            "api_key": API_KEY,
            "query": form.title.data
        }
        response = requests.get(url=URL, params=parameters)
        data = response.json()['results']
        return render_template('select.html', data=data)
    return render_template('add.html', form=form)


@app.route('/find', methods=["GET", "POST"])
def add_to_db():
    movie_id = request.args.get('id')
    parameters = {
        "api_key": API_KEY,
    }
    response = requests.get(url=f"{MOVIE_DETAILS_URL}/{movie_id}", params=parameters)
    data = response.json()
    new_movie = Movie(
        title=data['title'],
        year=data['release_date'].split('-')[0],
        description=data['overview'],
        img_url=f"https://www.themoviedb.org/t/p/w500{data['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
