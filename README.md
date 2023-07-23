
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


## Summary
This is a part of the *CS F407 Artificial Intelligence* Course at BITS Pilani Hyderabad Campus. In this assignment, a messenger bot  is created which can provide intelligent dialog conversations with the user, similar to  [ELIZA](https://en.wikipedia.org/wiki/ELIZA) or [ALICE](https://www.chatbots.org/chatbot/a.l.i.c.e/).

### Features
- AIML is used for the core of the chatbot.
- The messenger bot uses a knowledge base with multiple random responses exchanged between the user and the bot. 
- The bot is able to give replies to multiple interactions and stores the conversations in a  database. These persistent copies of the interactions can be retrieved the next time user chats with the  bot.
- The bot interacts with web services and helps the user decide the course to be taken based on the recent trends in the industry or the recent trending jobs.
-  The bot  recommends a subject based on domain of interest or based on the professor in whose class he/she is interested in. 
- The bot can tell the current weather by interacting with a web API.
- **No machine learning is used and the whole project is based on keyword matching and intent recognition.**



## Architecture
A corpus of professors and courses is stored in the MySQL database. Artificial Intelligence Markup Language (AIML) is used for creating the core of the chatbot. The frontend is developed using Android and backend using Python. 
The back end is in Python and front end is created using Android.
The app has been tested locally on Android emulator(in Android Studio) and not on an Android Phone.

The database information is stored in MySQL database on a  local machine. For viewing and updating databases, *mySQL.txt* contains the appropriate code.

![Database tables](media/tables.png)

A database named *user_chats* should be created in the *mysql* system first.2 tables named *chats* and *faculty* are used for persistent storage.

The *chats* table stores the timestamp,userid, bot query and bot response in that order.
![Database format](media/database.png)

The *faculty* table stores the name of the faculty along with the courses taught.

## Setup

Before starting ensure that you have *mysql* on your machine.
- Create a database named *user_chats*
- Create two tables namely *chats* & *faculty*
- Change the username and the password in the python files *app* & *conversation*

You can refer *[mySQL.txt](https://github.com/smit-1999/AIML_Bot/blob/master/mySQL.txt)* for basic SQL commands.
	

The backend server has to be run first,on port 8000.

The backend server can be run simply via 
```bash
$ python app.py 
```
(*Python v2.7 was used at the time of development*)



The [*MyApplication*](https://github.com/smit-1999/AIML_Bot/tree/master/MyApplication) folder contains the frontend code files.

The front end Android part can be run in *Android Studio*.
- Set up *Android Studio*,and install an emulator for testing/running the app.
- Open the *MyApplication* folder in Android Studio.
- Press the Play button to run the app. 
- This code was run on **Nexus S API 28** device at the time of development.

## Authors

 - [**Smit Shah**](https://github.com/smit-1999/)

## References

 - [For Android front end
   ](https://medium.com/@harivigneshjayapalan/android-baking-a-simple-chatbot-in-30-minutes-aiml-ff43c3269025)

## Contribution
[Contribution guidelines for this project](docs/CONTRIBUTING.md)
