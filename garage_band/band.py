class Band:
    members = []

    def __init__(self, name='unknown'):
        self.name = name
        Band.members.append(self)

    @staticmethod
    def play_solo(solo):
        print(solo)


class Musician:

    def __init__(self, name):
        self.name = name


class Guitarist(Musician):

    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'

    @staticmethod
    def get_instrument():
        return 'guitar'

    @staticmethod
    def play_solo():
        return 'face melting guitar solo'


class Bassist(Musician):

    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'

    @staticmethod
    def get_instrument():
        return 'bass'

    @staticmethod
    def play_solo():
        return 'bom bom buh bom'


class Drummer(Musician):

    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'

    @staticmethod
    def get_instrument():
        return 'drums'

    @staticmethod
    def play_solo():
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
