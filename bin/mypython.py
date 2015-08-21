import json

import requests

def getApiJson(path):
    result = requests.get("http://api-internal.linqia.com{}".format(path))
    return result.json()

