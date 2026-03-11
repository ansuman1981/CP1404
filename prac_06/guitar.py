import datetime
class Guitar:
    def __init__(self, name= "", year = 0, cost = 0):
        self.name = name
        self.year = year
        self.cost = cost
    def __str__(self):

        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        current_year = datetime.datetime.now().year
        return current_year - self.year

    def is_vantage(self):
       return self.get_age() >= 50
