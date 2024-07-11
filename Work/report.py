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
        for rows in csv_iter:
            try:
                # portfolio_items.append((rows[0], int(rows[1]), float(rows[2]))) # for tuples
                current_dict = {
                    'name' : rows[0],
                    'shares' : int(rows[1]),
                    'price' : float(rows[2])
                }
                portfolio_items.append(current_dict)
            except ValueError as ve:
                print(f"Skipping, error found in line: {rows}")
    return portfolio_items


def read_prices(filename):
    """ Reads portfolio from a csv file format to be NAMES,PRICE """
    prices_dict = {}
    with open(filename, "rt") as file_obj:
        csv_iter = csv.reader(file_obj)
        headers_str = next(csv_iter)
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

