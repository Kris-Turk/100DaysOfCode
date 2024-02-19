import os
from datetime import datetime
import json
import requests


HALO_SECRET = '39210af4-ce2d-401b-acd3-0bcf0266f4c4-9d41d307-6ffd-4dd6-91f3-d0c5347f4d44'
HALO_CLIENT_ID = 'a9814a1b-1ca7-4fe3-b611-42289181e2e6'
HALO_AUTH_URL = 'https://hybrituat.halopsa.com/auth/token'
HALO_RESOURCE_URL = 'https://hybrituat.halopsa.com/api'
HALO_TENANT = 'hybrituat'


CREATE_TICKET_URL = HALO_RESOURCE_URL + '/Tickets'
CLIENTS_URL = HALO_RESOURCE_URL + '/Client'


auth_body = { 
           'grant_type': 'client_credentials',
           'client_id': HALO_CLIENT_ID,
           'client_secret': HALO_SECRET,
           'scope': 'all'
}

access_token = requests.post(HALO_AUTH_URL, data=auth_body, timeout=10).json().get('access_token')




headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + access_token
}


def get_client_id(client_name):
    """Returns the client id for a given client name"""
    client = requests.get(CLIENTS_URL + f'?search={client_name}', headers=headers, timeout=10).json()
    return client.get('clients')[0].get('id')

ticket_payload = {   
    "dateoccured": datetime.now().isoformat(),
    "summary": "This is a ticket summary 2", # Needs customizing
    "details": "This is the ticket details 2", # Needs Customizing
    "client_id": get_client_id('HybrIT Services UK'), # Needs Paramatizing
    "client_name": "HybrIT Services UK", # Needs Paramatizing
    "team": "Service Desk", # Needs Paramatizing
    "impact": "3",
    "urgency": "3"
}

json_payload = json.dumps([
    ticket_payload
    ])


response = requests.post(CREATE_TICKET_URL, headers=headers, data=json_payload)