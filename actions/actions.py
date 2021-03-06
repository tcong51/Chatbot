# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.forms import FormAction
import mysql.connector
import feedparser
#-------------------------------------------------------------------------------------------------------------
class action_typeland(Action):

    def name(self):
        return "action_typeland"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        typeLandVariable = tracker.get_slot("typeland")
        typeLandArray= [] 
        myconn = mysql.connector.connect(host = "localhost", user = "root", 
            passwd = "",database="data_trees")
        curTree =myconn.cursor()
        codeOfLand = "SELECT * FROM landtype WHERE LandName LIKE '{}'".format(typeLandVariable)
        curTree.execute(codeOfLand)
        result = curTree.fetchall()
        for x in result:
            typeLandArray.append(x[0])
        myconn.rollback()
        myconn.close()
        # Code của loại đất
        codeOfVariable = typeLandArray[0]
        
        treeReturn = []
        myconn = mysql.connector.connect(host = "localhost", user = "root", 
                    passwd = "",database="data_trees")
        curTree =myconn.cursor()
        treeOfLand = "SELECT * FROM db_trees WHERE LandType LIKE '%{}%'".format(codeOfVariable)
        curTree.execute(treeOfLand)  
        result = curTree.fetchall()
        for x in result:
            treeReturn.append(x[1])
        myconn.rollback()
        myconn.close()
        dispatcher.utter_message("Các cây trồng có thể trồng trên "+ typeLandVariable + " là:")
        for x in treeReturn:
            dispatcher.utter_message(x)  
        return []

#------------------------------------------------------------------------------------------------------------------

# class action_get_lottery(Action):
#    def name(self):
#           return 'action_get_lottery'
#    def run(self, dispatcher, tracker:Tracker, domain)-> List[Text]:
#             # Khai bao dia chi luu tru ket qua so xo. O day lam vi du nen minh lay ket qua SX Mien Bac
#             url = 'https://xskt.com.vn/rss-feed/mien-bac-xsmb.rss'
#             # Tien hanh lay thong tin tu URL
#             feed_cnt = feedparser.parse(url)
#             # Lay ket qua so xo moi nhat
#             first_node = feed_cnt['entries']
#             # Lay thong tin ve ngay va chi tiet cac giai
#             return_msg = first_node[0]['title'] + "\n" + first_node[0]['description']
#             # Tra ve cho nguoi dung
#             dispatcher.utter_message(return_msg)
#             return []
# #-------------------------------------------------------------------------------------------------------------

# class action_land_mun(Action):
#   def name(self):
#           return 'action_land_mun'
#   def run(self,dispatcher, tracker, domain):
#             trees =[]
#             nameland = []
#             n = 1
#             # tạo đối tượng connection
#             # Tryền tham số giống như chatbot thông minh, select trong landtype -> code  -> select trong db_trees lấy cây.
#             myconn = mysql.connector.connect(host = "localhost", user = "root", 
#                 passwd = "",database="data_trees")
#             # tạo đối tượng cursor
#             cur = myconn.cursor()
#             query = "SELECT * FROM db_trees WHERE LandType LIKE '%{:d}%'".format(n)
#             # print (query)
#                 # select dữ liệu từ database
#             cur.execute(query)
#             # Chỉ số landtype -> varchar 1,2 ..... tìm loại cây rộng hơn. Nếu cây thuộc 2 loại cây trở lên
#             # nameland = cur.execute("SELECT LandName FROM landtype WHERE Code='%d'".format(n))
#             # r = cur.fetchall(nameland)
#                 # tìm nạp các hàng từ đối tượng con trỏ  
#             result = cur.fetchall()
#                 # print(result);
#             for x in result:
#                 trees.append(x[1])
#             myconn.rollback()
#             myconn.close()
# #-------------------------------------------------------------------------------------------------------------

#             myconn = mysql.connector.connect(host = "localhost", user = "root", 
#                 passwd = "",database="data_trees")
#             cur2 =myconn.cursor()
#             query = "SELECT * FROM landtype WHERE Code LIKE '%{:d}%'".format(n)
#             cur2.execute(query)
#             r = cur2.fetchall()
#             for x in r:
#                 nameland.append(x[1])
# #-------------------------------------------------------------------------------------------------------------

#             dispatcher.utter_message("Các cây trồng có thể trồng trên "+ nameland[0].lower() + " là:")
#             for name in trees:
#               dispatcher.utter_message(name)
#             return []
#-------------------------------------------------------------------------------------------------------------
