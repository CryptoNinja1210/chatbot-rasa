# This files contains your custom actions which can be used to run
# custom Python code.////// rasa train --config config.yml --endpoints endpoints.yml
#rasa run -m models --enable-api --cors "*" --debug //// pip install SQLAlchemy<2.0 //// pip install --upgrade pip
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionDefaultFallback(Action):
    def name(self) -> Text:
            return "action_default_fallback"
    def run(self, dispatcher, tracker, domain):
        # output a message saying that the conversation will now be
        # continued by a human.

        message = "Sorry! Let me connect you to a human..."
        dispatcher.utter_message(text=message)
        # pause tracker
        # undo last user interaction
        return [ConversationPaused(), UserUtteranceReverted()]
