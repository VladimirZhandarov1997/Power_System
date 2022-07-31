import time
import random
import seaborn as sns
import pandas as pd


class PowerStation():

    def __init__(self, amtStationMax, powerMin, powerMax):
        self.amtStationMax = amtStationMax # количество генераторов
        self.powerMin = powerMin # минимальная мощность генератора
        self.powerMax = powerMax # максимальная мощность генератора
        self.timeDay = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]


    def production(self, powerNowArray, timePowerOne, timePowerTwo): # берет 2 списка графика нагрузки
        consumerNow = powerNowArray[0] * timePowerOne / 100 + powerNowArray[1] * timePowerTwo / 100
        if consumerNow % self.powerMax >= self.powerMin:
            amtStation = consumerNow // self.powerMax + 1
        else:
            amtStation = consumerNow // self.powerMax
        time.sleep(0.1)
        return int(consumerNow), amtStation

class ConsumerPower():

    def __init__(self, powerOne, powerTwo):
        self.powerOne = powerOne # Базовая нагрузка 1 потребителя 100%
        self.powerTwo = powerTwo # Базовая нагрузка 2 потребителя 100%
        self.timePowerOne = [40, 40, 40, 40, 40, 40, 90, 90, 90, 90, 80, 80, 80, 80, 100, 100, 100, 100, 100, 100, 80,
                             80, 40, 40]  # график нагрузки 1
        self.timePowerTwo = [80, 80, 80, 80, 80, 80, 90, 90, 100, 100, 80, 80, 80, 80, 100, 100, 100, 100, 100, 90, 90,
                             80, 80, 80]  # график нагрузки 2

    def consumption(self):
        nOne = random.randint(70, 130) / 100  # разброс нагрузки 1
        nTwo = random.randint(80, 120) / 100  # разброс нагрузки 2
        powerNowOne = self.powerOne * nOne
        powerNowTwo = self.powerTwo * nTwo
        powerNowArray = []
        powerNowArray.append(powerNowOne)
        powerNowArray.append(powerNowTwo)
        return powerNowArray


a = ConsumerPower(200,100)
b = PowerStation(6, 40, 75)
consumerArray = []
productionArray = []
for day in range(1): # количесиво дней
    print('День:', day+1)
    for t in range(len(a.timePowerOne)): # перебор по часам
        con = a.consumption()
        prod = b.production(con, a.timePowerOne[t], a.timePowerTwo[t])
        consumerArray.append(prod[0]) # график реального потребления двух нагрузок
        productionArray.append(prod[1])
        print('Время', b.timeDay[t], 'ч. - потребление', prod[0], 'МВт - количество генераторов', prod[1])


data = {'Время': b.timeDay, 'Потребление': consumerArray, 'Количество генераторов': productionArray}
df = pd.DataFrame(data)
print(df)
print(df["Потребление"])
df['Потребление'].plot.hist()
sns.barplot(x=df['Время'], y=df['Потребление'])


