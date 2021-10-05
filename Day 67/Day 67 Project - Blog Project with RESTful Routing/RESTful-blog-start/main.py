from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from typing import Callable
import datetime as dt


# # Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

# #CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class MySQLAlchemy(SQLAlchemy):
    Column: Callable
    String: Callable
    Integer: Callable
    Boolean: Callable
    Text: Callable


db = MySQLAlchemy(app)


# #CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# # WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    print(posts)
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    posts = db.session.query(BlogPost).all()
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/new-post', methods=["GET", "POST"])
def make_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        post_title = form.title.data
        post_subtitle = form.subtitle.data
        post_author = form.author.data
        post_img_url = form.img_url.data
        post_content = form.body.data

        now = dt.datetime.now()
        post_date = now.strftime("%B %d, %Y")

        new_post = BlogPost(
            title=post_title,
            date=post_date,
            body=post_content,
            author=post_author,
            img_url=post_img_url,
            subtitle=post_subtitle,
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=form, is_edit=False)


@app.route('/edit-post/<int:post_id>', methods=["GET", "POST"])
def edit_post(post_id):
    current_post = db.session.query(BlogPost).get(post_id)
    print(current_post.title)
    edit_form = CreatePostForm(
        title=current_post.title,
        subtitle=current_post.subtitle,
        img_url=current_post.img_url,
        author=current_post.author,
        body=current_post.body
    )
    if edit_form.validate_on_submit():
        current_post.title = edit_form.title.data
        current_post.subtitle = edit_form.subtitle.data
        current_post.img_url = edit_form.img_url.data
        current_post.author = edit_form.author.data
        current_post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=edit_form, is_edit=True)


@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    current_post = BlogPost.query.get(post_id)
    db.session.delete(current_post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
