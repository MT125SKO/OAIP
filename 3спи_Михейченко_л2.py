class Projector:
    def __init__(self):
        self.work = False

    def on_Projector(self):
        self.work = True
        print("ПРОЕКТОР ВКЛ")

    def off_Projector(self):
        self.work = False
        print("ПРОЕКТОР ВЫК")


class Sound:
    def __init__(self):
        self.work = False

    def Sound_on(self):
        self.work = True
        print("ЗВУК ВКЛ")

    def Sound_off(self):
        self.work = False
        print("ЗВУК ВЫК")


class DvDPlayer:
    def __init__(self):
        self.work = False

    def DvD_on(self):
        self.work = True
        print("DVD ВКЛ")

    def DvD_off(self):
        self.work = False
        print("DVD ВЫК")

    def play(self, movie):
        print(f"фильм идёт {movie}")


class User:
    def __init__(self):
        self.projector = Projector()
        self.soundSystem = Sound()
        self.dvd_player = DvDPlayer()

    def go_movie(self, movie):
        print("Подготовка")
        self.projector.on_Projector()
        self.soundSystem.Sound_on()
        self.dvd_player.DvD_on()
        self.dvd_player.play(movie)


if __name__ == "__main__":
    user = User()
    user.go_movie("Призрак_Замка_Часть_3  6+")