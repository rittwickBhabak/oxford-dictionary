from sound.play import play

def hear_pronounciation(senses):
    track_urls = set()
    for sense in senses:
        track_url = sense.get('track_url')
        if track_url:
            track_urls.add(track_url)
    next_step = input('Hear the pronunciation 1\nEnter next word 2\n')
    try:
        next_step = int(next_step)
    except:
        pass 
    if next_step==1:
        track_urls = list(track_urls)
        if len(track_urls)>1:
            print(f"{len(track_urls)} pronunciations found.")
            track_no = input('Enter track number to play: ')
            try:
                track_no = int(track_no)
            except:
                pass 
            if 0<track_no and track_no<=len(track_urls):
                play(track_urls[track_no-1])
            else:
                print('Wrong pronunciation number given.')
        elif len(track_urls) == 1:
            play(track_urls[0])
        else:
            print('No track found')