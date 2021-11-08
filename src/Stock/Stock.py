import math
from abc import abstractmethod

from src.Stock.StockType import StockType


class Stock:

    def __init__(self, symbol, stock_type, last_dividend, par_value, fixed_dividend):
        self.symbol = symbol
        self.stock_type = stock_type
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        if not symbol:
            raise ValueError("Symbol cannot be empty")
        self._symbol = symbol.upper()

    @property
    def stock_type(self):
        return self._stock_type

    @stock_type.setter
    def stock_type(self, stock_type):
        if stock_type not in StockType.__members__:
            raise Exception(str(stock_type) + ' is not a valid stock type')
        self._stock_type = stock_type

    @property
    def last_dividend(self):
        return self._last_dividend

    @last_dividend.setter
    def last_dividend(self, last_dividend):
        if (math.isnan(last_dividend) and last_dividend is not None) or last_dividend < 0:
            raise Exception(str(last_dividend) + ' is not a valid value')
        self._last_dividend = last_dividend

    @property
    def fixed_dividend(self):
        return self._fixed_dividend

    @fixed_dividend.setter
    def fixed_dividend(self, fixed_dividend):
        if fixed_dividend is not None and (math.isnan(fixed_dividend) or fixed_dividend < 0):
            raise Exception(str(fixed_dividend) + ' is not a valid value')
        self._fixed_dividend = fixed_dividend

    @property
    def par_value(self):
        return self._par_value

    @par_value.setter
    def par_value(self, par_value):
        if (math.isnan(par_value) and par_value is not None) or par_value < 0:
            raise Exception(str(par_value) + ' is not a valid value')
        self._par_value = par_value

    def calculate_pe_ratio(self, price):
        if math.isnan(price):
            raise ValueError('Price is not a number!' + str(price))
        return 0 if (self.last_dividend == 0 or self.last_dividend is None) else price / self._last_dividend

    @abstractmethod
    def calculate_dividend_yield(self, price):
        pass
