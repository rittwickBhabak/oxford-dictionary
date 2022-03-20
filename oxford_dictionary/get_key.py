import random 

CREDENTIALS = [
    {
        'app_id': '00f19cda',
        'api_key': '44d73014bcb6b77019d05b54fb0ef065',
        'email': 'oxforddictionaries.1@protonmail.com',
        'username': 'oxforddictionariesrittwick',
        'password': 'Testpass@1234',
    },
    {
        'app_id': '7a9702a4',
        'api_key': 'f65b551e5574b881bbdec5a2d107df5c',
        'email': 'oxforddictionary.2@protonmail.com',
        'username': 'oxforddictionary2',
        'password': 'Testpass@1234',
    }
]

def get_key():
    return random.choice(CREDENTIALS)