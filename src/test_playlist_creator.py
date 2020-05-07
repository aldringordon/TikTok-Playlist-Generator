from PlayListCreator import PlayListCreator as PlayListCreator

username = '1299478497'

# sample output data from SongReader.py test
songs = [('You and Me', 'Shallou'),
        ('Desert Night', 'RUFUS DU SOL'),
        ('Elixir', 'Tourist'),
        ('Sunset Lover', 'Petite Biscuit'),
        ('Fibonacci', 'Nora En Pure')]

plc = PlayListCreator(songs, username)

plc.generate()
