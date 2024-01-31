# blueprints/spotify_blueprint.py
from flask import Blueprint, render_template
from models import Artist

spotify_bp = Blueprint('spotify', __name__, template_folder='templates', url_prefix='/spotify')

@spotify_bp.route('/')
def spotify():
    artist_data = {
        'name': "Frank D'Angelo",
        'bio': "Brief biography and achievements...",
    }
    artist = Artist(**artist_data)
    return render_template('spotify.html', artist=artist)
