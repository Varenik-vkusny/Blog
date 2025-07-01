from . import main_bp
from flask import render_template
from my_app.models import Post
from flask_login import current_user, login_required
from my_app.forms import CommentForm

@main_bp.route('/')
def home():
    posts = Post.query.all()
    form = CommentForm()
    user_posts = []
    if current_user.is_authenticated:
        user_posts = Post.query.filter_by(author=current_user).all()
    return render_template('main_bp/home.html', title='Главная', posts=posts, user_posts=user_posts, form=form)

@main_bp.route('/profile')
@login_required
def profile():
    posts = Post.query.filter_by(author=current_user).all()
    return render_template('main_bp/profile.html', title='Профиль', posts=posts)