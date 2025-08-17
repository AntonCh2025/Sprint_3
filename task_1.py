import datetime as dt

class ValueError(Exception):
    
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        if self.message:
            return f'{self.message}'
        return f'Неизвестная ошибка ValueError'
    

class NameError(Exception):
    
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        if self.message:
            return f'{self.message}'
        return f'Неизвестная ошибка NameError'
    

class OnlineSalesRegisterCollector:
    
    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def __number_items_discount(self):
        if len(self.__name_items) > 10:
            return 0.9
        else:
            return 1 

    @property
    def name_items(self):
        return self.__name_items
    
    @property
    def number_items(self):
        return self.__number_items
    
    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')            
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')            
        self.__name_items.append(name)
        self.__number_items +=1

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')            
        self.__name_items.remove(name)
        self.__number_items -=1

    def check_amount(self):
        total = []

        for item in self.__name_items:
            total.append(self.__item_price[item])
        
        return sum(total) * self.__number_items_discount

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []

        for item in self.__name_items:
            if self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)
                total.append(self.__item_price[item])
            
        return sum(total) * self.__number_items_discount * 0.2

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []

        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)
                total.append(self.__item_price[item])

        return sum(total) * self.__number_items_discount * 0.1

    def total_tax(self):
        return self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()

    @staticmethod
    def get_telephone_number(telephone_number):
        if type(telephone_number) != int:
            raise ValueError('Необходимо ввести цифры')
        if len(str(telephone_number)) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')            
        return f'+7{telephone_number}'        

    @staticmethod
    def get_date_and_time():
        now = dt.datetime.now()
        date = (lambda x: [['часы', x.hour], ['минуты', x.minute], ['день', x.day], ['месяц', x.month], ['год', x.year]])(now)
        date_and_time = []

        for item in date:
            date_and_time.append(f'{item[0]}: {item[1]}')

        return date_and_time
        