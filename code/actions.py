# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

time_zones = {
    "cairo" : "UTC+1:00",
    "sofia" : "UTC+3:00",
    "mumbai": "UTC+1:30",
    "london": "UTC+1:00",
    "barcelona" : "UTC+2:00"
}

class ActionShowTimeZone(Action):

    def name(self) -> Text:
        return "action_show_time_zone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.get_slot("city")
        time_zone = time_zones.get(str(city).lower() , None)
        if time_zone :
            output = f"Time zone for {city} is {time_zone}."
        else :
            output= f"Sorry , I couldn't found the time zone for {city}." 


        dispatcher.utter_message(text=output)

        return []
