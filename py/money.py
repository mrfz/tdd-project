class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    def __str__(self) -> str:
        return f"{self.currency} {self.amount:0.2f}"

    def __add__(self, other):
        if other is not None and self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        else:
            return None

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def divide(self, divisor):
        return Money(self.amount / divisor, self.currency)
