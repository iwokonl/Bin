from court import Court


class Stadium(Court):
    name: str
    common_name: str
    capacity: int

    def __init__(self, width: float, length: float, address: str, year_built: int, name: str
                 , capacity: int, common_name: str = None) -> None:
        super(width, length, address, year_built)
        self.name = name
        self.common_name = common_name
        if int(capacity) >= 0:
            self.capacity = capacity

    def __str__(self):
        if self.common_name is None:
            return f"{Court.__str__(self)}Nazwa: {self.name}\n" \
                   f"Pojemność stadionu: {self.capacity}"
        return f"{Court.__str__(self)}Nazwa: {self.name}\nNazwa zwyczajowa:" \
               f" {self.common_name}\nPojemność stadionu: {self.capacity}"
