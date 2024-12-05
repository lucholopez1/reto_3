class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_total_price(self):
        return self.price


class Beverage(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size


class Appetizer(MenuItem):
    def __init__(self, name, price, portion):
        super().__init__(name, price)
        self.portion = portion


class MainCourse(MenuItem):
    def __init__(self, name, price, cooking_level):
        super().__init__(name, price)
        self.cooking_level = cooking_level


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total_bill(self):
        total = sum(item.calculate_total_price() for item in self.items)
        return total
    
    def apply_discount(self, discount_percentage):
        total = self.calculate_total_bill()
        discount_amount = total * (discount_percentage / 100)
        return total - discount_amount


# Uso
menu = [
    Beverage("Sprite", 5000, "Mediana"),
    Beverage("Limonada", 8000, "Grande"),
    Beverage("Agua", 3000, "Pequeña"),
    Appetizer("Rollos de canela", 10000, "Medianos"),
    Appetizer("Brownie con helado", 8000, "Pequeño"),
    Appetizer("Porción de nachos", 15000, "Grande"),
    MainCourse("Bisteck", 40000, "Grande"),
    MainCourse("Mojarra", 50000, "Grande"),
    MainCourse("Pechuga a la plancha", 35000, "Grande")
]

#ejemplo

order = Order()
order.add_item(menu[0])
order.add_item(menu[5])
order.add_item(menu[7])

print(f"Subtotal: {order.calculate_total_bill()}")
print(f"Total a pagar (10% de descuento aplicado): {order.apply_discount(10)}")
