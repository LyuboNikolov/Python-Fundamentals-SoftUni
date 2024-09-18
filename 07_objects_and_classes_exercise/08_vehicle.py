class Vehicle:
    def __init__(self, vehicle_type, model, price, owner=None):
        self.type = vehicle_type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money: int, owner: str):
        if money >= self.price and not self.owner:
            self.owner = owner
            change = money - self.price
            return f"Successfully bought a {self.type}. Change: {change:.2f}"

        elif money < self.price:
            return "Sorry, not enough money"

        return "Car already sold"

    def sell(self):
        if not self.owner:
            return "Vehicle has no owner"

        self.owner = None

    def __repr__(self):
        if self.owner:
            return f"{self.model} {self.type} is owned by: {self.owner}"

        return f"{self.model} {self.type} is on sale: {self.price}"
