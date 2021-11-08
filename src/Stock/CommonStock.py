import math

from src.Stock.Stock import Stock, StockType


class CommonStock(Stock):
    def __init__(self, symbol, last_dividend, par_value, fixed_dividend=None):
        super().__init__(symbol, StockType.COMMON.name, last_dividend, par_value, fixed_dividend)

    def calculate_dividend_yield(self, price):
        if math.isnan(price):
            raise ValueError('Price is not a number!' + price)
        return self.last_dividend / price
