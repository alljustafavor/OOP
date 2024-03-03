import csv

class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Vaildations
        if price <= 0:
            raise ValueError(f"Price: {price} is not greater than 1")
        if quantity <= 0:
            raise ValueError(f"Quantity: {quantity} is not greater than 1")

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)
    
    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self) -> float:
        self.price = self.price * self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
           Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )


    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)


Item.instantiate_from_csv()
print(Item.all)
