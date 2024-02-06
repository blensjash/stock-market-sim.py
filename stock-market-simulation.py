# Redefining the code after reset

# Define a function to simulate fetching stock data
def get_stock_price(stock_symbol, date):
    # Simulated stock prices
    stock_prices = {
        "AAPL": {"2024-02-06": 150.00},
        "GOOGL": {"2024-02-06": 2800.00},
        "MSFT": {"2024-02-06": 300.00}
    }
    # Return the price if available, otherwise None
    return stock_prices.get(stock_symbol, {}).get(date, None)


# Define class to represent the user's portfolio
class Portfolio:
    def __init__(self):
        self.holdings = {}  # Dictionary to hold stock_symbol: quantity
        self.cash = 10000  # Starting cash, can be modified to simulate different scenarios

    def buy_stock(self, stock_symbol, quantity, date):
        stock_price = get_stock_price(stock_symbol, date)
        if stock_price is None:
            return "Stock price not available."

        total_cost = stock_price * quantity
        if self.cash >= total_cost:
            self.holdings[stock_symbol] = self.holdings.get(stock_symbol, 0) + quantity
            self.cash -= total_cost
            return f"Bought {quantity} shares of {stock_symbol}."
        else:
            return "Insufficient funds."

    def sell_stock(self, stock_symbol, quantity, date):
        stock_price = get_stock_price(stock_symbol, date)
        if stock_price is None:
            return "Stock price not available."

        if self.holdings.get(stock_symbol, 0) >= quantity:
            self.holdings[stock_symbol] -= quantity
            self.cash += stock_price * quantity
            return f"Sold {quantity} shares of {stock_symbol}."
        else:
            return "Not enough shares to sell."

    def get_portfolio_value(self, date):
        total_value = self.cash
        for stock_symbol, quantity in self.holdings.items():
            stock_price = get_stock_price(stock_symbol, date)
            if stock_price is not None:
                total_value += stock_price * quantity
        return total_value

    def display_portfolio(self):
        print("Portfolio:")
        for stock, quantity in self.holdings.items():
            print(f"{stock}: {quantity} shares")
        print(f"Cash: ${self.cash:.2f}")


my_portfolio = Portfolio()

print(my_portfolio.buy_stock('AAPL', 10, '2024-02-06'))
print(my_portfolio.sell_stock('AAPL', 5, '2024-02-06'))


my_portfolio.display_portfolio()


print(f"Total portfolio value: ${my_portfolio.get_portfolio_value('2024-02-06'):.2f}")
