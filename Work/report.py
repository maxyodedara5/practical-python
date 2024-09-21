# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    """ Reads portfolio from a csv file format to be NAMES,SHARES,PRICE """
    portfolio_items = []
    # Read the file
    with open(filename, "rt") as file_obj:
        csv_iter = csv.reader(file_obj)
        headers_str = next(csv_iter)
        for row_num,rows in enumerate(csv_iter):
            try:
                current_dict = dict(zip(headers_str, rows))
                current_dict['shares'] = int(current_dict['shares'])
                current_dict['price'] = float(current_dict['price'])
                portfolio_items.append(current_dict)
            except ValueError as ve:
                print(f"Skipping, error found in line num {row_num}: {rows}")
    return portfolio_items


def read_prices(filename):
    """ Reads portfolio from a csv file format to be NAMES,PRICE """
    prices_dict = {}
    with open(filename, "rt") as file_obj:
        csv_iter = csv.reader(file_obj)
        for rows in csv_iter:
            if rows:
                prices_dict[rows[0]] = float(rows[1])
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


# portfolio = read_portfolio('Data/portfolio.csv')
# prices = read_prices('Data/prices.csv')
# report_items = make_report(portfolio, prices)
# print_report(report_items)

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