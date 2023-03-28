from flask import Blueprint, render_template, redirect, url_for, request
from website.forms import ContactForm
from . import db
from website.models.db_models import Posts

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html")


@views.route('/return_home')
def return_home():
    return redirect(url_for('views.home'))


@views.route("/leaps")
def display_leap_years():
    leap_years = []
    for year in range(1900, 2100):
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            leap_years.append(year)
    return render_template("leap_years.html", leap_years=leap_years)


@views.route("/isleap", methods=["GET", "POST"])
def isleap():
    if request.method == "POST":
        year = int(request.form["year"])
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            message = f"{year} is a leap year!"
        else:
            message = f"{year} is not a leap year. Try again."
        return render_template("isleap.html", message=message)
    return render_template("isleap.html", message=None)


@views.route("/books")
def books():
    books = [
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction"},
        {"title": "Three body problem", "author": "Liu Cixin", "genre": "Science Fiction"},
        {"title": "Dune", "author": "Frank Herbert", "genre": "Science Fiction"},
    ]
    return render_template("books.html", books=books)


@views.route("/posts")
def posts():
    posts = Posts.query.all()
    return render_template('posts.html', posts=posts)


@views.route("/article/<book_name>")
def article(book_name):
    post = Posts.query.filter_by(book_name=book_name).first()
    return render_template('article.html', post=post)


@views.route('/add_post', methods=['GET', 'POST'])
def add_post():
    form = ContactForm()
    if form.validate_on_submit():
        post = Posts(data=form.data.data, autor=form.autor.data, book_name=form.book_name.data, comment=form.comment.data)
        db.session.add(post)
        db.session.commit()
        return render_template('post_added.html', form=form)
    return render_template('add_post.html', form=form)


@views.route('/delete_post/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post = Posts.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('views.posts'))


