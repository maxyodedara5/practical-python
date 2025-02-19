class Stock:
    """Stock class"""
    __slots__ = ('name', '_shares', 'price')
    def __init__(self, name, shares, price) -> None:
        self.name = name
        self._shares = shares
        self.price = price

    def __repr__(self) -> str:
        return f"Stock({self.name}, {self.shares}, {self.price})"

    @property          
    def cost(self):
        return self.shares * self.price
    
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected Int")
        self._shares = value

    def sell(self, to_sell):
        self.shares -= to_sell
        