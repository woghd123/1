class singer:
    singer_count = 0



    def __init__(self, name, Age, Debutday, Hitsong):
        self.name = name
        self.Age = Age
        self.Debutday = Debutday
        self.Hitsong = Hitsong
        singer.singer_count += 1

    def info(self):
        print(f'가수:{self.name}')
        print(f'나이:{self.Age}')
        print(f'데뷔일:{self.Debutday}')
        print(f'히트곡:{self.Hitsong}')
        print()

    def Song(self, Hitsong_num):
        print(self.Hitsong[Hitsong_num])

singer1 = singer('아이유', 29, 20080918, ['에잇', '밤편지', '팔레트'])
singer2 = singer('태연', 33, 20070805, ['만약에', '사계', 'Fine'])


singer1.info()
singer2.info()

singer1.Song(1)
singer2.Song(2)

