import datetime as dt

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        records = []

    def GetCurrentSum(currency, limit):

        USD_RATE  = 60
        EURO_RATE = 70



class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)
        #records = []

    def get_calories_remained(self):
        # Определять, сколько ещё калорий можно/нужно получить сегодня

        colory = currentlimitcalory()    
        answer_calory = ''

        if limit > currentlimitcalory:
            n_text = limit - currentlimitcalory
            answer_calory = f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {n_text} кКал'
        else:
            answer_calory = 'Хватит есть!'
        
        return answer_calory


    def add_record(self):
        #Сохранять новую запись о приёме пищи— метод
        self.records.append(Record)

    
    def get_today_stats():
        #Считать, сколько калорий уже съедено сегодня — метод
        print()
        pass

    def get_week_stats():
        #Считать, сколько калорий получено за последние 7 дней — метод
        print()
        pass

class CashCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)
        #records = []


    def get_today_cash_remained(currency):
        #Определять, сколько ещё денег можно потратить сегодня в рублях, долларах или евро — метод
        
        CurentSum = GetCurrentSum(currency)
        answer_limit = ''

        if CurentSum > limit: # Есил лимит не достигнут
            answer_limit = f'На сегодня осталось N {currency}'
        elif CurentSum > limit: #Если лимит достигнут
            answer_limit = 'Денег нет, держись'
        elif CurentSum > limit: #если лимит превышен
            answer_limit = 'Денег нет, держись: твой долг - N руб/USD/Euro'

        return answer_limit

    def add_record(Record)
        #Сохранять новую запись о приёме пищи— метод
        self.records.append(Record)

    def get_today_stats():
        #Считать, сколько денег потрачено сегодня
        pass

    def get_week_stats():
        #Считать, сколько денег потрачено за последние 7 дней — метод 
        pass





class Record:
    def __init__(self, amount = 0, comment = '', date = dt.datetime.now().date()):
        
        if amount == 0:
            print('Укажаите число трат')
            pass

        self.amount = amount
        self.comment = comment
        self.date = date
    



'''
# для CashCalculator 
r1 = Record(amount=145, comment="Безудержный шопинг", date="08.03.2019")
r2 = Record(amount=1568, comment="Наполнение потребительской корзины", date="09.03.2019")
r3 = Record(amount=691, comment="Катание на такси", date="08.03.2019")

# для CaloriesCalculator
r4 = Record(amount=1186, comment="Кусок тортика. И ещё один.", date="24.02.2019")
r5 = Record(amount=84, comment="Йогурт.", date="23.02.2019")
r6 = Record(amount=1140, comment="Баночка чипсов.", date="24.02.2019"
'''


'''
# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = CashCalculator(1000)
        
# дата в параметрах не указана, 
# так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment="кофе")) 
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
                
print(cash_calculator.get_today_cash_remained("rub"))
# должно напечататься
# На сегодня осталось 565 руб
'''


'''
class Bird:
    def __init__(self, name, size):
            self.name = name
            self.size = size
    def show(self):       
            print(f'{self.name} носит одежду размера «{self.size}».')

class Parrot(Bird):
    def __init__(self, name, size, sound):
        super().__init__(name, size)
        self.sound = sound
    def show(self):
        print(f'{self.name} носит одежду размера «{self.size}» и {self.sound}.')

class Predator(Bird):
    def __init__(self, name, size, claws_size):
        super().__init__(name, size)
        self.claws_size = claws_size
    def show(self):
        print(f'{self.name} носит одежду размера «{self.size}» и когти размера {self.claws_size}.')

class Egg(Predator):
    def show(self):
        print(f'Из яйца вылупится птичка {self.name} размера «{self.size}» с когтями размера {self.claws_size}.')
'''

'''
class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def show(self):
        print(f'{self.name} ({self.phone})')

# объявляем класс Friend, дочерний по отношению к классу User
class Friend(User):
    def show(self):
        print(f'Имя: {self.name} || Телефон: {self.phone}')

# создаём объекты User и Friend
father = User("Дюма-отец", "+33 3 23 96 23 30")
son = Friend("Дюма-сын", "+33 3 23 96 23 30")
'''