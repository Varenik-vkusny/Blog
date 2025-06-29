from . import main_bp
from flask import render_template
from my_app.models import Post
from flask_login import current_user, login_required

@main_bp.route('/')
def home():
    articles = Post.query.all()
    user_articles = []
    if current_user.is_authenticated:
        user_articles = Post.query.filter_by(author=current_user).all()
    return render_template('main_bp/home.html', title='Главная', articles=articles, user_articles=user_articles)

@main_bp.route('/profile')
@login_required
def profile():
    posts = Post.query.filter_by(author=current_user).all()
    return render_template('main_bp/profile.html', title='Профиль', posts=posts)