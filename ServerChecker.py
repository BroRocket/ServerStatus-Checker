import requests
from tkinter import messagebox

url = "" #Enter server URL here

requests.packages.urllib3.disable_warnings()
try:
    statusCode = requests.head(url, verify=False).status_code
    messagebox.showinfo("Server Status", f'The status of the Server hosted at {url} is {statusCode}.')
      
except requests.ConnectionError:
    messagebox.showinfo("Server Status", f'The program was unable to connect to: {url}')
