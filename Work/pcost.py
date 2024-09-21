# pcost.py
#
# Exercise 1.27
import sys
import csv


def portfolio_cost(filename):
    cost_to_buy = 0
    # Read the file
    with open(filename, "rt") as file_obj:
        csv_iter = csv.reader(file_obj)
        headers = next(csv_iter)
        for line_num, line in enumerate(csv_iter):
            record = dict(zip(headers, line))
            try:
                # name, share, price = line.split(",")
                # cost_to_buy += float(price.strip()) * int(share)
                cost_to_buy += float(record['price']) * int(record['shares'])
            except ValueError as ve:
                print(f"Skipping, error found in line num {line_num}: {line}")
    return cost_to_buy


if len(sys.argv) == 2:
    filename = sys.argv[1]
    print(f"Total cost : {portfolio_cost(filename)}")
