trades = []


def get_all():
    return trades


def clear():
    trades.clear()


def remove_trade(trade):
    trades.remove(trade)


def add(trade):
    trades.append(trade)


def filter_stock(symbol):
    return filter(lambda x: x.stock == symbol.upper(), trades)
