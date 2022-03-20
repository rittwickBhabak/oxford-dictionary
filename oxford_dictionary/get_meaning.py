from .get_senses import get_senses
from .print_meaning import print_meaning 
from sound.play import play
import sys

if len(sys.argv)>1:
    word = sys.argv[1]
    try:
        senses = get_senses(word)
        print_meaning(word, senses)
        track_urls = set()
        for sense in senses:
            track_url = sense.get('track_url')
            if track_url:
                track_urls.add(track_url)
        next_step = input('Hear the pronunciation 1\nEnter next word 2\n')
        if next_step==1:
            if len(list(track_urls))>1:
                print(f"{len(list(track_urls))} pronunciations found.")
                for index, track in enumerate(list(track_urls)):
                    track_no = input('Enter track number to play: ')
                    if 0<=track_no and track_no<len(list(track_urls)):
                        play(track_urls[track_no])
                    else:
                        print('Wrong pronunciation number given.')
            elif len(list(track_urls)) == 1:
                play(track_urls[0])
            else:
                print('No track found')
                
    except Exception as e:
        print(f"ERROR: {str(e)}")
        input('Some error occoured. Press ENTER to EXIT.')
else:
    input('No words passed. Press ENTER to EXIT.')