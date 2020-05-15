from abc import ABC


class Band:
    band_list=[]
    def __init__(self,name="unknown",members=[]):
        self.name=name
        self.members=members
        Band.band_list.append(self)

    def play_solos(self):
        solosList=[]
        for i in range(len(Band.band_list)):
            for a in range(len(Band.band_list[i].members)):
                solosList.append(Band.band_list[i].members[a].play_solo())
        return solosList

    def __str__(self):
        return f'This is the band {self.name}'
    def __repr__(self):
        return f'Band instant. Name: {self.name}'

    @classmethod
    def to_list(cls):
        return cls.band_list

class Musician(ABC):
    def __init__(self,name,instrument,solo,role):
        self.name=name
        self.instrument=instrument
        self.solo=solo
        self.role=role

    def __str__(self):
        return f'Hi, I am {self.name}, a {self.role}'

    def __repr__(self):
        return f'{self.role} instant. Name: {self.name}'

    def get_instrument(self):
        return f"I play {self.instrument}"

    def play_solo(self):
        return f'The {self.role} is playing solo now, {self.solo} !'


class Guitarist(Musician):
    def __init__(self,name):
        super().__init__(name,'guitar','Dang Ding Dang','Guitarist')

class Bassist(Musician):
    def __init__(self,name):
        super().__init__(name,'bass guitar','Wong Dong Wong','Bassist')

class Drummer(Musician):
    def __init__(self,name):
        super().__init__(name,'drum set','Dong Si Da Si','Drummer')



if __name__ == "__main__":
    test = Drummer('Hill Billy')
    print(test.name)
    print(test.instrument)
    print(test.solo)
    print(test.role)
    print(test.__str__())
    print(test.__repr__())
    print(test.play_solo())
    print(test.get_instrument())

