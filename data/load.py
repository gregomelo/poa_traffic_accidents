import requests

# https://stackoverflow.com/questions/71892890/returning-all-data-from-a-ckan-api-request-python

BASE_URL = "http://dadosabertos.poa.br"
INITIAL_URL = "/api/3/action/datastore_search?resource_id=b56f8123-716a-4893-9348-23945f1ea1b9"
LIMIT = 10000

def get_data() -> list:
    result = []
    resp = requests.get(f"{BASE_URL}{INITIAL_URL}&limit={LIMIT}")
    js = resp.json()["result"]
    result.extend(js["records"])
    while "_links" in js and "next" in js["_links"]:
        resp = requests.get(BASE_URL + js["_links"]["next"])
        js = resp.json()["result"]
        result.extend(js["records"])
        # print(js["_links"]["next"]) # just so you know it's actually doing stuff
        if len(js["records"]) < LIMIT:
            # if it returned less records than the limit, the end has been reached
            break
    return result