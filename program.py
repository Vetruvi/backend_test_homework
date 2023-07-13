import datetime as dt

import constant


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.today_amount = 0

    def add_record(self, other):
        self.records.append([other.amount, other.comment, other.date])


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount

        self.comment = comment

        if date is None:
            now = dt.datetime.now()
            self.date = now.date()
        else:
            date_format = '%d.%m.%Y'
            moment = dt.datetime.strptime(date, date_format)
            self.date = moment.date()


class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_today_stats(self):

        now = dt.datetime.now()
        today_amount = self.today_amount
        for i in range(len(self.records)):
            if self.records[i][2] == now.date():
                today_amount += self.records[i][0]
        print(f"Сегодня потрачено каллорий {today_amount}")

    def get_calories_remained(self):

        now = dt.datetime.now()
        limit = self.limit
        for i in range(len(self.records)):
            if self.records[i][2] == now.date():
                limit -= self.records[i][0]
        if limit > 0:
            print(f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {limit}")
        else:
            print(f"Хватит есть!")

    def get_week_stats(self):

        now = dt.datetime.now()
        past = now.date() - dt.timedelta(days=7)
        Calories_per_week = 0
        for i in range(len(self.records)):
            if self.records[i][2] > past:
                Calories_per_week += self.records[i][0]
        print(f"За неделю получено {Calories_per_week} каллорий")


class CashCalculator(Calculator):

    def __init__(self, limit):
        super().__init__(limit)

    def get_today_stats(self, currency):

        now = dt.datetime.now()

        limit = self.limit

        if currency == "usd" or currency == "USD":
            self.today_amount /= constant.USD_RATE
            limit /= constant.USD_RATE
        elif currency == "euro" or currency == "EURO":
            self.today_amount /= constant.EURO_RATE
            limit /= constant.EURO_RATE

        for i in range(len(self.records)):
            if self.records[i][2] == now.date():
                record_amount = self.records[i][0]
                if currency == "usd" or currency == "USD":
                    self.today_amount += (record_amount / constant.USD_RATE)
                elif currency == "euro" or currency == "EURO":
                    self.today_amount += (record_amount / constant.EURO_RATE)
                else:
                    self.today_amount += record_amount

        print(f"Сегодня потрачено денег {self.today_amount} {currency}")

    def get_today_cash_remained(self, currency):

        now = dt.datetime.now()

        limit = self.limit

        if currency == "usd" or currency == "USD":
            limit /= constant.USD_RATE
        elif currency == "euro" or currency == "EURO":
            limit /= constant.EURO_RATE

        for i in range(len(self.records)):
            if self.records[i][2] == now.date():
                record_amount = self.records[i][0]
                if currency == "usd" or currency == "USD":
                    limit -= (record_amount / constant.USD_RATE)
                elif currency == "euro" or currency == "EURO":
                    limit -= (record_amount / constant.EURO_RATE)
                else:
                    limit -= record_amount

        if limit > 0:
            print(f"На сегодня осталось {limit} {currency}")
        elif limit == 0:
            print("Денег нет, держись")
        else:
            print(f"Денег нет, держись: твой долг - {abs(limit)} {currency}")

    def get_week_stats(self, currency):

        now = dt.datetime.now()
        past = now.date() - dt.timedelta(days=7)
        Amount_per_week = 0
        for i in range(len(self.records)):
            if self.records[i][2] > past:
                record_amount = self.records[i][0]
                if currency == "usd" or currency == "USD":
                    Amount_per_week += (record_amount / constant.USD_RATE)
                elif currency == "euro" or currency == "EURO":
                    Amount_per_week += (record_amount / constant.EURO_RATE)
                else:
                    Amount_per_week += record_amount

        print(f"За неделю потрачено {Amount_per_week} {currency}")

cash_calculator = CashCalculator(1000)

calories_calculator = CaloriesCalculator(1000)

cash_calculator.add_record(Record(amount=400, comment="кофе"))

cash_calculator.add_record(Record(amount=700, comment="Чай"))

calories_calculator.add_record(Record(amount=500, comment="кофе"))

calories_calculator.add_record(Record(amount=800, comment="Чай"))

cash_calculator.add_record(Record(amount=185, comment="Мороженка", date="12.07.2023"))

cash_calculator.add_record(Record(amount=300, comment="Мороженка", date="11.07.2023"))

cash_calculator.add_record(Record(amount=500, comment="Мороженка", date="10.07.2023"))

cash_calculator.add_record(Record(amount=600, comment="Мороженка", date="9.07.2023"))

cash_calculator.add_record(Record(amount=600, comment="Мороженка", date="6.07.2023"))

calories_calculator.add_record(Record(amount=185, comment="Мороженка", date="12.07.2023"))

calories_calculator.add_record(Record(amount=300, comment="Мороженка", date="11.07.2023"))

calories_calculator.add_record(Record(amount=500, comment="Мороженка", date="10.07.2023"))

calories_calculator.add_record(Record(amount=600, comment="Мороженка", date="9.07.2023"))

calories_calculator.add_record(Record(amount=600, comment="Мороженка", date="6.07.2023"))

cash_calculator.get_today_stats("rub")

calories_calculator.get_today_stats()

cash_calculator.get_today_cash_remained("rub")

calories_calculator.get_calories_remained()

cash_calculator.get_week_stats("euro")

calories_calculator.get_week_stats()
