#1
class box():
    def __init__(self, save_cap):
        self.__open = True
        self.__save = save_cap
        self.__close = False
        self.__save_drop = []

    def open(self):
        self.__open = False
        print('сундук закрыт')

    def close(self):
        self.__close = True
        print('сундук открыт')

    def open_drop(self):
        print('save_drop', self.__save_drop)

    def save_drop(self, saved_drop):
        if len(self.__save_drop) < self.__save:
            self.__save_drop.append(saved_drop)
            print(f"лут {saved_drop}")
        else:
            print("нет места")

    def looc_save(self):
        if self.__save_drop:
            print("есть", end="")
            for saved_drop in self.__save_drop:
                print(saved_drop, end=",")
            print()
        else:
            print("пусто")


i_box = box(3)
i_box.save_drop("лут 1")
i_box.save_drop("лут 2")
i_box.save_drop("лут 3")
i_box.save_drop("лут 4")
i_box.save_drop("лут ")  # нет места
i_box.looc_save()

#2
class Knop:
    def __init__(self, color,x,y,active=True,passive=False,):
        self.color=color
        self.active=active
        self.passive=passive
        self.x=x
        self.y=y
    def stat(self):
        print(f'Цвет{self.color}'
              f'по x {self.x}'
              f'по y {self.y}')
    def mode_yes(self):
        self.active=True
        self.passive=False
        print('Активна')
    def mode_not(self):
        self.active=False
        self.passive=True
        print('Не активна')

knop=Knop(' orange ',250,250)
knop.mode_yes()
knop.mode_not()
knop.stat()
#3
print('Привет это твой питомец Игроль, давай узнаем что он может')
class Igor:
    def __init__(self,hp=100,food=1000, stamina=100, to_eat=False,sleep=False,play=False,Waiting=True):
        self.hp=hp
        self.food=food
        self.stamina=stamina
        self.to_eat=to_eat
        self.sleep=sleep
        self.play=play
        self.Waiting=Waiting
    def info_stat(self):
        print(f' Радость {self.hp}'
              f' Сытость {self.food}'
              f' усталость {self.stamina}')
    def to_eat_play(self):
        self.to_eat=True
        self.to_eat=False
        print('Пора подкрепиться ')
    def sleeping(self):
        self.sleep=True
        self.sleep=False
        print('Пора спать')
    def play_GAME(self):
        self.play=True
        self.play=False
        print('Пора играть')
    def Waiting_IGOR(self):
        self.Waiting=True
        self.Waiting=False
        print('Оставить Игоря')
igor=Igor()
igor.to_eat_play()
igor.sleeping()
igor.play_GAME()
igor.Waiting_IGOR()
igor.info_stat()