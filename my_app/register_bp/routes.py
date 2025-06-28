from . import register_bp
from flask import redirect, render_template, flash, request, url_for
from my_app.forms import RegistrationForm
from my_app.models import User
from my_app import db

@register_bp.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():

        if User.query.filter_by(username=form.username.data).first():
            flash('Пользователь с таким именем уже существует.', 'danger')
            return redirect(url_for('register_bp.register'))
        if User.query.filter_by(email=form.email.data).first():
            flash('Пользователь с таким email уже существует.', 'danger')
            return redirect(url_for('register_bp.register'))

        new_user = User(username=form.username.data, email=form.email.data)

        new_user.set_password(form.password.data)

        try: 
            db.session.add(new_user)
            db.session.commit()
            flash('Вы успешно зарегистрированы!', 'success')
            return redirect(url_for('auth_bp.auth'))
        except Exception as e:
            db.session.rollback()
            flash('Произошла ошибка при регистрации. Пожалуйста, попробуйте еще раз.', 'danger')


    return render_template('register_bp/register.html', title='Регистрация', form=form)