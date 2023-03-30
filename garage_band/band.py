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
        return f'Guitarist("{self.name}")'

    @staticmethod
    def get_instrument(self):
        return 'guitar'

    @staticmethod
    def play_solo(self):
        return 'face melting guitar solo'


class Bassist(Musician):

    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def __repr__(self):
        return f'Bassist("{self.name}")'

    @staticmethod
    def get_instrument(self):
        return 'bass'

    @staticmethod
    def play_solo(self):
        return 'bom bom buh bom'


class Drummer(Musician):

    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def __repr__(self):
        return f'Bassist("{self.name}")'

    @staticmethod
    def get_instrument(self):
        return 'bass'

    @staticmethod
    def play_solo(self):
        return 'bom bom buh bom'


if __name__ == "__main__":
    # Guitarists
    joan = pass
    jimi = pass
    # Drummers
    sheila = pass
    ginger = pass
    # Bassists
    meshell = pass
    flea = pass
