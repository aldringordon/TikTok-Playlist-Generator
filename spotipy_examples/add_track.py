import sys

import spotipy
import spotipy.util as util


username='1299478497'
playlist_id = '6cBUJqXbOYrHfTMNCfVYx4'
track_ids = ['0hNduWmlWmEmuwEFcYvRu1',
'00bz5bGRGFMfACJWfhMSxx',
'0Jb3Kq7oDqRznHPIcrQpiX',
'1Z6u99PTG9w2t4mcIGoqqS',
'59ZfFk7ETa57vQY07XxliT']
scope = 'playlist-modify-private'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
    print(results)
else:
    print("Can't get token for", username)

print(track_ids)
