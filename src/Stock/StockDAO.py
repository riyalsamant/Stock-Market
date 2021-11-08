
from src.Stock.CommonStock import CommonStock
from src.Stock.PreferredStock import PreferredStock

stocks = {"TEA": CommonStock("TEA", 0, 100), "POP": CommonStock("POP", 8, 100),
          "ALE": CommonStock("ALE", 23, 60),
          "GIN": PreferredStock("GIN",  8, 100, 0.02),
          "JOE": CommonStock("JOE", 13, 250)}


def get_all():
    return stocks


def clear():
    stocks.clear()


def remove_element(key):
    stocks.pop(key)


def add(key, value):
    stocks[key] = value


def find_element(key):
    return stocks[key.upper()]


