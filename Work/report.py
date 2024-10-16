# report.py
#
# Exercise 2.4
import csv
from fileparse import parse_csv
import sys
from stock import Stock
from typing import List,Any,Iterable
import tableformat
from portfolio import Portfolio

def read_portfolio(filename):
    """ Reads portfolio provided for file """
    with open(filename) as file:
        portfolio_items = parse_csv(file,
                                    select=['name','shares','price'],
                                    types=[str,int,float])

    portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portfolio_items ]
    return Portfolio(portfolio)

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
        originial_value += value.shares * value.price
        if value.price in prices:
            current_value += prices[value.name] * value.shares

    return current_value - originial_value


def make_report(portfolio, prices):
    report_items = []
    for value in portfolio:
        report_items.append((value.name,
                             value.shares,
                             value.price,
                             prices[value.name] - value.price))
        
    return report_items


def print_report(report_items, formatter):
    """Print a nicely formatted table from list of (name,shares,price,change) Tuples"""

    headers = ["Name", "Shares", "Price", "Change"]
    formatter.headings(headers)
    for name, shares, price, change in report_items:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:>0.2f}']
        formatter.row(rowdata)

    #TODO : Figure out a way to add $ symbol to price column #2.3 #2.12 


def portfolio_report(portfolio_filename, prices_filename, format_type="txt"):
    """
    Creates the report
    arg1: portfolio filename
    arg2: prices filename
    """
    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    # Create report data
    report_items = make_report(portfolio, prices)

    # Print report
    formatter = tableformat.create_formatter(format_type)
    print_report(report_items, formatter)


# portfolio_report('Data/portfolio.csv', 'Data/prices.csv', "txt")

def main(portfolio_file, prices_file, format_type="txt"):
    portfolio_report(portfolio_file, prices_file, format_type)

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 3:
        print("Usage: report.py <portfolio_file> <prices_file>")
        sys.exit()
    portfolio_file = args[1]
    prices_file = args[2]
    if args[3]:
        format_type = args[3]
        main(portfolio_file, prices_file, format_type)
    else:
        main(portfolio_file, prices_file)