class Character:
    # def __init__(self, name):
    #     self.name = name

    def move(self, direction, distance):

        directions_list = {"north": "на север", "south": "на юг", "west": "на запад", "east": "на восток"}
        if direction not in directions_list.keys():
            print(self.name, "движется непонятно куда")
        else:
            print(self.name, "движется", distance, "метров", directions_list[direction])


class Hero(Character):

    def __init__(self, name):
        self.name = name


class Enemy(Character):

    def __init__(self, name):
        self.name = name


pythomir = Hero("Питомир")
bugoonya = Enemy("Багуня")

pythomir.move("north", 50)
pythomir.move("west", 10)
pythomir.move("climb", 0)

bugoonya.move("north", 50)
bugoonya.move("west", 10)
pythomir.move("climb", 0)

# Не удаляйте код ниже, это проверка!

if not 'Character' in dir():
    print("Общий класс родитель Character не создан")

if not hasattr(Character, "move"):
    print("У общего класса отсутствует метод move")
