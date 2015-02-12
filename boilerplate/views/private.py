from flask import Blueprint, request, g, redirect, flash, render_template
from ..models import db, Session
from ..util import enforce_auth

private = Blueprint(__name__, 'public')

private.before_request(enforce_auth)

@private.route('/')
def home():
    return render_template('home.html')
