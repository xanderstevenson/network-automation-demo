import requests
import json
# Suppress HTTPS warnings
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def restconf_config(username, password):

    # Print a stream of bytes as pretty JSON
    def printBytesAsJSON(bytes):
        print(json.dumps(json.loads(bytes), indent=2))
   
   
    restconf_base_url = 'https://ios-xe-mgmt.cisco.com:9443/restconf/data'
    headers ={
        "Content-Type": "application/yang-data+json",
        "Accept": "application/yang-data+json"
            }

    response = requests.get(url=f"{restconf_base_url}", headers = headers, auth=(username, password), verify= False)
    
    # response = requests.get(
    # url = 'https://ios-xe-mgmt.cisco.com',
    # auth = (username, password),
    # headers = {
    #     'Accept': 'application/yang-data+json'
    # },
    # verify = False)

    # Pretty print our JSON response
    print(response)

