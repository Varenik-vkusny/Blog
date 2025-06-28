from . import auth_bp
from flask import render_template, redirect, flash, url_for
from flask_login import logout_user, login_user
from my_app.forms import LoginForm
from my_app.models import User

@auth_bp.route('/login', methods=['GET', 'POST'])
def auth():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main_bp.profile'))
        else:
            flash('Неверный email или пароль. Пожалуйста, попробуйте еще раз.', 'danger')
            return redirect(url_for('auth_bp.auth'), form=form)

    return render_template('auth_bp/auth.html', title="Авторизация")


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main_bp.home'))