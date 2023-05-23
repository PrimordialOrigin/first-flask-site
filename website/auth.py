from flask import Blueprint

bp_auth = Blueprint('auth', __name__, url_prefix='/')

@bp_auth.route('/register')
def register():
    return "<p>register</p>"

@bp_auth.route('/login')
def login():
    return "<p>login</p>"

@bp_auth.route('/logout')
def logout():
    return "<p>logout</p>"