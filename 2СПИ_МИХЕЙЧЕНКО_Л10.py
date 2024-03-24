class stone:
    def __init__(self, quantity=0):
        self.quantity = quantity

class rope:
    def __init__(self, quantity=0):
        self.quantity = quantity

class stick:
    def __init__(self, quantity=0):
        self.quantity = quantity

class cloth:
    def __init__(self, quantity=0):
        self.quantity = quantity

class Axe:
    def __init__(self, stone=0, rope=0, stick=0, cloth=0, craft=0):
        self.stone = stone
        self.rope = rope
        self.stick = stick
        self.cloth = cloth
        self.craft = craft
        if self.stone == self.rope == self.stick == self.cloth == 1 and self.craft == 4:
            print('топор создан')
        else:
            print('Недостаточно ресурсов')
axe = Axe()