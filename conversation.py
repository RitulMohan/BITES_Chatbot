import os
import aiml,random,requests,decimal
from autocorrect import spell
import mysql.connector
from flask import Flask, request, jsonify
from url import topFood

k = aiml.Kernel();

def learn():    
    k.learn("data/ai.aiml")
    k.learn("data/bot.aiml")

learn()

def findResponse(query):
    response = k.respond(query)
    print('bot response:' + response)
    if response[:85] == "http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a":
        city = response[85:]
        api = response[:85] + "&q=" + city
        json_data = requests.get(api).json()
        print('Weather for city', json_data['main']['temp'],type(json_data['main']['temp']))
        response="Obtained from OpenMapWeather API\nMain:" + json_data['weather'][0]['main'] + " \nDescription: " \
                 +json_data['weather'][0]['description'] + "\nTemperature:" + str((json_data['main']['temp'])-273) + "Celsius"
    elif response[:28] == "http://localhost:8000/profs/":
       print('User entered an outlet name,now finding...')
       response = "You can order food items offered by your favourite outlet :" + getOutlets(response)
    elif response == "call best food in url.py":
        foods = topFood()
        response = "Google's pick:"
        for food in foods:
            response+= food + ","
       
        return response
    elif response == "":
        responseMsgs = ["Sorry,I don't understand that!","I searched through dozens of articles,but to no avail.Sorry!"
                        "I am unable to answer this.Please inform the developers!"]
        response = random.choice(responseMsgs)
    return response

# def getOutlets(query):
#     a = query[28:]
#     val = (a,)
#     print('val:', val)
#     cnx = mysql.connector.connect(user='localhost', password='ritul1234',
#                                   host='root',
#                                   database='user_chats')
#     mycursor = cnx.cursor()

#     sql = "SELECT * FROM outlets WHERE name = %s"
#     mycursor.execute(sql, val)
#     myresult = mycursor.fetchall()
#     dic = {}
#     for x in myresult:
#         str_outlet = x[1].encode('ascii', 'ignore')
#         str_location = x[2].encode('ascii', 'ignore')
#         dic['outlet'] = str_outlet
#         dic['location'] = str_location

#     cnx.close()
#     return dic['location']
