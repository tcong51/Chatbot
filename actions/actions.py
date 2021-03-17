# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.forms import FormAction
import mysql.connector
import feedparser
#-------------------------------------------------------------------------------------------------------------
# #--------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
# #-------------------------------------------------------------------------------------------------------------
# #--------------------------------------------------------------------------------------------------------------
# #--------------------------------------------------------------------------------------------------------------
class action_area(Action):

    def name(self):
        return "action_area"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        areaVariable = tracker.get_slot("area")
        areaArray= [] 
        myconn = mysql.connector.connect(host = "localhost", user = "root", 
            passwd = "",database="data_trees")
        curTree =myconn.cursor()
        codeOfArea = "SELECT * FROM area WHERE Area LIKE '{}'".format(areaVariable)
        curTree.execute(codeOfArea)
        result = curTree.fetchall()
        for x in result:
            areaArray.append(x[0])
        myconn.rollback()
        myconn.close()
        # Code của area
        codeOfVariable = areaArray[0]
        
        treeReturn = []
        myconn = mysql.connector.connect(host = "localhost", user = "root", 
                    passwd = "",database="data_trees")
        curTree =myconn.cursor()
        treeOfArea = "SELECT * FROM db_trees WHERE Area LIKE '%{}%'".format(codeOfVariable)
        curTree.execute(treeOfArea)  
        result = curTree.fetchall()
        for x in result:
            treeReturn.append(x[1])
        myconn.rollback()
        myconn.close()
        dispatcher.utter_message("Các cây trồng có thể trồng ở khu vực "+ areaVariable + " là:")
        for x in treeReturn:
            dispatcher.utter_message(x)  
        return []


# #--------------------------------------------------------------------------------------------------------------
# #--------------------------------------------------------------------------------------------------------------
# #-------------------------------------------------------------------------------------------------------------
class action_benefit(Action):

    def name(self):
        return "action_benefit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        benefitVariable = tracker.get_slot("benefit")
        benefitArray= [] 
        myconn = mysql.connector.connect(host = "localhost", user = "root", 
            passwd = "",database="data_trees")
        curTree =myconn.cursor()
        codeOfBenefit = "SELECT * FROM benefit WHERE Benefit LIKE '{}'".format(benefitVariable)
        curTree.execute(codeOfBenefit)
        result = curTree.fetchall()
        for x in result:
            benefitArray.append(x[0])
        myconn.rollback()
        myconn.close()
        # Code của benefit
        codeOfVariable = benefitArray[0]
        
        treeReturn = []
        myconn = mysql.connector.connect(host = "localhost", user = "root", 
                    passwd = "",database="data_trees")
        curTree =myconn.cursor()
        treeOfBenefit = "SELECT * FROM db_trees WHERE Benefit LIKE '%{}%'".format(codeOfVariable)
        curTree.execute(treeOfBenefit)  
        result = curTree.fetchall()
        for x in result:
            treeReturn.append(x[1])
        myconn.rollback()
        myconn.close()
        dispatcher.utter_message("Các cây trồng dùng để "+ benefitVariable + " là:")
        for x in treeReturn:
            dispatcher.utter_message(x)  
        return []
# #--------------------------------------------------------------------------------------------------------------
# #--------------------------------------------------------------------------------------------------------------
# #--------------------------------------------------------------------------------------------------------------
class action_climate(Action):

    def name(self):
        return "action_climate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        climateVariable = tracker.get_slot("climate")
        climateArray= [] 
        myconn = mysql.connector.connect(host = "localhost", user = "root", 
            passwd = "",database="data_trees")
        curTree =myconn.cursor()
        codeOfClimate = "SELECT * FROM climate WHERE Climate LIKE '{}'".format(climateVariable)
        curTree.execute(codeOfClimate)
        result = curTree.fetchall()
        for x in result:
            climateArray.append(x[0])
        myconn.rollback()
        myconn.close()
        # Code của loại đất
        codeOfVariable = climateArray[0]
        
        treeReturn = []
        myconn = mysql.connector.connect(host = "localhost", user = "root", 
                    passwd = "",database="data_trees")
        curTree =myconn.cursor()
        treeOfClimate = "SELECT * FROM db_trees WHERE Climate LIKE '%{}%'".format(codeOfVariable)
        curTree.execute(treeOfClimate)  
        result = curTree.fetchall()
        for x in result:
            treeReturn.append(x[1])
        myconn.rollback()
        myconn.close()
        dispatcher.utter_message("Các cây trồng có thể trồng ở khí hậu "+ climateVariable + " là:")
        for x in treeReturn:
            dispatcher.utter_message(x)  
        return []
# #--------------------------------------------------------------------------------------------------------------
# #--------------------------------------------------------------------------------------------------------------
# #--------------------------------------------------------------------------------------------------------------

class action_growthtime(Action):

    def name(self):
        return "action_growthtime"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        growthtimeVariable = tracker.get_slot("growthtime")
        growthtimeArray= [] 
        myconn = mysql.connector.connect(host = "localhost", user = "root", 
            passwd = "",database="data_trees")
        curTree =myconn.cursor()
        codeOfGrowthTime = "SELECT * FROM growthtime WHERE Growthtime LIKE '{}'".format(growthtimeVariable)
        curTree.execute(codeOfGrowthTime)
        result = curTree.fetchall()
        for x in result:
            growthtimeArray.append(x[0])
        myconn.rollback()
        myconn.close()
        # Code của loại đất
        codeOfVariable = growthtimeArray[0]
        
        treeReturn = []
        myconn = mysql.connector.connect(host = "localhost", user = "root", 
                    passwd = "",database="data_trees")
        curTree =myconn.cursor()
        treeOfGrowthtime = "SELECT * FROM db_trees WHERE Growthtime LIKE '%{}%'".format(codeOfVariable)
        curTree.execute(treeOfGrowthtime)  
        result = curTree.fetchall()
        for x in result:
            treeReturn.append(x[1])
        myconn.rollback()
        myconn.close()
        dispatcher.utter_message("Các cây trồng   "+ growthtimeVariable + " là:")
        for x in treeReturn:
            dispatcher.utter_message(x)  
        return []
# #--------------------------------------------------------------------------------------------------------------
# #--------------------------------------------------------------------------------------------------------------
# #--------------------------------------------------------------------------------------------------------------
class action_humidity(Action):

    def name(self):
        return "action_humidity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        humidityVariable = tracker.get_slot("humidity")
        humidityArray= [] 
        myconn = mysql.connector.connect(host = "localhost", user = "root", 
            passwd = "",database="data_trees")
        curTree =myconn.cursor()
        codeOfHumidity = "SELECT * FROM humidity WHERE Humidity LIKE '{}'".format(humidityVariable)
        curTree.execute(codeOfHumidity)
        result = curTree.fetchall()
        for x in result:
            humidityArray.append(x[0])
        myconn.rollback()
        myconn.close()
        # Code của loại đất
        codeOfVariable = humidityArray[0]
        
        treeReturn = []
        myconn = mysql.connector.connect(host = "localhost", user = "root", 
                    passwd = "",database="data_trees")
        curTree =myconn.cursor()
        treeOfHumidity = "SELECT * FROM db_trees WHERE Humidity LIKE '%{}%'".format(codeOfVariable)
        curTree.execute(treeOfHumidity)  
        result = curTree.fetchall()
        for x in result:
            treeReturn.append(x[1])
        myconn.rollback()
        myconn.close()
        dispatcher.utter_message("Các cây trồng sống được ở độ ẩm "+ humidityVariable + " là:")
        for x in treeReturn:
            dispatcher.utter_message(x)  
        return []

# #--------------------------------------------------------------------------------------------------------------
# #--------------------------------------------------------------------------------------------------------------
# #--------------------------------------------------------------------------------------------------------------
class action_landtype(Action):

    def name(self):
        return "action_landtype"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        typeLandVariable = tracker.get_slot("landtype")
        typeLandArray= [] 
        myconn = mysql.connector.connect(host = "localhost", user = "root", 
            passwd = "",database="data_trees")
        curTree =myconn.cursor()
        codeOfLand = "SELECT * FROM landtype WHERE Landtype LIKE '{}'".format(typeLandVariable)
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
        dispatcher.utter_message("Các cây trồng  "+ typeLandVariable + " là:")
        for x in treeReturn:
            dispatcher.utter_message(x)  
        return []
# #--------------------------------------------------------------------------------------------------------------
# #--------------------------------------------------------------------------------------------------------------
# #--------------------------------------------------------------------------------------------------------------
# #--------------------------------------------------------------------------------------------------------------
class action_light(Action):

    def name(self):
        return "action_light"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        lightVariable = tracker.get_slot("light")
        lightArray= [] 
        myconn = mysql.connector.connect(host = "localhost", user = "root", 
            passwd = "",database="data_trees")
        curTree =myconn.cursor()
        codeOfLight = "SELECT * FROM light WHERE Light LIKE '{}'".format(lightVariable)
        curTree.execute(codeOfLight)
        result = curTree.fetchall()
        for x in result:
            lightArray.append(x[0])
        myconn.rollback()
        myconn.close()
        # Code của loại đất
        codeOfVariable = lightArray[0]
        
        treeReturn = []
        myconn = mysql.connector.connect(host = "localhost", user = "root", 
                    passwd = "",database="data_trees")
        curTree =myconn.cursor()
        treeOfLight = "SELECT * FROM db_trees WHERE Light LIKE '%{}%'".format(codeOfVariable)
        curTree.execute(treeOfLight)  
        result = curTree.fetchall()
        for x in result:
            treeReturn.append(x[1])
        myconn.rollback()
        myconn.close()
        dispatcher.utter_message("Các cây trồng dưới điều kiện "+ lightVariable + " là:")
        for x in treeReturn:
            dispatcher.utter_message(x)  
        return []
# #--------------------------------------------------------------------------------------------------------------
# #--------------------------------------------------------------------------------------------------------------
# #--------------------------------------------------------------------------------------------------------------
class action_species(Action):

    def name(self):
        return "action_species"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        speciesVariable = tracker.get_slot("species")
        speciesArray= [] 
        myconn = mysql.connector.connect(host = "localhost", user = "root", 
            passwd = "",database="data_trees")
        curTree =myconn.cursor()
        codeOfSpecies = "SELECT * FROM species WHERE Species LIKE '{}'".format(speciesVariable)
        curTree.execute(codeOfSpecies)
        result = curTree.fetchall()
        for x in result:
            speciesArray.append(x[0])
        myconn.rollback()
        myconn.close()
        # Code của loại đất
        codeOfVariable = speciesArray[0]
        
        treeReturn = []
        myconn = mysql.connector.connect(host = "localhost", user = "root", 
                    passwd = "",database="data_trees")
        curTree =myconn.cursor()
        treeOfSpecies = "SELECT * FROM db_trees WHERE Species LIKE '%{}%'".format(codeOfVariable)
        curTree.execute(treeOfSpecies)  
        result = curTree.fetchall()
        for x in result:
            treeReturn.append(x[1])
        myconn.rollback()
        myconn.close()
        dispatcher.utter_message("Các cây trồng thuộc loại "+ speciesVariable + " là:")
        for x in treeReturn:
            dispatcher.utter_message(x)  
        return []
# #--------------------------------------------------------------------------------------------------------------
# #--------------------------------------------------------------------------------------------------------------
class action_condition(Action):

    def name(self):
        return "action_condition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:                        
        area = []
        benefit = []
        climate = []
        growthtime = []
        humidity = []
        landtype = []
        light = []
        species = []
        myconn = mysql.connector.connect(host = "localhost", user = "root", 
                            passwd = "",database="data_trees")
        curTree =myconn.cursor()
        commandGiveData = "SELECT Area FROM area"
        curTree.execute(commandGiveData)  
        result = curTree.fetchall()
        for x in result:
            area.append(x[0].lower())
        
        #
        myconn = mysql.connector.connect(host = "localhost", user = "root", 
                            passwd = "",database="data_trees")
        curTree =myconn.cursor()
        commandGiveData = "SELECT Benefit FROM benefit"
        curTree.execute(commandGiveData)  
        result = curTree.fetchall()
        for x in result:
            benefit.append(x[0].lower())        
        
        #
        myconn = mysql.connector.connect(host = "localhost", user = "root", 
                            passwd = "",database="data_trees")
        curTree =myconn.cursor()
        commandGiveData = "SELECT Climate FROM climate"
        curTree.execute(commandGiveData)  
        result = curTree.fetchall()
        for x in result:
            climate.append(x[0].lower())        
        
        #
        myconn = mysql.connector.connect(host = "localhost", user = "root", 
                            passwd = "",database="data_trees")
        curTree =myconn.cursor()
        commandGiveData = "SELECT Growthtime FROM growthtime"
        curTree.execute(commandGiveData)  
        result = curTree.fetchall()
        for x in result:
            growthtime.append(x[0].lower())        
        
        #
        myconn = mysql.connector.connect(host = "localhost", user = "root", 
                            passwd = "",database="data_trees")
        curTree =myconn.cursor()
        commandGiveData = "SELECT Humidity FROM humidity"
        curTree.execute(commandGiveData)  
        result = curTree.fetchall()
        for x in result:
            humidity.append(x[0].lower())        
        
        #
        myconn = mysql.connector.connect(host = "localhost", user = "root", 
                            passwd = "",database="data_trees")
        curTree =myconn.cursor()
        commandGiveData = "SELECT Landtype FROM landtype"
        curTree.execute(commandGiveData)  
        result = curTree.fetchall()
        for x in result:
            landtype.append(x[0].lower())        
        

        #
        myconn = mysql.connector.connect(host = "localhost", user = "root", 
                            passwd = "",database="data_trees")
        curTree =myconn.cursor()
        commandGiveData = "SELECT Light FROM light"
        curTree.execute(commandGiveData)  
        result = curTree.fetchall()
        for x in result:
            light.append(x[0].lower())        
        
        #
        myconn = mysql.connector.connect(host = "localhost", user = "root", 
                            passwd = "",database="data_trees")
        curTree =myconn.cursor()
        commandGiveData = "SELECT Species FROM species"
        curTree.execute(commandGiveData)  
        result = curTree.fetchall()
        for x in result:
            species.append(x[0].lower())    
        #
        lenArea = len(area)
        lenBenefit= len(benefit)
        lenClimate = len(climate)      
        lenGrowthtime = len(growthtime)
        lenHumidity = len(humidity)
        lenLandtype = len(landtype)
        lenLight = len(light)
        lenSpecies= len(species)
        lenArray = [lenArea, lenBenefit, lenClimate, lenGrowthtime, lenHumidity, lenLandtype, lenLight, lenSpecies]
        lenArray.sort(reverse=True)
        lenUse = lenArray[0]+5

    # Condition from data of chatbot with user
        # Command Support--------------------------------------------------------------------------      
        def commandSupport(x):
            support = ''
            for i in range(0,lenUse):
                try:
                    if(x == humidity[i]):                          
                        support = 'Humidity'
                        break                        
                    else:
                        if(x == benefit[i]):                                  
                            support = 'Benefit'
                            break
                        else:
                            if(x == climate[i]):                                       
                                support = 'Climate'
                                break
                            else:
                                if(x == growthtime[i]):
                                    support = 'Growthtime'
                                    break
                                else:
                                    if ( x == light[i]):
                                        support = 'Light'
                                        break
                                    else:
                                        if(x == area[i]):        
                                            support = 'Area'
                                            break           
                except: 
                    break
            return support
        # name Table on Database-------------------------------------------------------------------------
        def commandNameTableOfCondition(x):
            nameTable = ''
            for i in range(0,lenUse):
                try:
                    if ( x == species[i]): 
                        nameTable = 'species'
                        break
                    else:
                        if(x ==landtype[i]):         
                            nameTable = 'landtype'
                            break
                        else:
                            nameTable = commandSupport(x).lower()  
                except: 
                    break
            return nameTable    
        #Name Column on Table Database-------------------------------------------------------------------
        def commandNameColumnOfCondition(x):
            nameColumn =''
            for i in range(0,lenUse):
                try:
                    if (x == species[i]):
                            nameColumn = 'Species'
                            break
                    else:
                        if(x ==landtype[i]):
                            nameColumn = 'Landtype'
                            # nameColumn = landtype[i]
                            break                      
                        else:
                            nameColumn = commandSupport(x)            
                except:          
                    break
            return nameColumn
        # -----------------------------------------------------------------------------------------------------------       
        conditionFirstVariable = tracker.get_slot("conditionfirst").lower()
        conditionSecondVariable = tracker.get_slot("conditionsecond").lower()
        nameTableOfConditionFirst = commandNameTableOfCondition(conditionFirstVariable)
        nameTableOfConditionSecond = commandNameTableOfCondition(conditionSecondVariable)
        nameColumnOfConditionFirst = commandNameColumnOfCondition(conditionFirstVariable)
        nameColumnOfConditionSecond = commandNameColumnOfCondition(conditionSecondVariable)
        # codeOfTypeCondition = "SELECT * FROM {} WHERE {} LIKE '{}'".format(nameTableOfConditionFirst,nameColumnOfConditionFirst,conditionFirstVariable)
        # print(codeOfTypeCondition)
        # codeOfTypeCondition2 = "SELECT * FROM {} WHERE {} LIKE '{}'".format(nameTableOfConditionSecond,nameColumnOfConditionSecond,conditionSecondVariable)
        # print(codeOfTypeCondition2)
        #---------------------------------------------------------------------------
        arrTreeFirstReturn = []
        def listTreesOfConditionFirst(table,column,value):
            conditionArray= []
            myconn = mysql.connector.connect(host = "localhost", user = "root", 
                passwd = "",database="data_trees")
            curTree =myconn.cursor()
            codeOfTypeCondition = "SELECT * FROM {} WHERE {} LIKE '{}'".format(table,column,value)
            curTree.execute(codeOfTypeCondition)
            result = curTree.fetchall()
            for x in result:
                conditionArray.append(x[0])
            myconn.rollback()
            myconn.close()
            codeOfVariable = conditionArray[0]
            treeReturn = []
            myconn = mysql.connector.connect(host = "localhost", user = "root", 
                        passwd = "",database="data_trees")
            curTree =myconn.cursor()
            treeOfSpecies = "SELECT * FROM db_trees WHERE {} LIKE '%{}%'".format(column,codeOfVariable)
            curTree.execute(treeOfSpecies)  
            result = curTree.fetchall()
            for x in result:
                treeReturn.append(x[1])
            myconn.rollback()
            myconn.close()
            for x in treeReturn:
                arrTreeFirstReturn.append(x)
        #--------------------------------------------------------------------------
        arrTreeSecondReturn = []
        def listTreesOfConditionSecond(table,column,value):
            conditionArray= []
            myconn = mysql.connector.connect(host = "localhost", user = "root", 
                passwd = "",database="data_trees")
            curTree =myconn.cursor()
        
            codeOfTypeCondition = "SELECT * FROM {} WHERE {} LIKE '{}'".format(table,column,value)
            curTree.execute(codeOfTypeCondition)
            result = curTree.fetchall()
            for x in result:
                conditionArray.append(x[0])
            myconn.rollback()
            myconn.close()
            codeOfVariable = conditionArray[0]
            treeReturn = []
            myconn = mysql.connector.connect(host = "localhost", user = "root", 
                        passwd = "",database="data_trees")
            curTree =myconn.cursor()
            treeOfSpecies = "SELECT * FROM db_trees WHERE {} LIKE '%{}%'".format(column,codeOfVariable)
            curTree.execute(treeOfSpecies)  
            result = curTree.fetchall()
            for x in result:
                treeReturn.append(x[1])
            myconn.rollback()
            myconn.close()
            for x in treeReturn:
                arrTreeSecondReturn.append(x)
        #--------------------------------------------------------------------------
        listTreesOfConditionFirst(nameTableOfConditionFirst, nameColumnOfConditionFirst, conditionFirstVariable)
        listTreesOfConditionSecond(nameTableOfConditionSecond, nameColumnOfConditionSecond,conditionSecondVariable)        
        lenOfarrTreeFirstReturn = len(arrTreeFirstReturn)
        lenOfarrTreeSecondReturn = len(arrTreeSecondReturn)
        value = False
        arrTrees = []
        for i in range(0,lenOfarrTreeFirstReturn):
            for j in range(0,lenOfarrTreeSecondReturn):
                try:
                    if(arrTreeFirstReturn[i] == arrTreeSecondReturn[j]):
                        # dispatcher.utter_message(arrTreeFirstReturn[i])
                        arrTrees.append(arrTreeFirstReturn[i])
                        value = True
                except:
                    break
        # Error hiển thị fix từ dòng này -> return []
        if(value == True):
            dispatcher.utter_message("Cây trồng phù hợp với điều kiện "+ conditionFirstVariable.lower() + " và " + conditionSecondVariable.lower() + " là:")
            for i in range(0,len(arrTrees)):
                dispatcher.utter_message(arrTrees[i])
        else: 
            dispatcher.utter_message("0 kết quả cho tìm kiếm này!")
        return []
                  
# #--------------------------------------------------------------------------------------------------------------
# #--------------------------------------------------------------------------------------------------------------
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
# #--------------------------------------------------------------------------------------------------------------
# #--------------------------------------------------------------------------------------------------------------