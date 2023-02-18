import datetime
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Replace with your Google Calendar API credentials
creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/calendar'])

# Replace with your calendar ID
calendar_id = 'primary'

# Set the start date for the events
start_date = datetime.datetime.now().date()

# Create a function to generate events
def create_event(day, event_number):
    start_time = datetime.datetime.combine(day, datetime.time(9, 0, 0))
    end_time = datetime.datetime.combine(day, datetime.time(10, 0, 0))
    event_name = f'Event {event_number}'
    event = {
        'summary': event_name,
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': end_time.isoformat(),
            'timeZone': 'America/Los_Angeles',
        },
    }
    service.events().insert(calendarId=calendar_id, body=event).execute()

# Initialize the Google Calendar API client
service = build('calendar', 'v3', credentials=creds)

# Generate events for the next 4 weeks on Mondays and Wednesdays
for i in range(1, 9):
    event_number = i
    for j in range(1, 8, 2):
        day = start_date + datetime.timedelta(days=(j + (i - 1) * 7))
        create_event(day, event_number)

#This script generates events on Mondays and Wednesdays for the next 4 weeks, with event names incrementing by 1 each time. 
#You'll need to replace the credentials and calendar ID with your own, 
#and you'll also need to have the necessary Google Calendar API access and permissions.