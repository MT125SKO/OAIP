class RockAndStone:
    def __init__(self, number=0):
        self.number = number

class Rope:
    def __init__(self, number=0):
        self.number = number

class Stick:
    def __init__(self, number=0):
        self.number = number

class Cloth:
    def __init__(self, number=0):
        self.number = number

class Axe:
    def __init__(self):
        self.stone = RockAndStone(int(input("Введите количество камней для создания ")))
        self.rope = Rope(int(input("Введите количество веревок для создания ")))
        self.stick = Stick(int(input("Введите количество палок для создания ")))
        self.cloth = Cloth(int(input("Введите количество ткани для создания ")))

        if self.stone.number > 0 and self.rope.number > 0 and self.stick.number > 0 and self.cloth.number > 0:
            self.craft = min(self.stone.number, self.rope.number, self.stick.number, self.cloth.number)
            if self.craft >= 1:
                self.stone.number -= 1 #присваивания как в ассембеле
                self.rope.number -= 1
                self.stick.number -= 1
                self.cloth.number -= 1
                self.craft -= 4
                print('Топор создан')

        print('Остаток ресурсов')
        print(f'камни {self.stone.number}') 
        print(f'веревки {self.rope.number}')
        print(f'палки {self.stick.number}')
        print(f'ткань {self.cloth.number}')

axe = Axe()
