# blueprints/home_blueprint.py
from flask import Blueprint, render_template
from os import listdir
from os.path import isfile, join

home_bp = Blueprint('home', __name__, url_prefix='/', static_folder='static')

@home_bp.route('/')
def home():

    slideshow_folder = 'static/images/slideshow'
    slideshow_images = [f for f in listdir(slideshow_folder) if isfile(join(slideshow_folder, f))]

    inspiring_quotes = [
        {"quote": "Music is the divine way to tell beautiful, poetic things to the heart.", "author": "Pablo Casals"},
        {"quote": "Where words fail, music speaks.", "author": "Hans Christian Andersen"},
        {"quote": "Music can change the world because it can change people.", "author": "Bono"},
        {"quote": "The only truth is music.", "author": "Jack Kerouac"},
        {"quote": "Music gives a soul to the universe, wings to the mind, flight to the imagination, and life to everything.", "author": "Plato"},
        {"quote": "Without music, life would be a mistake.", "author": "Friedrich Nietzsche"},
        {"quote": "Music expresses that which cannot be said and on which it is impossible to be silent.", "author": "Victor Hugo"},
        {"quote": "The earth has music for those who listen.", "author": "William Shakespeare"},
        {"quote": "Music is the strongest form of magic.", "author": "Marilyn Manson"},
        {"quote": "Music is the universal language of mankind.", "author": "Henry Wadsworth Longfellow"}
    ]

    # Combine the quotes and slideshow_images into a list of dictionaries
    slides_data = [
        {'image': image, 'quote': quote['quote'], 'author': quote['author']}
        for image, quote in zip(slideshow_images, inspiring_quotes)
    ]



    return render_template('home.html', slides_data=slides_data)
