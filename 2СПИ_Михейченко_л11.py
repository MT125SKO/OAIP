#1
class Widget:
    def __init__(self, x_long, y_long):
        self.x_long=x_long
        self.y_long=y_long
    
    def window(self):
        print(f"Длина по x {self.x_long} высота по y {self.y_long}")

class Label(Widget):#маркер
    def __init__ (self, colour, text, x_long, y_long):
        super(). __init__(x_long, y_long)
        self.colour=colour
        self.text=text
    
    def window(self):
        print(f"Цвет {self.colour} Tекст {self.text}")
    
class LineEdit(Widget): # строка править
    def __init__(self, x_long, y_long):
        super().__init__(x_long, y_long)
    
    def window(self):
        super().window()
        print("Строка для текста ")

class TextEdit(Widget): #исправление текста
    def __init__(self, x_long, y_long):
        super().__init__(x_long, y_long)
    
    def window(self):
        super().window()
        print("Поле для исправления текста ")

class Button(Widget):
    def __init__(self,text, x_long, y_long):
        super().__init__(x_long, y_long)
        self.text=text
    
    def window(self):
        super().window()
        print(f"Текст кнопка {self.text}")

class CheckBox(Widget):
    def __init__(self,text, x_long, y_long):
        super().__init__(x_long, y_long)
        self.text=text
    def window(self):
        super().window()
        print(f"Переключатель {self.text}")

label=Label("Красный","Добро пожаловать",512,512)
lineEdit=LineEdit(512,120)
textEdi=TextEdit(512,240)
button=Button("Выход",500,450)
checkbox = CheckBox("Режима", 120, 20)
label.window()
print()
lineEdit.window()
print()
textEdi.window()
print()
button.window()
print()
checkbox.window()
print()
#2
class Weapon:
    def __init__(self, name, level, material):
        self.name=name
        self.level=level
        self.material=material
    
    def statistics_weapon(self):
        print(f"Вид холодное оружие Название {self.name} Уровень {self.level} материал {self.material} ")
    
    def statistics_firearms(self):
        print(f"Вид метательное Название {self.name} Уровень {self.level} материал {self.material} ")

class ColdWeapon (Weapon): # ХОЛОД
    def __init__(self, name, level, material):
        self.name=name
        self.level=level
        self.material=material

class Firearm (Weapon): # огь
    def __init__(self, name, level, material):
        self.name=name
        self.level=level
        self.material=material

class Dagger(ColdWeapon):
    def __init__ (self, name, level, material):
        super().__init__(name,level, material)

class Sword(ColdWeapon):
    def __init__ (self, name, level, material):
        super().__init__(name,level, material)

class Axe(ColdWeapon):
    def __init__ (self, name, level, material):
        super().__init__(name,level, material)

class Spear(Firearm): #коп
    def __init__ (self, name, level, material):
        super().__init__(name,level, material)

class Crossbow(Firearm): #дрот
    def __init__ (self, name, level, material):
        super().__init__(name,level, material)

class Stone(Firearm): 
    def __init__ (self, name, level, material):
        super().__init__(name,level, material)

dagger_1=Dagger("Кинжал", 1, "каменный")
dagger_2=Dagger("Кинжал", 2, "медный")
dagger_3=Dagger("Кинжал", 3, "железный")
sword_1=Sword("Меч", 1, "каменный")
sword_2=Sword("Меч", 2, "медный")
sword_3=Sword("Меч", 3, "железный")
axe_1=Axe("Топор", 1, "каменный")
axe_2=Axe("Топор", 2, "медный")
axe_3=Axe("Топор", 3, "железный")
spear_1=Spear("Копьё", 1, "каменный")
spear_2=Spear("Копьё", 2, "медный")
spear_3=Spear("Копьё", 3, "железный")
сrossbow_1=Crossbow("Дротик", 1, "каменный")
сrossbow_2=Crossbow("Дротик", 2, "медный")
сrossbow_3=Crossbow("Дротик", 3, "железный")
stone_1=Stone("Камень", 1, "каменный")

dagger_1.statistics_weapon()
dagger_2.statistics_weapon()
dagger_3.statistics_weapon()
sword_1.statistics_weapon()
sword_2.statistics_weapon()
sword_3.statistics_weapon()
axe_1.statistics_weapon()
axe_2.statistics_weapon()
axe_3.statistics_weapon()
spear_1.statistics_firearms()
spear_2.statistics_firearms()
spear_3.statistics_firearms()
сrossbow_1.statistics_firearms()
сrossbow_2.statistics_firearms()
сrossbow_3.statistics_firearms()
stone_1.statistics_firearms()

#3
class Game:
    def __init__(self, name, level, PacMan, perfume):
        self.name = name
        self.level = level
        self.PacMan = PacMan
        self.perfume = perfume

    def tutorial_game(self):
        print(f"Игра {self.name}. Пакман может идти в {self.PacMan.get_movement_status()} у вас враги {self.perfume.name}  уровень локации {self.level}")

class PacMan:
    def __init__(self, name, score_counter=0, left=False, right=False, down=False, up=False):
        self.name = name
        self.score_counter = score_counter
        self.left = left
        self.right = right
        self.down = down
        self.up = up

    def get_movement_status(self):
        return f"влево {self.left}, вправо {self.right}, вниз {self.down}, вверх {self.up}"

class Perfume:
    def __init__(self, name, colour, left=False, right=False, down=False, up=False):
        self.name = name
        self.colour = colour
        self.left = left
        self.right = right
        self.down = down
        self.up = up

    def get_movement_status(self):
        return f"влево {self.left}, вправо {self.right}, вниз {self.down}, вверх {self.up}"

class Level:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"уровень {self.number}"

class Effect:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class Fruits:
    def __init__(self, name, gives_number):
        self.name = name
        self.gives_number = gives_number

pac_man = PacMan("Пакман")
perfume_1 = Perfume("Дух", "Розовый")
perfume_2 = Perfume("Дух", "Оранжевый")
perfume_3 = Perfume("Дух", "Розовый")
perfume_4 = Perfume("Дух", "Бирюзовый")
level_1 = Level(1)
effect_1 = Effect("Супер", 1)
cherry_1 = Fruits("Вишня", 2)
cherry_2 = Fruits("Яблоко", 2)
cherry_3 = Fruits("Вишня", 3)
cherry_4 = Fruits("Апельсин", 5)

game = Game("Pac-Man", level_1, pac_man, perfume_1)

game.tutorial_game()

print(f"Уровень {level_1.number}")
print(f"{pac_man.name}  {pac_man.get_movement_status()}")
print(f"{perfume_1.name}  Цвет {perfume_1.colour}.{perfume_1.get_movement_status()}")
print(f"{perfume_2.name}  Цвет {perfume_2.colour}.{perfume_2.get_movement_status()}")
print(f"{perfume_3.name}  Цвет {perfume_3.colour}.{perfume_3.get_movement_status()}")
print(f"{perfume_4.name}  Цвет {perfume_4.colour}.{perfume_4.get_movement_status()}")
print(f"Level {level_1.number}")
print(f"Effect {effect_1.name}  Число {effect_1.number}")
print(f"Fruit {cherry_1.name} Даёт {cherry_1.gives_number} очка")
print(f"Fruit {cherry_2.name} Даёт {cherry_2.gives_number} очка")
print(f"Fruit {cherry_3.name} Даёт {cherry_3.gives_number} очка")
print(f"Fruit {cherry_4.name} Даёт {cherry_4.gives_number} очка")