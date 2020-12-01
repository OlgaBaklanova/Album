class Track():
    def __init__(self, name_track, duration_track):
        self.name_track = name_track
        self.duration_track = duration_track

    def show(self):
        print(f'{self.name_track} - {self.duration_track}')


ga_oye = Track('Open Your Eyes', 3)
ga_m = Track('Maria', 3)
ga_gb = Track('Get Busy', 3)
lp_f = Track('Faint', 3)
lp_n = Track('Numb', 3)
lp_bth = Track('Breaking the Habit', 3)

print(ga_gb.show())


class Album():
    def __init__(self, name_album, band):
        self.name_album = name_album
        self.band = band
        self.list_track = []


    def get_tracks(self):
        print(f'Треки группы {self.band} в альбоме: {self.list_track[0]}, {self.list_track[1]}, {self.list_track[2]}')

    def add_track(self, track):
        self.list_track.append(track)
        print(f'Трек {track} добавлен в альбом {self.list_track}')

    def get_duration(self):
        summ_duration_ga = 0
        summ_duration_lp = 0
        for duration_ga in dict_ga.values():
            summ_duration_ga += duration_ga
        print(f' Длительность альбома Proud Like a God - {summ_duration_ga}')
        for duration_lp in dict_lp.values():
            summ_duration_lp += duration_lp
        print(f' Длительность альбома Meteora - {summ_duration_lp}')

dict_ga = {ga_oye.duration_track: 3, ga_m.duration_track: 3, ga_gb.duration_track: 3}
dict_lp = {lp_f.duration_track: 3, lp_n.duration_track: 3, lp_bth.duration_track: 3}

guano_apes = Album('Proud Like a God', 'Guano Apes')
linkin_park = Album('Meteora', 'LINKIN PARK')

guano_apes.list_track.append('Open Your Eyes')
guano_apes.list_track.append('Maria')
guano_apes.list_track.append('Get Busy')

linkin_park.list_track.append('Faint')
linkin_park.list_track.append('Numb')
linkin_park.list_track.append('Breaking the Habit')

print(linkin_park.get_tracks())
print(linkin_park.add_track('In the End'))
print(guano_apes.get_duration())


