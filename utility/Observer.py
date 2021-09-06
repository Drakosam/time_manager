from enum import Enum
from typing import List


class EventName(Enum):
    NewCategory = 1
    UpdateCategory = 2
    NewItem = 3
    UpdateItem = 4
    UpdateDetails = 5
    SelectCategory = 6
    SelectItem = 7
    LoadFile = 8


class EventCall:
    def __init__(self, name: EventName, event):
        self.name = name
        self.event = event

    def execute(self, name):
        if name == self.name:
            self.event()


class Observer:
    def __init__(self):
        self.events_to_call: List[EventCall] = []

    def register_event(self, name: EventName, event):
        self.events_to_call.append(EventCall(name, event))

    def call(self, name: EventName):
        for event in self.events_to_call:
            event.execute(name)
