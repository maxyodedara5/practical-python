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
        headers_str = next(csv_iter)
        for line in file_obj:
            try:
                name, share, price = line.split(",")
                cost_to_buy += float(price.strip()) * int(share)
            except ValueError as ve:
                print(f"Skipping, error found in line: {line}")
    return cost_to_buy


if len(sys.argv) == 2:
    filename = sys.argv[1]
    print(f"Total cost : {portfolio_cost(filename)}")
