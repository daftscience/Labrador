# -*- coding: utf-8 -*-
"""file section, including homepage and signup."""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user

from labrador.extensions import login_manager
from labrador.file.forms import LoginForm
from labrador.user.forms import RegisterForm
from labrador.user.models import User
from labrador.utils import flash_errors

blueprint = Blueprint('settings', __name__, static_folder='../static')


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@blueprint.route('/settings', methods=['GET', 'POST'])
def home():
    """Home page."""
    form = LoginForm(request.form)
    # Handle logging in
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            flash('You are logged in.', 'success')
            redirect_url = request.args.get('next') or url_for('user.members')
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template('settings/home.html', form=form, page="settings", left="search", right="")
