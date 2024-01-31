# blueprints/photos_blueprint.py
from flask import Blueprint, render_template, send_from_directory, request
from os import listdir
from os.path import isfile, join

photos_bp = Blueprint('photos', __name__, template_folder='templates', url_prefix='/photos')

@photos_bp.route('/')
def photos():
    page = request.args.get('page', 1, type=int)
    per_page = 8 if request.user_agent.platform != 'iphone' else 1

    photos_path = 'static/images/photos'
    photo_files = [f for f in listdir(photos_path) if isfile(join(photos_path, f))]

    total_photos = len(photo_files)
    num_pages = (total_photos + per_page - 1) // per_page  # Calculate total pages

    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    paginated_photos = photo_files[start_index:end_index]

    return render_template('photos.html', photo_files=paginated_photos, page=page, num_pages=num_pages)

@photos_bp.route('/thumbnail/<filename>')
def thumbnail(filename):
    return send_from_directory('static/images/photos', filename)

@photos_bp.route('/view/<filename>')
def view_photo(filename):
    return render_template('view_photo.html', filename=filename)
