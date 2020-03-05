import datetime as dt
from datetime import timedelta, datetime

class Record:
    def __init__(self, amount = 0, comment = '', date = dt.datetime.now().date()):
        super(Record, self).__init__()
        
        if amount == 0:
            print('Укажаите число трат')
            pass
        
        if type(date) == str:
            date_format = '%d.%m.%Y'
            date = dt.datetime.strptime(date, date_format).date()

        self.amount = amount
        self.comment = comment
        self.date = date
    

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    #Сохранять новую запись о приёме пищи— метод
    def add_record(self, Record):
        self.records.append(Record)

    def today(self):
        return dt.datetime.now().date()

    def get_today_sum(self, records):

        today = self.today()
        sum_of_recods = 0    

        for rw in range(len(records)):
            if records[rw].date == today:
                    sum_of_recods += records[rw].amount
        
        return sum_of_recods

    def get_last_week_sum(self, records):

        today = self.today()

        date_list = []
        ittr = 0

        while ittr <= 6: # "Сегодня" тоже считаем 
            find_date = today - timedelta(ittr)
            date_list.append(find_date)
            ittr += 1


        sum_week_records = 0    

        for rw in range(len(records)):
             if records[rw].date in date_list:
                sum_week_records += records[rw].amount

        return sum_week_records    

    def get_current_cash_sum(self, currency, records, EURO_RATE, USD_RATE):
    
        rate_currency = {'eur': EURO_RATE,'usd': USD_RATE,'rub': 1}
        sum_today = self.get_today_sum(records) 
        limit_currency = self.limit
        
        sum_today = sum_today / rate_currency[currency]
        limit_currency = limit_currency / rate_currency[currency]
        
        balance = limit_currency - sum_today
        
        return  round(balance,2)

    def get_current_limit_calory(self,records):

        current_calory_today = self.get_today_sum(records)

        balance = self.limit - current_calory_today

        return round(balance, 2)

    #Считать, сколько калорий уже съедено сегодня — метод
    def get_today_stats(self):

        stats_today = self.get_today_sum(self.records)
        return stats_today

    #Считать, сколько калорий получено за последние 7 дней — метод    
    def get_week_stats(self):

        week_stat = self.get_last_week_sum(self.records)
        return week_stat



class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)


    # Определять, сколько ещё калорий можно/нужно получить сегодня
    def get_calories_remained(self):

        balance = super().get_current_limit_calory(self.records)    
        answer_calory = ''

        if balance > 0:
            answer_calory = f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {balance} кКал'
        else:
            answer_calory = 'Хватит есть!'
        
        return answer_calory
    

class CashCalculator(Calculator):
    
    EURO_RATE = 70.00
    USD_RATE = 60.00

    def __init__(self, limit):
        super().__init__(limit)


    def get_today_cash_remained(self, currency):
        #Определять, сколько ещё денег можно потратить сегодня в рублях, долларах или евро — метод
        
        list_of_currency = ['rub','usd','eur']

        if not currency in list_of_currency:
            print(f'Укажите валюту правильно: {list_of_currency[0]},{list_of_currency[1]},{list_of_currency[2]}')

        print_currency = {'eur':'Euro','usd':'USD','rub':'руб'}    

        limit = super().get_current_cash_sum(currency, self.records, CashCalculator.EURO_RATE, CashCalculator.USD_RATE)

        if limit > 0: # Есил лимит не достигнут
            answer_limit = f'На сегодня осталось {limit} {print_currency[currency]}'
        elif limit == 0: #Если лимит достигнут
            answer_limit = 'Денег нет, держись'
        elif limit < 0: #если лимит превышен
            answer_limit = f'Денег нет, держись: твой долг - {limit * -1} {print_currency[currency]}'

        return answer_limit