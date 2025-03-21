from flask import Flask, request, jsonify, render_template
import openai
import google.auth
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle

app = Flask(__name__)

# Load OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Google Calendar API setup
SCOPES = ['https://www.googleapis.com/auth/calendar']
creds = None
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)
service = build('calendar', 'v3', credentials=creds)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']
    response = openai.Completion.create(
        engine="davinci",
        prompt=question,
        max_tokens=150
    )
    answer = response.choices[0].text.strip()
    return jsonify({'answer': answer})

@app.route('/create_event', methods=['POST'])
def create_event():
    event_data = request.json
    event = {
        'summary': event_data['summary'],
        'start': {
            'dateTime': event_data['start'],
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': event_data['end'],
            'timeZone': 'UTC',
        }
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    return jsonify({'status': 'Event created', 'event_id': event['id']})

if __name__ == '__main__':
    app.run(debug=True)