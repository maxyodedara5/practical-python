# pcost.py
#
# Exercise 1.27
import sys
import report
from stock import Stock
from portfolio import Portfolio

def portfolio_cost(filename):
    """Calculates the Portfolio Cost for provided file"""
    cost_to_buy = 0
    records = report.read_portfolio(filename)

    Stocks = []
    for line_num, record in enumerate(records):
        try:
            # name, share, price = line.split(",")
            # cost_to_buy += float(price.strip()) * int(share)
            # cost_to_buy += float(record.price) * int(record.shares)
            current_stock = Stock(record.name, record.shares, record.price)
            Stocks.append(current_stock)
        except ValueError as ve:
            print(f"Skipping, error found in line num {line_num}: {record}")
    
    portfolio = Portfolio(Stocks)
    return portfolio.total_cost


def main(filename):
    print(f"Total cost : {portfolio_cost(filename)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <portfolio_file>")
        sys.exit()
    filename = sys.argv[1]
    main(filename)

# print(portfolio_cost('Data/portfolio.csv'))