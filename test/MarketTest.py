import datetime
import unittest

from src import Market
from src.Stock import StockDAO
from src.Stock.CommonStock import CommonStock
from src.Stock.PreferredStock import PreferredStock
from src.Trade import TradeDAO
from src.Trade.Trade import Trade
from src.Trade.TradeType import TradeType
from datetime import datetime, timedelta


def clear_data():
    TradeDAO.clear()


class MarketTest(unittest.TestCase):

    def test_add_stock_and_calculate_dividend_yield(self):
        clear_data()
        StockDAO.add("TEST", CommonStock("TEST", 0, 10))
        exp_div_yield = 0.0
        self.assertEqual(exp_div_yield, Market.calculate_dividend_yield("TEST", 10))

    def test_add_and_calculate_dividend_yield_preferred_stock(self):
        clear_data()
        StockDAO.add("TEST", PreferredStock("TEST", 10, 10, 0.5))
        exp_div_yield = 0.05
        self.assertEqual(exp_div_yield, Market.calculate_dividend_yield("TEST", 100))

    def test_calculate_dividend_yield_all(self):
        clear_data()
        self.assertEqual(0, Market.calculate_dividend_yield("TEA", 100))
        self.assertEqual(0.08, Market.calculate_dividend_yield("POP", 100))
        self.assertEqual(0.23, Market.calculate_dividend_yield("ALE", 100))
        self.assertEqual(0.02, Market.calculate_dividend_yield("GIN", 100))
        self.assertEqual(0.13, Market.calculate_dividend_yield("JOE", 100))

    def test_calculate_pe_ratio_all(self):
        clear_data()
        self.assertEqual(0, Market.calculate_pe_ratio("TEA", 50))
        self.assertEqual(6.25, Market.calculate_pe_ratio("POP", 50))
        self.assertEqual(2.1739, Market.calculate_pe_ratio("ALE", 50))
        self.assertEqual(6.25, Market.calculate_pe_ratio("GIN", 50))
        self.assertEqual(3.8462, Market.calculate_pe_ratio("JOE", 50))

    def test_case_for_stock(self):
        clear_data()
        self.assertEqual("POP", StockDAO.find_element("PoP").symbol)
        self.assertEqual("POP", StockDAO.find_element("pop").symbol)

    def test_invalid_symbol_for_stock(self):
        clear_data()
        with self.assertRaises(KeyError):
            StockDAO.find_element("VOD")

    def test_invalid_last_dividend(self):
        clear_data()
        with self.assertRaises(Exception):
            CommonStock("TEST", -1, 10)

    def test_invalid_par_value(self):
        clear_data()
        with self.assertRaises(Exception):
            CommonStock("TEST", 1, "abc")

    def test_calc_volume_weighted_stock_price(self):
        clear_data()
        Market.record_trade("POP", TradeType.BUY.name, 2, 100, datetime.now())
        Market.record_trade("GIN", TradeType.SELL.name, 10, 100, datetime.now())
        Market.record_trade("JOE", TradeType.SELL.name, 10, 100, datetime.now())
        Market.record_trade("POP", TradeType.SELL.name, 45, 90, datetime.now())

        self.assertEqual(90.4255, Market.calc_volume_weighted_stock_price("POP"))

        Market.record_trade("POP", TradeType.SELL.name, 45, 90, datetime.now() - timedelta(minutes=6))
        self.assertEqual(90.4255, Market.calc_volume_weighted_stock_price("POP"))

        self.assertEqual(100, Market.calc_volume_weighted_stock_price("GIN"))
        self.assertEqual(0, Market.calc_volume_weighted_stock_price("TEA"))

    def test_record_trade_invalid_quantity(self):
        clear_data()
        with self.assertRaises(ValueError):
            Trade("POP", TradeType.BUY.name, -2, 100, datetime.now())

    def test_record_trade(self):
        clear_data()
        Market.record_trade("POP", TradeType.BUY.name, 2, 100, datetime.now())
        self.assertEqual(1, len(TradeDAO.trades))

    def test_record_trade_invalid_price(self):
        clear_data()
        with self.assertRaises(Exception):
            Trade("POP", TradeType.BUY.name, 2, None, datetime.now())

    def test_record_trade_invalid_date(self):
        clear_data()
        with self.assertRaises(Exception):
            Trade("POP", TradeType.BUY.name, 2, 400, datetime.now() + timedelta(minutes=6))

    def test_calc_gbce_no_trades(self):
        clear_data()
        self.assertEqual(0, Market.calc_gbce())

    def test_calc_gbce(self):
        clear_data()
        Market.record_trade("POP", TradeType.BUY.name, 1, 30, datetime.now())
        Market.record_trade("GIN", TradeType.SELL.name, 2, 40, datetime.now())
        Market.record_trade("JOE", TradeType.SELL.name, 5, 70, datetime.now())
        Market.record_trade("POP", TradeType.SELL.name, 4, 50, datetime.now())
        self.assertEqual(18.9443, Market.calc_gbce())




if __name__ == '__main__':
    MarketTest.main()
