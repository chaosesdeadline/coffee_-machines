print("Здравствуйте это кофе автомат, какой кофе вы хотите выбрать введите пожалуйста его на экран", "\n"
      "**********************************************************************************************", "\n"
      "Вот какие варианты у нас есь: Мокка': 100, 'Капучино': 110, 'Эспрессо': 50, 'Американо': 80,'Латте': 100", "\n")

a = input("Введите название кофе: ")
b = int(input("Вложите количество ваших деньжюнечек: "))

class Machine:

    slov_coff = {'Мокка': 100,
                 'Капучино': 110,
                 'Эспрессо': 50,
                 'Американо': 80,
                 'Латте': 100}

    def __init__(self, cof, money):
        self.cof = cof
        self.money = money

    sdacha = 0
    pomosh = 0

    def podschet(self):
        for i, j in Machine.slov_coff.items():
            if self.cof == i:
                if self.money > j:
                    Machine.sdacha = self.money - j
                    Machine.pomosh = 1
                elif self.money < j:
                    print("Денег было вложено недостаточно")
                    break
                else:
                    print("Сдачи не будет!")
                    Machine.pomosh = 1

    def give_coffee(self):
        if Machine.pomosh == 0:
            print('Кофе не будет, сорян, иди нахасли бабок')
        elif Machine.sdacha == 0:
            print(f'держите ваш: {self.cof}, сдачи не будет')
        elif Machine.sdacha > 0:
            print(f'держите ваш: {self.cof}, а также вашу сдачу в размере: {Machine.sdacha} рублей')

coo = Machine(a, b)
coo.podschet()
coo.give_coffee()