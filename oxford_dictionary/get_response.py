import requests, os, json
from .get_key import CREDENTIALS, get_key

CREDENTIALS = get_key()
APP_ID = CREDENTIALS.get('app_id')
APP_KEY = CREDENTIALS.get('api_key')
language = "en-gb"

def write_output(word, response):
    if not os.path.exists('cache'): 
        os.mkdir('cache')
    with open(os.path.join('cache', f"{word}.json"), 'w', encoding='utf8') as f:
        f.write(json.dumps(response))

def new_request(word_id):
    print('Fteching from internet. Please wait...')
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": APP_ID, "app_key": APP_KEY})
    write_output(word_id, json.loads(r.text))
    return json.loads(r.text)

def meaning(word_id):
    if(os.path.exists(os.path.join('cache', f"{word_id}.json"))):
        try:
            with open(os.path.join('cache', f"{word_id}.json"), 'r', encoding='utf8') as f:
                return json.loads(f.read())
        except:
            os.remove(f"{word_id}.json")
            return new_request(word_id)
    else:
        return new_request(word_id)

if __name__=="__main__":
    print(meaning('example'))