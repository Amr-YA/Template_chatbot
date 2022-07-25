# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions



from importlib_metadata import metadata
import rasa_sdk
import os, re
from rasa_sdk.types import DomainDict
from rasa_sdk.interfaces import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import SlotSet, FollowupAction, EventType, ActionExecuted, SessionStarted
from typing import Any, Text, Dict, List, Optional

class qr_action(Action):
    def name(self) -> Text:
        return "qr_action"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:

        dispatcher.utter_message(text="message with 6 quick replies",
                                 quick_replies = [
                                            {"content_type":"text","payload": "qr_1", "title": "one"},
                                            {"content_type":"text","payload": "qr_2", "title": "two"},
                                            {"content_type":"text","payload": "qr_3", "title": "three"},
                                            {"content_type":"text","payload": "qr_4", "title": "four"},
                                            {"content_type":"text","payload": "qr_5", "title": "five"},
                                            {"content_type":"text","payload": "qr_6", "title": "six"},
                                            ],

        )
        return []

class btn_action(Action):
    def name(self) -> Text:
        return "btn_action"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:

        dispatcher.utter_message(text="message with 3 buttons",
                                 buttons = [{"payload": "button_1", "title": "one"},
                                            {"payload": "button_2", "title": "two"},
                                            {"payload": "button_3", "title": "three"},
                                            ]
                                            )
        return []

