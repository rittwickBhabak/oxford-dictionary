from playsound import playsound 

def play(track_url):
    playsound(track_url)
    print('Playing the sound.')


if __name__=="__main__":
    track_url = 'https://audio.oxforddictionaries.com/en/mp3/actual_gb_3.mp3'
    play(track_url)