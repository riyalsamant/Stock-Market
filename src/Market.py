import logging
import math
from datetime import datetime, timedelta

from src.Stock import StockDAO
from src.Trade import TradeDAO
from src.Trade.Trade import Trade


def calculate_dividend_yield(symbol, price):
    try:
        logging.info("Calculating dividend yield for stock " + symbol)
        stock = StockDAO.find_element(symbol)
        if math.isnan(price) or price == 0:
            raise ValueError("Invalid price!" + price)
        return round(stock.calculate_dividend_yield(price), 4)
    except Exception as e:
        logging.error("Exception occurred while calculating Dividend yield" + str(e))


def calculate_pe_ratio(symbol, price):
    try:
        logging.info("Calculating PE Ratio for stock " + symbol)
        stock = StockDAO.find_element(symbol)
        if math.isnan(price) or price == 0:
            raise ValueError("Invalid price!" + price)
        return round(stock.calculate_pe_ratio(price), 4)
    except Exception as e:
        logging.error("Exception occurred while calculating Dividend yield" + str(e))


def record_trade(symbol, indicator, quantity, price, creation_timestamp):
    try:
        logging.info("Adding new trade")
        TradeDAO.add(Trade(symbol, indicator, quantity, price, creation_timestamp))
    except Exception as e:
        logging.error("error occurred while recording trade" + str(e))


def calc_volume_weighted_stock_price(symbol):
    try:
        logging.info("Calculating volume weighted stock price for stock " + symbol)
        if not StockDAO.find_element(symbol):
            raise ValueError("Invalid stock " + symbol)
        vwsp_num = 0
        vwsp_denum = 0
        for trade in filter_on_timestamp(TradeDAO.filter_stock(symbol), 5):
            vwsp_num += trade.price * trade.quantity
            vwsp_denum += trade.quantity
        logging.info("Volume weighted stock price for " + symbol + " was calculated successfully")
        return 0 if vwsp_denum == 0 else round(vwsp_num / vwsp_denum, 4)
    except Exception as e:
        logging.error("error occurred while calculating volume weighted stock price for stock " + str(symbol) + str(e))


def filter_on_timestamp(trades, interval=None):
    if interval is None:
        return trades
    time = datetime.now() - timedelta(minutes=interval)
    return filter(lambda x: x.creation_timestamp >= time, trades)


def calc_gbce():
    try:
        logging.info("Calculating GBCE All Share index for all stocks")
        stocks = StockDAO.get_all()
        gmean = 1.0
        for stock in stocks.values():
            vwsp = calc_volume_weighted_stock_price(stock.symbol)
            gmean *= 1.0 if vwsp == 0 else vwsp
            logging.info("Calculated Volume weighted stock price for stock " + str(stock.symbol))
        return 0 if len(TradeDAO.trades) == 0 else round(math.pow(gmean, 1 / len(TradeDAO.trades)), 4)
    except Exception as e:
        logging.error("error occurred while calculating GBCE All Share Index " + str(e))
