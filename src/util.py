import random

def roll(num, die) -> int:
    result = 0
    for i in range(num):
        result += random.uniform(1, die)
    return result


class Time:
    
    MONTHS = [
        "Early-Spring", 
        "Mid-Spring", 
        "Late-Spring", 
        "Early-Summer", 
        "Mid-Summer", 
        "Late-Summer", 
        "Early-Autumn", 
        "Mid-Autumn", 
        "Late-Autumn", 
        "Early-Winter", 
        "Mid-Winter",  
        "Late-Winter", 
    ]

    def __init__(self):
        self.year = 666
        self.day = random.randint(1, 360)

    def next_day(self):
        self.day += 1
        while self.day > 360:
            self.day -= 360
            self.year += 1

    def get_date(self) -> str:
        day_of_month = (self.day - 1) % 30 + 1
        month_name = self.MONTHS[int((self.day - 1) / 30)]
        return f"{day_of_month} {month_name}, Year {self.year} SE"
