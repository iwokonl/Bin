import datetime


class Court(object):
    width: float
    length: float
    address: str
    year_built: int

    def __init__(self,   width: float = 68, length: float = 150, *, address: str, year_built: int) -> None:
        if year_built < 2008:
            if width >= 90 and width <= 120 and length >= 45 and length <= 90:
                self.length = length
                self.width = width
                self.__length = length
                self.__width = width
        if year_built >= 2008:
            self.__width = width
            self.__length = length
        self.address = address
        self.year_built = year_built
        self.__address = address
        self.__year_built = year_built

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, value: float):
        self.__width = value

    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, value: float):
        self.__length = value

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, value) -> str:
        self.__address = value

    @property
    def _year_built(self) -> int:
        return self.__year_built

    @_year_built.setter
    def year_built(self, value: int):
        self.__year_built = value

    @staticmethod
    def validate(value):
        if value.year_built < 0:
            value.year_built = datetime.datetime.now().year
        if value.year_built > datetime.datetime.now().year:
            value.year_built = datetime.datetime.now().year

    def area(self) -> float:
        return self.width * self.length

    def __get__(self, instance, owner):
        return self.year_built

    def __str__(self):
        return f"Boisko wybudowane w roku {self.year_built}, o długości {self.length} metrów i szerokości " \
               f"{self.width} metrów.\nPole powierzchni: {Court.area(self)} mkw.\nAdres: {self.address}"

    def __eq__(self, other: 'Court'):
        if Court.area(self) == other.area():
            return True
        else:
            return False

    def __ne__(self, other):
        if Court.area(self) != other.area():
            return True
        else:
            return False
