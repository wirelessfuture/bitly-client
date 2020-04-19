import os
import time

import requests
from dotenv import load_dotenv
load_dotenv()

from db import insert

# Bitly Domain 
BITLY_DOMAIN = "https://api-ssl.bitly.com/v4/"

# The bitly token
BITLY_TOKEN = os.getenv("BITLY_TOKEN")

# Gets the current unix time based on local clock
def get_current_unix_timestamp():
    return time.time()

# Make a POST request - Returns a JSON object
def post_request(endpoint, payload):
    headers = {"Host": "api-ssl.bitly.com", "Content-Type": "application/json", "Authorization": "Bearer " + BITLY_TOKEN}
    url = os.path.join(BITLY_DOMAIN, endpoint)
    return requests.post(url, headers=headers, json=payload).json()

# Shortens a URL
def shorten(url):
    payload = {"domain": "bit.ly", "long_url": url}
    response = post_request("shorten", payload)
    data = {"url_before": response["long_url"], "url_after": response["link"], "unix_timestamp": get_current_unix_timestamp()}
    insert(data)
    return data

# Expands a URL
def expand(url):
    bitlink_id = os.path.join("bit.ly/", url.split("/")[-1])
    payload = {"bitlink_id": bitlink_id}
    response = post_request("expand", payload)
    data = {"url_before": response["link"], "url_after": response["long_url"], "unix_timestamp": get_current_unix_timestamp()}
    insert(data)
    return data
