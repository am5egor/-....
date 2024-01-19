class Animal():
    def __init__(self, color, size, location, type_food, name):
        self.color = color
        self.size = size
        self.location = location
        self.type_food = type_food
        self.name = name
    
    def print_info(self):
        print('Животное:', self.name)
        print('Окрас:', self.color)
        print('Размер:', self.size)
        print('Место обитания:', self.location)
        print('Питается:', self.type_food)

    def eating(self):
        print(self.name, 'покушал(а)!')

    def sleeping(self):
        print(self.name, 'спит')

penguin = Animal('чёрный с белым пузом','средний', 'Антарктида', 'рыбой','Пингвин')

penguin.print_info()
penguin.eating()
penguin.sleeping()

bear = Animal('бурый','большой', 'леса', 'всеядные','Бурый медеведь')

bear.print_info()
bear.eating()
bear.sleeping()