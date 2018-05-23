from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime
import os 



def add(filename,summary,startdatetime,enddatetime,attendees,location="",description=""):
    SCOPES = 'https://www.googleapis.com/auth/calendar'
    store = file.Storage(filename)
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets("client_secret.json", SCOPES)
        creds = tools.run_flow(flow, store)
    guests=[{'email': 'traveldglobe.com@gmail.com'},{'email': 'himanshujain.2792@gmail.com'},{'email':'jainjainhimanshu@gmail.com'}]

    for i in attendees:
        guests.append(i)
    service = build('calendar', 'v3', http=creds.authorize(Http()))
    event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start':{ 'dateTime':startdatetime ,'timeZone': 'Asia/Kolkata'},
        'end': {'dateTime': enddatetime,'timeZone': 'Asia/Kolkata'},
        'recurrence': [ 'RRULE:FREQ=DAILY;COUNT=1'],
        'attendees':guests,
        'reminders': {'useDefault': False,
        'overrides':[{'method': 'popup', 'minutes': 24*60},{'method': 'popup', 'minutes': 48*60},{'method': 'email', 'minutes': 48*60},{'method': 'email', 'minutes': 96*60}]
                }
        }
    event = service.events().insert(calendarId='primary', body=event, sendNotifications=True).execute()
    print ("Event created")