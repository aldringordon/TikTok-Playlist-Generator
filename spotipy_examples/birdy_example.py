# example code from spotipy docs

# assumes you set the SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET environment variables

# lists the names of all the ablums released by the artist 'Birdy'

import spotipy
from spotipy.oath2 import SpotifyClientCredentials

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(birdy_uri, album_type='album')

albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extends(results['items'])

for album in albums:
    print(album['name'])
