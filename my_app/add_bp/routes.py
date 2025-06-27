from . import add_bp
from flask import render_template, redirect, flash

@add_bp.route('/')
def add():
    return render_template('add.html', title='Добавление статьи')