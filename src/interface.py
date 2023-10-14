class Trade:
    def __init__(self, trader, is_buy, quantity, price):
        self.trader = trader
        self.is_buy = is_buy
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.trader}: {self.is_buy}, {self.quantity}x{self.price}"

    def copy(self):
        return Trade(self.trader, self.is_buy, self.quantity, self.price)

class Exchange:
    # implement this!

    def __init__(self, initial_balance, accounts={}):
        """Initial Balance is the amount that each account should start with."""
        self.accounts = accounts
        self.trades = []
        self.balance = initial_balance
        self.pending = []

    def valid_price(self, trade1, trade2):
        """
        if trade1 is buy, returns trade1.price <= trade2.price
        if trade1 is sell, returns trade1.price >= trade2.price
        """
        if trade1.is_buy:
            return trade1.price >= trade2.price
        else:
            return trade1.price <=trade2.price

    def match_trade(self, new_trade):
        """Finds other trades that may meet the requirements of the new trade."""
        trade = new_trade
        matches = []
        for match in self.pending:
            if trade.quantity and match.is_buy != trade.is_buy and self.valid_price(trade, match):
                if match.quantity <= trade.quantity:
                    self.pending.remove(match)
                    matches.append(match)
                    trade.quantity -= match.quantity
                else:
                    matches.append(Trade(match.trader, match.is_buy, trade.quantity, match.price))
                    match.quantity -= trade.quantity
                    trade.quantity = 0
                    break
        return matches


    def add_trade(self, trade):
        """Adds a trade to the exchange (validation required)
        and returns a match if required. It is up to you on how you will
        handle representing trades. """
        if not isinstance(trade,Trade):
            raise ValueError("error: invalid trade format")
        if trade.trader not in self.accounts:
            self.accounts[trade.trader] = [self.balance, 0] #balance and quantity
            if not trade.is_buy:
                return "error: can't sell if you don't own it" #can't sell when you don't own anything
        cost = trade.price * trade.quantity
        if trade.is_buy:
            if self.accounts[trade.trader][0] < cost:
                return "error: insufficient funds" #could throw error as well
        else:
            if self.accounts[trade.trader][1] < trade.quantity:
                return "error: insufficient stocks"
        matches = self.match_trade(trade.copy())
        for match in matches:
            multiplier = -1 if match.is_buy else 1
            balance_change = multiplier * match.quantity * match.price
            quantity_change = multiplier * match.quantity
            self.accounts[match.trader][0] += balance_change
            self.accounts[match.trader][1] += -1 * quantity_change
            self.accounts[trade.trader][0] += -1 * balance_change
            self.accounts[trade.trader][1] += quantity_change
            trade.quantity -= match.quantity
        if trade.quantity > 0:
            self.pending.append(trade)

        return self.accounts

    


