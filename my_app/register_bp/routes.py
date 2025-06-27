from . import register_bp
from flask import redirect, render_template, flash, request

@register_bp.route('/')
def register():
    return render_template('register.html', title='Регистрация')