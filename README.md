# ServerStatus-Checker
This is a simple script to check whether a server/service is running by trying to make a web request to the service and checking the status code response. When run, the program will send a web request to the server URL provided and then will create a message box tdisplaying the stauts of the service. 

## Setup
  To use this download the program and open the file in you preffered editor/IDE and enter the url for the server/service you wish to check th status of. Yo may alos chnag the messgaebox prompt if you wish, but do not remove the "{statusCode}" part. You can then run the program. You ay even hoose to set thi sprogram up with task scheduler so that you can be notified regurarly if a service is wokring. 

## Requirements
  The depenencies of this program are:
  - tkinter
  - requests
