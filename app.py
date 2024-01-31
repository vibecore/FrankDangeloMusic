# app.py
from flask import Flask
from blueprints.about_blueprint import about_bp
from blueprints.photos_blueprint import photos_bp
from blueprints.videos_blueprint import videos_bp
from blueprints.spotify_blueprint import spotify_bp
from blueprints.contact_blueprint import contact_bp
from blueprints.home_blueprint import home_bp
from blueprints.calendar_blueprint import calendar_bp


app = Flask(__name__)
app.config['TRAILING_SLASH'] = False

app.register_blueprint(about_bp)
app.register_blueprint(photos_bp)
app.register_blueprint(videos_bp)
app.register_blueprint(spotify_bp)
app.register_blueprint(contact_bp)
app.register_blueprint(home_bp)
app.register_blueprint(calendar_bp)

if __name__ == '__main__':
    app.run(debug=True)
