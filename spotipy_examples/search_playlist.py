import spotipy
import spotipy.util as util
import pprint

username = '1299478497'
scope = 'playlist-modify-private'

search_str = 'spotipy_test'

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    result = sp.search(search_str,type='playlist')

    try:
        uri = result['playlists']['items'][0]['uri']
        print('spotipy_test uri = ', uri.replace('spotify:playlist:',''))
    except Exception:
        print('no playlist found')


