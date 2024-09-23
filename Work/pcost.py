# pcost.py
#
# Exercise 1.27
import sys
import csv
import report

def portfolio_cost(filename):
    """Calculates the Portfolio Cost for provided file"""
    cost_to_buy = 0
    records = report.read_portfolio(filename)
    for line_num, record in enumerate(records):
        try:
            # name, share, price = line.split(",")
            # cost_to_buy += float(price.strip()) * int(share)
            cost_to_buy += float(record['price']) * int(record['shares'])
        except ValueError as ve:
            print(f"Skipping, error found in line num {line_num}: {record}")
    
    return cost_to_buy


if len(sys.argv) == 2:
    filename = sys.argv[1]
    print(f"Total cost : {portfolio_cost(filename)}")
