from interface import Exchange, Trade
import unittest

class InterfaceTests(unittest.TestCase):
    def test_init(self):
        self.assertIsInstance(Exchange(10000), Exchange)

    def test_add_trade(self):
        initial_balance = 1000
        accounts = {
            "Alice": [initial_balance, 500]
        }

        exchange = Exchange(initial_balance, accounts)

        exchange.add_trade(Trade(trader='Alice', is_buy=False, quantity=10, price=50))
        exchange.add_trade(Trade(trader='Bob', is_buy=True, quantity=5, price=50))
        exchange.add_trade(Trade(trader='George', is_buy=True, quantity=7, price=50))

        self.assertEqual(exchange.accounts, {'Alice': [1500, 490], 'Bob': [750, 5], 'George': [750, 5]})
        self.assertEqual(len(exchange.pending), 1)
        self.assertEqual(exchange.pending[0].trader, "George")
        self.assertEqual(exchange.pending[0].quantity, 2)#George still wants 2 more shares

        exchange.add_trade(Trade(trader="Bob", is_buy=False, quantity=5, price=100)) #George still can't buy
        self.assertEqual(exchange.accounts, {'Alice': [1500, 490], 'Bob': [750, 5], 'George': [750, 5]})
        self.assertEqual(len(exchange.pending), 2)


if __name__ == "__main__":
    unittest.main()

