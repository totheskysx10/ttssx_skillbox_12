class Property:
    def __init__(self, worth):
        self.worth = worth

    def __calc__(self):
        pass

class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.percentage = 1.0 / 1_000

    def calc(self):
        return self.worth * self.percentage

class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.percentage = 1.0 / 200

    def calc(self):
        return self.worth * self.percentage

class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.percentage = 1.0 / 500

    def calc(self):
        return self.worth * self.percentage

property_type = input('Введите тип имущества(квартира, машина, дача): ')
cost = int(input('Введите стоимость имущества: '))
if property_type.lower() in ['квартира', 'машина', 'дача']:
    if property_type.lower() == 'квартира':
        chosen = Apartment(cost)
    elif property_type.lower() == 'машина':
        chosen = Car(cost)
    else:
        chosen = CountryHouse(cost)
    print('Налог на ваше имущество:', chosen.calc())
else:
    print('Ошибка ввода!')