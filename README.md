# macos-siri-shortcuts
Python Web Server with scripts needed to execute certain actions on macOS

This application is intended to be ran on a seperate system to listen for incoming requests and then the seperate system will SSH into your macOS computer and execute the scripts.

Steps to run:
* Exchange SSH keys between macOS and server machine. (For example, I use a raspberry pi on my home network)
  * ssh-keygen -t RSA
  * ssh-copy-id *username*@*macos-machine-name.lan*
  
* Place the scripts folder in the root of your User folder in macOS
* Update the username and machine name to match your username and machine name in **server.py**
* Install server dependencies 
  * *pip3 install flask flask_cors*
* Start server 
  * *python3 server.py*
  
* Request the url as http://*your-server-address*/*option*
  * current options include:
      * */sleep **<--(turn off displays)***
      * */wake **<--(turn on displays)***
      * */mute **<--(turn off volume)***
      * */hide **<--(show screensaver)***
  * I generally set up a Siri shortcut to hit these endpoints
