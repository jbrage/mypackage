# %%
class Computer:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Computer with name '{self.name}', price {self.price} CHF and quantity {self.quantity}."


class Laptop(Computer):
    def __init__(self, name, price, quantity, battery_life):
        super().__init__(name, price, quantity)
        self.battery_life = battery_life

    def __str__(self):
        return (
            super().__str__()
            + f" This laptop has a battery life of {self.battery_life} hours."
        )


class PC(Computer):
    def __init__(self, name, price, quantity, expansion_slots):
        super().__init__(name, price, quantity)
        self.expansion_slots = expansion_slots

    def __str__(self):
        return (
            super().__str__() + f" This PC has {self.expansion_slots} expansion slots."
        )


pc = {"name": "pc_1", "price": 1500, "quantity": 1, "expansion_slots": 2}

laptop = {"name": "laptop_1", "price": 1200, "quantity": 4, "battery_life": 6}

lp = Laptop(**laptop)
print(lp)
# %%
