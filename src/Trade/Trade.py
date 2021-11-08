import datetime
import math

from src.Stock import StockDAO
from datetime import datetime

from src.Trade.TradeType import TradeType


def validate_date(date):
    return datetime.fromisoformat(date)


class Trade(object):
    def __init__(self, stock, indicator, quantity, price, creation_timestamp):
        self.stock = stock
        self.indicator = indicator
        self.quantity = quantity
        self.price = price
        self.creation_timestamp = creation_timestamp

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, stock):
        if not (stock or StockDAO.find_element(stock)):
            raise Exception("Invalid stock value" + str(stock))
        self._stock = stock

    @property
    def indicator(self):
        return self._indicator

    @indicator.setter
    def indicator(self, indicator):
        if not indicator or indicator.upper() not in TradeType.__members__:
            raise Exception("Invalid indicator value" + str(indicator))
        self._indicator = indicator

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if math.isnan(quantity) or quantity <= 0:
            raise ValueError("Invalid quantity:" + str(quantity))
        self._quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if math.isnan(price) or price <= 0:
            raise ValueError('Invalid price' + str(price))
        self._price = price

    @property
    def creation_timestamp(self):
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, timestamp):
        if datetime.now() < validate_date(str(timestamp)):
            raise Exception(str(timestamp) + ' cannot be greater than current time')
        self._creation_timestamp = timestamp
