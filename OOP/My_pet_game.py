import time
start_time = time.time()
n = 1
class My_pet(object):
    def __str__(self):
        print("\nСкука:", self.boredom, '\nГолод:', self.hunger)
        self.__pass_time()


    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        n1 =n
        pass_time = int(time.time() - start_time)
        if pass_time /(60*n1) >1:
            n1 += 1
            self.hunger += 1
            self.boredom += 1
        self.hunger += 1
        self.boredom += 1


    @property
    def mood(self):
        unhappieness = self.hunger + self.boredom
        if unhappieness < 10:
            m = "прекарсно"
        elif unhappieness <= 15:
            m = "неплохо"
        elif unhappieness <= 20:
            m = "не сказать что хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        print("Меня зовут", self.name, "и сейчас я чувствую себя", self.mood)
        self.__pass_time()

    def eat(self):
        food = int(input("сколько корма ты мне насыпешь?\n"))
        print("Мрр...спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self):
        fun = int(input("сколько ты будешь со мной играть?\n"))
        time_to_fun = fun
        while time_to_fun != 0:
            print("Уииии!")
            time.sleep(1)
            time_to_fun -= 1
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    pet_name = input("Как вы назовете своего питомца?\n")
    pet = My_pet(pet_name)
    choise = None
    while choise != "0":
        print(
            """
Игра моя зверюшка:
0 - Выйти
1 - Узнать об самочувствии зверюшки
2 - Покормить зверюшку
3 - Поиграть со зверюшкой""")
        choise = input("Ваш выбор :")
        print()
        if choise == "0":
            print("До свидания")
        elif choise == "1":
            pet.talk()
        elif choise == "2":
            pet.eat()
        elif choise == "3":
            pet.play()
        elif choise == "menu":
            pet.__str__()
        else:
            print("Извините в меню нет пункта", choise)

main()
input("\n\nНажмите Enter, что бы выйти.")
