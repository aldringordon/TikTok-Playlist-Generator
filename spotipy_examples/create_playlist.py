import spotipy
import spotipy.util as util
import pprint

username = '1299478497'
scope = 'playlist-modify-private'

playlist_name = 'spotipy_test'
playlist_description = 'test for spotipy.user_playlist_create()'

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    playlists = sp.user_playlist_create(username, playlist_name, public=False, description=playlist_description)
    pprint.pprint(playlists)
else:
    print("cant get token for %s" % username)
