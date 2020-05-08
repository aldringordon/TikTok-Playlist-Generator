# application prototype
# combine SongReader and PlayListCreator test code

from SongReader import SongReader
from PlayListCreator import PlayListCreator

video_path = '../test_data/test.mp4'

reader = SongReader(video_path)

songs = reader.get_song_information()

print('----------------------')
print('   song information:  ')
print('----------------------')
for song in songs:
    print(song)

print('\n\n')
print('----------------------')
print('creating playlist ...')
username = '1299478497'

plc = PlayListCreator(songs, username)
plc.generate()

print('done')
