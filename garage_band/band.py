class Band:

    def __init__(self, name, members):
        self.name = name
        self.members = members

    @staticmethod
    def play_solos(solo):
        print(solo)


class Musician:

    def __init__(self, name):
        self.name = name


class Guitarist(Musician):

    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'

    def get_instrument(self):
        return 'guitar'

    def play_solo(self):
        return 'face melting guitar solo'


class Bassist(Musician):


    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'

    def get_instrument(self):
        return 'bass'

    def play_solo(self):
        return 'bom bom buh bom'


class Drummer(Musician):

    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'

    def get_instrument(self):
        return 'drums'

    def play_solo(self):
        return 'bom bom buh bom'


if __name__ == "__main__":
    pass
    # # Guitarists
    # joan = Guitarist("Joan Jett")
    # jimi = Guitarist("Jimi Hendrix")
    # # Drummers
    # sheila = Drummer("Sheila E.")
    # ginger = Drummer("Ginger Baker")
    # # Bassists
    # meshell = Bassist("Meshell Ndegeocello")
    # flea = Bassist("Flea")
