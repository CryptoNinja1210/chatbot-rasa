# This files contains your custom actions which can be used to run
# custom Python code.////// rasa train --config config.yml --endpoints endpoints.yml
#rasa run -m models --enable-api --cors "*" --debug //// pip install SQLAlchemy<2.0 //// pip install --upgrade pip
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionAddDestinaton(Action):
    def name(self) -> Text:
        return "action_add_destination"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entity_to = next(tracker.get_latest_entity_values(entity_type="location", entity_role="to"), None)
        slot_main_destination = tracker.get_slot('main_destination')
        slot_include_point = tracker.get_slot('include-point')
        if slot_main_destination is None:
            return [SlotSet("main_destination", entity_to)]
        else:
            if slot_include_point is not None:
                slot_include_point.append(entity_include_point)
            else:
                slot_include_point = [entity_include_point]
                return [SlotSet("include-point", entity_to)]
