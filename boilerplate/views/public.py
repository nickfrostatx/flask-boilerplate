from flask import Blueprint, request, redirect, flash, render_template
from werkzeug.security import safe_str_cmp
from sqlalchemy.exc import IntegrityError
from bcrypt import gensalt, hashpw
from ..forms import LoginForm, SignupForm
from ..models import db, Session, User
from ..util import random_string

public = Blueprint(__name__, 'public')

@public.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    status = 200
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user is None:
            flash('No such user')
            status = 403
        elif not safe_str_cmp(hashpw(password, user.password), user.password):
            flash('Invalid username or password')
            status = 403
        else:
            session_key = random_string(32)
            session = Session(key=session_key, user_id=user.id)
            db.session.add(session)
            db.session.commit()
            resp = redirect(request.args.get('next') or '/', code=303)
            resp.set_cookie('key', session_key, max_age=(60 * 60 * 24 * 30),
                httponly=True, path='/')
            return resp
    return render_template('login.html', form=form), status

@public.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    status = 200
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = hashpw(form.password.data, gensalt())
        user = User(email=email, password=password)
        db.session.add(user)
        try:
            db.session.commit()
            flash('Signed up successfully')
        except IntegrityError:
            flash('User already exists with that email')
            status = 400
    return render_template('signup.html', form=form), status
