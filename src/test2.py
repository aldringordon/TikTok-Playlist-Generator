from SongReader2 import SongReader

video_path = "../test_data/test.mp4"

reader = SongReader(video_path)

reader.convert()

songs = reader.get_song_information()

print('------------------')
for song in songs:
    print("%s - %s" % (song))
