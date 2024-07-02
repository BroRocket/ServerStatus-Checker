#Import necessary libraries 
import requests
from tkinter import messagebox

#Set url for server
url = "" #Enter URL here

#Disbales the console warning about sending “Unverified HTTPS request”
requests.packages.urllib3.disable_warnings()
#Use try and except in case the request fails
try:
	#Makes a web request to the server and grabs status code
    statusCode = requests.head(url, verify=False).status_code
    #Creates message box on screen and displays the status code of the server
    messagebox.showinfo("Service Status", f'The status of the Service hosted at {url} is {statusCode}.')
      
except requests.ConnectionError:
    #Creates message box if request failed
    messagebox.showinfo("Service Status", f'The program was unable to connect to: {url}')
