from . import auth_bp
from flask import render_template, redirect, flash

@auth_bp.route('/')
def auth():
    return render_template('auth.html', title="Авторизация")