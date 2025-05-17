import requests

def get_questions() :
    params= {
        "amount" : 10,
        "type" : "boolean"
        }

    response= requests.get(url="https://opentdb.com/api.php", params= params)
    response.raise_for_status()

    return response.json()['results']