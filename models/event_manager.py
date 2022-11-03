from models.event import *
from datetime import date


event1 = Event(date(2022, 11, 3), "Some gig", 100, "cowgate", "some gig under a bridge with music and drinking", False)
event2 = Event(date(2022, 11, 4), "Another gig", 120, "usher hall", "big gig in a hall with no drinking", True)
events = [event1, event2]

def add_new_event(event):
    events.append(event)

def remove_event(index):
    events.pop(index)
