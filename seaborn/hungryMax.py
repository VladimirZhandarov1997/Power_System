import time
import random


class Maksim():
    # атрибуты
    def __init__(self, a):
        self.hp = 10
        self.hungryNow = a
        self.hungryMax = 20
        self.actionMin = 1
        self.actionMax = 3

    def feed(self, food):
        if food == 1:
            self.hungryNow -= 1
        if food == 2:
            self.hungryNow -= self.actionMax
            self.hungryNow += 2
        if food == 3:
            self.hungryNow -= self.actionMin
            self.hungryNow += 3

        if self.hungryNow > self.hungryMax:
            self.hungryNow = self.hungryMax

    def hungry(self):
        self.hungryNow -= 1

    def born(self):
        n = random.randint(0, 100)
        if n <= self.hungryNow and self.hungryNow > 1:
            self.hungryNow = int(self.hungryNow / 2)
            return True
        else:
            return False


class Food():
    def __init__(self):
        self.food = [1, 1, 1, 1, 3, 3, 3, 3, 3, 2, 2, 2, 2]
        self.foodOne = 75
        self.foodTwo = 60
        self.foodThree = 40

    def generation(self):
        n = random.randint(0, 100)
        if n <= self.foodOne:
            self.food.append(1)
        if n <= self.foodTwo:
            self.food.append(2)
        if n <= self.foodThree:
            self.food.append(3)


food = Food()
MaksimArray = [Maksim(10)]
arr = []
j = 1000
for q in range(1000):

    for i in range(len(MaksimArray)):
        if i >= len(MaksimArray):
            break

        fl = MaksimArray[i].born()
        if fl:
            MaksimArray.append(Maksim(MaksimArray[i].hungryNow))
        if len(food.food) > 0:
            n = random.choice(food.food)
            MaksimArray[i].feed(n)
            food.food.remove(n)

        MaksimArray[i].hungry()
        if MaksimArray[i].hungryNow <= 0:
            MaksimArray.pop(i)

    food.generation()
    arr.append(len(MaksimArray))

    print('Наши Максы:', len(MaksimArray), 'Колл еды:', len(food.food))
    if len(MaksimArray) == 0:
        break
    time.sleep(0.1)

print(arr)
for w in range(1, 12):
    print(w, '-', arr.count(w))