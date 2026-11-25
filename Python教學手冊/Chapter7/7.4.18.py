class Year:
    def __init__(self, Year):
        self.__year = Year

    def isleap(self):
        return self.__year % 400 == 0 or (self.__year % 4 == 0 and self.__year % 100 != 0)

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_Year):
        self.__year = new_Year


y0 = Year(2024)
print(y0.isleap())
print(y0.year)
y0.year = 2023
print(y0.isleap())