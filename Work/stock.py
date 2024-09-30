class Stock:
    """Stock class"""

    def __init__(self, name, shares, price) -> None:
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self) -> str:
        return f"Stock({self.name}, {self.shares}, {self.price})"
                
    def cost(self):
        return self.shares * self.price
    
    def sell(self, to_sell):
        self.shares -= to_sell
        