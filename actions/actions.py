# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
# Ham lay ket qua so xo va tra ve. Ten ham la action_get_lottery
import feedparser
class action_get_lottery(Action):
   def name(self):
          return 'action_get_lottery'
   def run(self, dispatcher, tracker, domain):
            # Khai bao dia chi luu tru ket qua so xo. O day lam vi du nen minh lay ket qua SX Mien Bac
            url = 'https://xskt.com.vn/rss-feed/mien-bac-xsmb.rss'
            feed_cnt = feedparser.parse(url)
            # Lay ket qua so xo moi nhat
            first_node = feed_cnt['entries']
            # Lay thong tin ve ngay va chi tiet cac giai
            return_msg = first_node[0]['title'] + "\n" + first_node[0]['description']
            # Tra ve cho nguoi dung
            dispatcher.utter_message(return_msg)
            return []
