# combine authorization.py and birdy_example.py

# shows a users playlists

import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

username = '1231091521'
scope = 'user-library-read'

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = sp.user_playlists(username)
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
