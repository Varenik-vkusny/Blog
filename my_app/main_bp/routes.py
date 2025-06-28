from . import main_bp
from flask import render_template

@main_bp.route('/')
def home():
    return render_template('main_bp/home.html', title='Главная')

@main_bp.route('/profile')
def profile():
    return render_template('main_bp/profile.html', title='Профиль')