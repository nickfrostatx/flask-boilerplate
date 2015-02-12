from flask import request, g, redirect
from random import choice
from urllib.parse import quote
from .models import Session
import string

def random_string(num):
    s = ''
    for x in range(num):
        s += choice(string.ascii_letters + string.digits)
    return s

def enforce_auth():
    g.user_id = None
    session_key = request.cookies.get('key')
    if session_key is not None:
        session = Session.query.filter_by(key=session_key).first()
        if session is not None:
            g.user_id = session.user_id
    if g.user_id is None:
        return redirect('/login/?next=' + quote(request.path), code=302)
