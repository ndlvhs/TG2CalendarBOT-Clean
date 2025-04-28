from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import datetime

from config import GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REFRESH_TOKEN

def get_calendar_service():
    creds = Credentials(
        token=None,
        refresh_token=GOOGLE_REFRESH_TOKEN,
        token_uri='https://oauth2.googleapis.com/token',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        scopes=["https://www.googleapis.com/auth/calendar"],
    )
    service = build('calendar', 'v3', credentials=creds)
    return service

def create_event(summary, start_time, duration_minutes=30):
    service = get_calendar_service()
    end_time = start_time + datetime.timedelta(minutes=duration_minutes)

    event = {
        'summary': summary,
        'start': {'dateTime': start_time.isoformat(), 'timeZone': 'Europe/Belgrade'},
        'end': {'dateTime': end_time.isoformat(), 'timeZone': 'Europe/Belgrade'},
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    return event.get('htmlLink')