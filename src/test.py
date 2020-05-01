from SongReader import SongReader

video_path = "../test_data/test.mp4"

reader = SongReader(video_path)

songs = reader.get_song_information()

print("---------------------------")
for x,y in songs:
    print(x + " - " + y)

print("size: " + str(len(songs)))
