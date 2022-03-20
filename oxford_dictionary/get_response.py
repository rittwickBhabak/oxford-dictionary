import requests
from .get_key import CREDENTIALS, get_key

CREDENTIALS = get_key()
APP_ID = CREDENTIALS.get('app_id')
APP_KEY = CREDENTIALS.get('api_key')
language = "en-gb"

def meaning(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": APP_ID, "app_key": APP_KEY})
    return r 

if __name__=="__main__":
    print(meaning('example'))