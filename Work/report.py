# report.py
#
# Exercise 2.4
import csv
from fileparse import parse_csv
import sys


def read_portfolio(filename):
    """ Reads portfolio provided for file """
    with open(filename) as file:
        portfolio_items = parse_csv(file,types=[str,int,float])

    return portfolio_items


def read_prices(filename):
    """ Reads portfolio from a csv file format to be NAMES,PRICE """
    with open(filename) as file:
        price_items = parse_csv(file,
                                has_headers=False,
                                types=[str,float])
    prices_dict = dict(price_items)
    return prices_dict



def loss_gain_computation(portfolio_file, prices_file):
    """ Gives the loss or gain value from the portfolio and prices file """
    portfolio_items = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    originial_value = 0 
    current_value = 0
    for value in portfolio_items:
        originial_value += value['shares'] * value['price']
        if value['name'] in prices:
            current_value += prices[value['name']] * value['shares']

    return current_value - originial_value

def make_report(portfolio, prices):
    report_items = []
    for value in portfolio:
        report_items.append((value['name'],
                             value['shares'],
                             value['price'],
                             prices[value['name']] - value['price']))
        
    return report_items

def print_report(report_items):
    headers = ("Name", "Shares", "Price", "Change")
    print("%10s %10s %10s %10s" % headers)
    print('{:-<10} {:-<10} {:-<10} {:-<10}'.format(' ', ' ', ' ', ' '))
    for name, shares, price, change in report_items:
        print(f"{name:>10} {shares:>10} {price:>10.2f} {change:>10.2f}")
    #TODO : Figure out a way to add $ symbol to price column #2.3 #2.12 


def portfolio_report(portfolio_filename, prices_filename):
    """
    Creates the report
    arg1: portfolio filename
    arg2: prices filename
    """
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report_items = make_report(portfolio, prices)
    print_report(report_items)


# portfolio_report('Data/portfolio.csv', 'Data/prices.csv')

def main(portfolio_file, prices_file):
    portfolio_report(portfolio_file, prices_file)

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        print("Usage: report.py <portfolio_file> <prices_file>")
        sys.exit()
    portfolio_file = args[1]
    prices_file = args[2]
    main(portfolio_file, prices_file)