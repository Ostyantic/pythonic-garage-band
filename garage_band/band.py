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
        print(f'Wassup! My name is {self.name}')

    def __repr__(self):
        print(f'Guitarist("{self.name}")')

    def get_instrument(self):
        print('Instrument: Guitar')

