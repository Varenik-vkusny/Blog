from . import add_bp
from flask import render_template, redirect, flash, url_for
from my_app import db
from my_app.forms import PostForm
from my_app.models import Post
from flask_login import current_user, login_required

@add_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = PostForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            new_post = Post(title=form.title.data, content=form.content.data, author=current_user)
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('main_bp.home'))

    return render_template('add_bp/add.html', title='Добавление статьи', form=form)