# create playlist using spotify python api Spotipy

import spotipy
import spotipy.util as util

# probably use for debugging, delete later
import pprint

class PlayListCreator:
    
    def __init__(self, songs, username):
        self._songs = songs
        self._username = username
        self._scope = 'playlist-modify-private'
        self._search_str = 'spotipy_test'
        self._playlist_uri = ''
        self._token = False
        self._sp = None
        self._song_uris = set()

    def generate(self):
        self._token = util.prompt_for_user_token(self._username, self._scope)

        self._get_playlist_uri()
        print('playlist uri: %s' % self._playlist_uri)
        
        self._add_songs()
        print('song uris:')
        for song in self._song_uris:
            print(song)
        self._add_to_playlist()

    # gets the URI for the users playlist to add the tracks to
    def _get_playlist_uri(self):
        if self._token:
            self._sp = spotipy.Spotify(auth=self._token)
            self._sp.trace = False
            result = self._sp.search(self._search_str, type='playlist')

            # assumes that there is only 1 playlist in the users library
            # called 'spotipy_test', if there are more than one it takes
            # the newest one as per the ['items'][0]

            # checks that the playlist already exists,
            # if it doesn't create one
            try:
                uri = result['playlists']['items'][0]['uri']
            except Exception:
                playlist_name = 'spotipy_test'
                playlist_description = 'generated spotipy playlist'
                playlist = self._sp.user_playlist_create(self._username, playlist_name, public=False, description=playlist_description)
                uri = playlist['uri']
            formatted = uri.replace('spotify:playlist:','')
            self._playlist_uri = formatted
        else:
            print("token not set or invalid, try again")

    # adds the songs in songs[(name, artist), ..., ] to the playlist
    # found in _get_playlist_uri()
    def _add_songs(self):
        for name, artist in self._songs:
            result = self._sp.search(name + " - " + artist,type='track')
            try:
                uri = result['tracks']['items'][0]['uri']
                self._song_uris.add(uri.replace('spotify:track:',''))
            except Exception:
                pass

    # add the songs to the playlist using the uris form _add_songs()
    def _add_to_playlist(self):
        self._sp.user_playlist_add_tracks(self._username, self._playlist_uri, list(self._song_uris))

