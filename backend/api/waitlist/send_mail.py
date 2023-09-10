import requests
import json

url = "https://mailapi.dockhive.io/join_waitlist"
def send_email(email:str,name:str):    
    payload = json.dumps({
    "email": email,
    "name": name
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    
