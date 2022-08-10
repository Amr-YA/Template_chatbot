# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions



# from asyncio import ThreadedChildWatcher
from importlib_metadata import metadata
import rasa_sdk
import os, re
from rasa_sdk.types import DomainDict
from rasa_sdk.interfaces import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import SlotSet, FollowupAction, EventType, ActionExecuted, SessionStarted, UserUtteranceReverted
from typing import Any, Text, Dict, List, Optional
from rasa.shared.nlu.constants import INTENT_NAME_KEY, INTENT_RANKING_KEY


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

class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # assume there's a function to call customer service
        # pass the tracker so that the agent has a record of the conversation between the user
        # and the bot for context

        dispatcher.utter_message(text="Would you like to talk to our support agent", 
                                 buttons = [{"payload": "/handover", "title": "Talk to Agent"},])


        dispatcher.utter_message(text="Or you can try to rephrase your question")
        
        return [UserUtteranceReverted()]

class ActionDefaultAskAffirmation(Action):
    def name(self):
            return "action_default_ask_affirmation"
    async def run(self, dispatcher, tracker, domain):
        # select the top three intents from the tracker        
        # ignore nlu fallback, out of scope

        predicted_intents = tracker.latest_message["intent_ranking"]
        to_affirm_intents = []
        for intent in predicted_intents:
            if intent["name"] not in ["nlu_fallback", "out_of_scope"]:
                to_affirm_intents.append(intent)

        # A prompt asking the user to select an option
        message = "Sorry! What do you want to do?"
        # a mapping between intents and user friendly wordings
        intent_mappings = {
                            "msg": "Simple Message",
                            "btn": "Button Message",
                            "qr": "Quick Reply Message",
                            "qr_payload": "Quick Reply Payload",
                            "bt_payload": "Button Payload",
                            "handover" : "Handover to Agent",
        }
        # show the top three intents as buttons to the user
        buttons = []
        for i, intent in enumerate(to_affirm_intents):
            buttons.append( 
                {
                    "title": intent_mappings[intent['name']],
                    "payload": "/{}".format(intent['name'])
                }
            )
            if i == 2: break 
                
        # add a "none of these button", if the user doesn't
        # agree when any suggestion
        # buttons.append({
        #     "title": "None of These",
        #     "payload": "/out_of_scope"
        # })
        dispatcher.utter_message(text=message, buttons=buttons)
        return []