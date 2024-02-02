import random


class Cat:
    def __init__(self, name="Cat"):
        self.name = name
        self.ves_in_gram = 4000
        self.gladness = 100
        self.live_now = True
        self.food = True
        self.want_eat = 1
        self.lotok = True
        self.want_kakati = 1

    def to_kakati(self):
        if self.lotok == True and self.want_kakati == 1:
            print("Ты сходил в лоток")
            self.want_kakati = 0
            self.lotok = False
            self.ves_in_gram -= 35
        elif self.lotok == False and self.want_kakati == 1:
            print("В лотке нету наполнителя")
            self.lotok = True
            self.gladness -= 20
        elif self.lotok == True and self.want_kakati == 0:
            print("Ты нехочешь идти в лоток")
            self.want_kakati = 1
        else:
            print("Ты нехочешь идти в лоток и в лотке нету наполнителя")
            lotok_or_want_kakati = (random.randint(1, 2))
            if lotok_or_want_kakati == 1:
                self.lotok = True
                lotok_or_want_kakati = (random.randint(1, 2))
            elif lotok_or_want_kakati == 2:
                self.want_kakati = 1
                lotok_or_want_kakati = (random.randint(1, 2))

    def to_eat(self):
        if self.food == True and self.want_eat == 1:
            print("Ты покушал")
            self.food = False
            self.want_eat = 0
            self.want_kakati += 0.5
            self.ves_in_gram += 50
            self.gladness += 10
        elif self.food == False and self.want_eat == 1:
            print("В кормушке нету еды")
            self.food = True
            self.gladness -= 20
        elif self.food == True and self.want_eat == 0:
            print("Ты нехочешь кушать")
            self.want_eat = 1
        else:
            print("Ты нехочешь кушать и в кормушке нету еды")
            food_or_want_eat = (random.randint(1, 2))
            if food_or_want_eat == 1:
                self.food = True
                food_or_want_eat = (random.randint(1, 2))
            elif food_or_want_eat == 2:
                self.want_eat = 1
                food_or_want_eat = (random.randint(1, 2))

    def to_sleep(self):
        self.want_sleep = 0
        if self.want_sleep == 1:
            print("Ты поспал")
            self.want_sleep = 0
            self.food = True
            self.want_eat = 1
            self.gladness += 5
        else:
            print("Ты ещё не хочешь спать")

    def play(self):
        self.toy = True
        self.want_play = 1
        if self.toy == True and self.want_play == 1:
            print("Ты поиграл")
            self.gladness += 10
            self.want_play = 0

    def is_alive(self):
        if self.ves_in_gram <= 3700:
            print("Ты умер от сильно маленького веса")
            self.live_now = False
        elif self.ves_in_gram >= 4500:
            print("Ты умер от переизбыточного веса")
            self.live_now = False
        elif self.gladness <= 0:
            print("Ты сильно грусный, поэтому ты ушол в депресняк")
            self.live_now = False
        elif self.gladness > 100:
            self.gladness = 90

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Ves = {self.ves_in_gram}")

    def live(self, day):
        d = f"Day {day} of {self.name} life"
        print(f"{d:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_kakati()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.play()
        elif live_cube == 4:
            self.to_eat()
        self.is_alive()
        self.end_of_day()


Busia = Cat("Busia")

for day in range(1, 366):
    if Busia.live_now == False:
        break
    Busia.live(day)
