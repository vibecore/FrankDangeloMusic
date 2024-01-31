# blueprints/contact_blueprint.py
from flask import Blueprint, render_template
from models import Artist

contact_bp = Blueprint('contact', __name__, template_folder='templates', url_prefix='/contact')

@contact_bp.route('/')
def contact():
    artist_data = {
        'name': "Frank D'Angelo",
        'bio': "Brief biography and achievements...",
    }
    artist = Artist(**artist_data)
    return render_template('contact.html', artist=artist)
