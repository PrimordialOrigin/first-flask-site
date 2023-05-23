from flask import Blueprint, render_template

bp_views = Blueprint('views', __name__, url_prefix='/')

@bp_views.route('/')
def Home():
    return render_template('home.html')
