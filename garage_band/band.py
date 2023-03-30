class Band:
    members = []

    def __init__(self, name='unknown'):
        self.name = name
        Band.members.append(self)

    @staticmethod
    def play_solo(solo):
        print(solo)