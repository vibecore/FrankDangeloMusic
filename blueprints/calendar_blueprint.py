# calendar_blueprint.py
from flask import Blueprint, render_template
from utils import format_event_date, get_google_url
import requests

calendar_bp = Blueprint('calendar', __name__, url_prefix='/calendar')

@calendar_bp.route('/')
def calendar():

    #BandIsInTown API Credentials
    bandsintown_app_id = '42b4f6d6fc077a51a5f4b7a2976550ac'
    bandsintown_name = "FrankDAngelo"


    # Bandsintown API endpoint for upcoming events
    bandsintown_api_url = f"https://rest.bandsintown.com/artists/{bandsintown_name}/events"

    # Specify Bandsintown API parameters (you may need to use your own Bandsintown API key)
    bandsintown_params = {
        'app_id': bandsintown_app_id,
        'date': 'upcoming'
    }

    try:
        # Make the API request to Bandsintown
        response = requests.get(bandsintown_api_url, params=bandsintown_params)
        events = response.json()

        # Process events and format dates
        for event in events:
            # Format Bandsintown date to match the expected format
            event['datetime'] = event['datetime'].replace('T', ' ')
            event['formatted_date'] = format_event_date(event['datetime'])

            # Generate Google Search link for directions
            event['google_search_link'] = get_google_url(event['venue']['name'], event['venue']['city'], event['venue']['region'])

    except requests.RequestException as e:
        print(f"Error fetching events from Bandsintown: {e}")
        events = []  # Empty events in case of an error

    return render_template('calendar.html', events=events)
