import spotipy
import spotipy.util as util
import pprint

username = '1299478497'
scope = 'playlist-modify-private'

# sample output data from SongReader.py test
songs = [('You and Me', 'Shallou'),
        ('Desert Night', 'RUFUS DU SOL'),
        ('Elixir', 'Tourist'),
        ('Sunset Lover', 'Petite Biscuit'),
        ('Fibonacci', 'Nora En Pure')]

# do a search on each song
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    for name, artist in songs:
        result = sp.search(name + " - " + artist,type='track')
        info = result['tracks']['items'][0]
        print('-------------------')
        print("%s - %s" % (info['name'], info['artists'][0]['name']))
        print('song uri: %s' % info['uri'])
        print('preview link: %s' % info['external_urls'])
