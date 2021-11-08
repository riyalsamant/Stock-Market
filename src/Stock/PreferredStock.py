import math

from src.Stock.Stock import Stock, StockType


class PreferredStock(Stock):
    def __init__(self, symbol, last_dividend, par_value, fixed_dividend=None):
        super().__init__(symbol, StockType.PREFERRED.name, last_dividend, par_value, fixed_dividend)

    def calculate_dividend_yield(self, price):
        if math.isnan(price):
            raise ValueError('Price is not a number!' + price)
        return 0 if self.fixed_dividend is None else (self.fixed_dividend * self.par_value) / price
