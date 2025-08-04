'''Write a system that calculates the price of a pizza, based on its ingredients.
A friend of yours is going to open a pizza restaurant and they asked you to build the software to support it. Concretely, you need to work on price

Pizzas are composed of:
1 base (e.g.: thin, regular, cheesy crust)
1 size (e.g.: small, medium, large)
0..N toppings (e.g.: olives, cheese, pepperoni)

Price = (base price + sum(toppings prices)) * size multiplier'''

class Pizza:
    BASE_PRICES = {
        'thin': 5.0,
        'regular': 6.0,
        'cheesy crust': 7.0
    }

    SIZE_MULTIPLIER = {
        'small': 1.0,
        'medium': 1.2,
        'large': 1.5
    }

    TOPPING_PRICES = {
        'olives': 0.5,
        'cheese': 1.0,
        'pepperoni': 1.5
    }

    def __init__(self, base: str, size: str, toppings: list):
        self.base = base
        self.size = size
        self.toppings = toppings  # list of topping strings

    def calculate_price(self):
        base_price = Pizza.BASE_PRICES[self.base]
        topping_total = sum(Pizza.TOPPING_PRICES[t] for t in self.toppings)
        multiplier = Pizza.SIZE_MULTIPLIER[self.size]
        return (base_price + topping_total) * multiplier


pizza = Pizza('cheesy crust', 'large', ['cheese', 'pepperoni'])
print(f"Total price: ${pizza.calculate_price():.2f}")
