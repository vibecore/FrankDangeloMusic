# blueprints/about_blueprint.py
from flask import Blueprint, render_template
from models import Artist

about_bp = Blueprint('about', __name__, url_prefix='/about')

@about_bp.route('/')
def about():
    artist_data = {
        'name': "Frank D'Angelo",
        'bio': ""
    }
    artist = Artist(**artist_data)
    return render_template('about.html', artist=artist)

