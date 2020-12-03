class Track():
    def __init__(self, name_track, duration_track):
        self.name_track = name_track
        self.duration_track = duration_track

    def show(self):
        return f'{self.name_track} - {self.duration_track}'

    def get_name(self):
        return self.name_track

    def get_duration(self):
        return self.duration_track

class Album():
    def __init__(self, name_album, band):
        self.name_album = name_album
        self.band = band
        self.list_track = []


    def get_tracks(self):
        return [track.show() for track in self.list_track]


    def add_track(self, track):
        if not isinstance(track, Track):
            raise NotImplementedError('Can not add this object to track list')
        self.list_track.append(track)

    def get_duration(self):
        return sum([track.duration_track for track in self.list_track])


albums = []

album = Album('Proud Like a God', 'Guano Apes')
album.add_track(Track('Open Your Eyes', 3))
album.add_track(Track('Maria', 3))
album.add_track(Track('Get Busy', 3))

albums.append(album)

album = Album('Meteora', 'LINKIN PARK')
album.add_track(Track('Faint', 3))
album.add_track(Track('Numb', 3))
album.add_track(Track('Breaking the Habit', 3))

albums.append(album)

for album in albums:
    print(f'Альбом "{album.name_album}" группы {album.band}:')
    for track in enumerate(album.get_tracks(), 1):
        print(f'{track[0]}. {track[1]}')
    print(f'Общая длительность альбома: {album.get_duration()} минут\n')