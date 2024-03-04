from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(
            name, price, quantity
        )

        if broken_phones <= 0:
            raise ValueError(f"Broken Phones: {broken_phones} is not greater than 1")

        self.broken_phones = broken_phones


