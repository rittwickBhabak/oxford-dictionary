import requests
import json
app_id = "00f19cda"
app_key = "44d73014bcb6b77019d05b54fb0ef065"
language = "en-gb"

def meaning(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    return r 

if __name__=="__main__":
    print(meaning('example'))