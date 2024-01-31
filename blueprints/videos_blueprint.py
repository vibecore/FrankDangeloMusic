# blueprints/videos_blueprint.py
from flask import Blueprint, render_template
from models import Artist
from googleapiclient.discovery import build

videos_bp = Blueprint('videos', __name__, url_prefix='/videos')

@videos_bp.route('/')
def videos():
    youtube_api_key = 'AIzaSyAQQwSHf1pXFTp7MdeIICOvivGTatT6JvA'
    youtube_channel_id = 'UCEwQys7xPXKRzOgIkjBYr1Q'

    youtube = build('youtube', 'v3', developerKey=youtube_api_key)
    # Get the playlist ID for the "Acoustic Performances" playlist
    playlists_response = youtube.playlists().list(part='snippet', channelId=youtube_channel_id, maxResults=50).execute()
    acoustic_performances_playlist = next((playlist for playlist in playlists_response['items'] if playlist['snippet']['title'] == 'Acoustic Performances'), None)

    if not acoustic_performances_playlist:
        return render_template('videos.html', videos=[])

    playlist_id = acoustic_performances_playlist['id']

    videos = []
    next_page_token = None

    while True:
        # Request a page of videos
        videos_response = youtube.playlistItems().list(playlistId=playlist_id, part='snippet', maxResults=50, pageToken=next_page_token).execute()
        videos.extend(videos_response['items'])

        # Check if there are more pages
        next_page_token = videos_response.get('nextPageToken')
        if not next_page_token:
            break

    return render_template('videos.html', videos=videos)
