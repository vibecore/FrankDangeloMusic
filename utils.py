# utils.py
from datetime import datetime
from urllib.parse import quote

def format_event_date(date_string):
    # Convert string to datetime object
    date_object = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
    
    # Format the date as "Thursday, Feb 1st @ 8pm"
    formatted_date = date_object.strftime('%A, %b %dth @ %I:%M%p').replace('1th', '1st').replace('2th', '2nd').replace('3th', '3rd')
    
    return formatted_date

def get_google_url(venue_name, city, state):
    # Encode venue name, city, and state for the URL
    encoded_query = f"{venue_name} {city} {state}".replace(" ", "+")

    # Construct the Google Maps search link
    google_maps_url = f"https://www.google.com/maps/search/?api=1&query={encoded_query}"

    return google_maps_url
