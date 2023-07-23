# BITES_Chatbot
_Keyword-based chatbot with AIML core, random responses, conversation storage, web scraping, weather API integration._


# Table of Contents
  * [Demo](#demo)
  * [Summary](#summary)
  * [Architecture](#architecture)
  * [Setup](#setup)
  * [Authors](#authors)
  * [References](#references)
  * [Contribution](#contribution)

## Demo
![Application demo](media/demo.gif)
<img width="265" alt="image" src="https://github.com/RitulMohan/AIML_Chatbot/assets/79750424/a0296537-c634-493d-9860-bfecbdb1bf7e">

<img width="281" alt="Pasted Graphic 13" src="https://github.com/RitulMohan/AIML_Chatbot/assets/79750424/f829bc52-0cd3-40ce-90b6-ba7df1404529">



## Summary
This is a part of the *CS F407 Artificial Intelligence* Course at BITS Pilani Hyderabad Campus. In this assignment, a messenger bot  is created which can provide intelligent dialog conversations with the user, similar to  [ELIZA](https://en.wikipedia.org/wiki/ELIZA) or [ALICE](https://www.chatbots.org/chatbot/a.l.i.c.e/).

### Features
- AIML is used for the core of the chatbot.
- The messenger bot uses a knowledge base with multiple random responses exchanged between the user and the bot. 
- The bot is able to give replies to multiple interactions and stores the conversations in a  database. These persistent copies of the interactions can be retrieved the next time user chats with the  bot.
- The bot interacts with web services and recommends students healthy food options by web scraping.
- The bot can tell the current weather by interacting with a web API.
- **the whole project is based on keyword matching and intent recognition.**



## Architecture
Artificial Intelligence Markup Language (AIML) is used for creating the core of the chatbot. The frontend is developed using Android and backend using Python. 
The back end is in Python and front end is created using Android.
The app has been tested locally on Android Studio and not on an Android Phone.

The database information is stored in MySQL database on a  local machine. For viewing and updating databases, contains the appropriate code.



A database named *user_chats* should be created in the *mysql* system first.
2 tables named *chats* and *faculty* are used for persistent storage.

The *chats* table stores the timestamp,userid, bot query and bot response in that order.
Basic commands required to create/navigate through the db have been provided in a seperate file "mysql.txt"

## Setup

Before starting ensure that you have *mysql* on your machine.
- Create a database named *user_chats*
- Create table namely *chats* 
- Change the username and the password in the python files *app* & *conversation*


	
Make sure to install the dependecies 
```bash
pip install AIML
pip install beautifulsoup4
pip install urllib2
```
make sure to update the python time library, there is a common issue while using with the AIML library
FIX Available here: [https://stackoverflow.com/questions/58569361/attributeerror-module-time-has-no-attribute-clock-in-python-3-8](url)


The backend server has to be run first on port 8000.

The backend server can be run simply via 
```bash
$ python app.py 
```
(*Python v3.9 was used for development*)
<img width="863" alt="Pasted Graphic 1" src="https://github.com/RitulMohan/AIML_Chatbot/assets/79750424/d61681c4-4e43-4578-b351-7bec9b4babc5">


The front end Android part can be run in *Android Studio*.
- Set up *Android Studio*,and install an emulator for testing/running the app.
- Open the *MyApplication* folder in Android Studio.
- Press the Play button to run the app.
- update gradle configuration to update build 
- This code was run on a virtual **Pixel 3A** device.


