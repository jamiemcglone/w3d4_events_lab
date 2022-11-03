from flask import render_template, request, redirect
from app import app
from models.event_manager import events, add_new_event, remove_event
from models.event import Event
from datetime import datetime

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events', methods=['POST'])
def add_event():
    event_date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
    event_name = request.form['name']
    event_guests = request.form['guests']
    event_location = request.form['location']
    event_description = request.form['description']
    event_recurring = bool(request.form['recurring'])
    new_event = Event(event_date, event_name, event_guests, event_location, event_description, event_recurring)
    add_new_event(new_event)
    print(new_event)
    return render_template('index.html', title='Home', events=events)

@app.route('/events/delete/<index>', methods=['POST'])
def delete_event(index):
    remove_event(int(index))
    return redirect('/events')
