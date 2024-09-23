# fileparse.py
#
# Exercise 3.3
import csv
from typing import List,Any
from pprint import pprint

def parse_csv(filename: str, 
              select: List[str] = [],
              types: List[Any] = [],
              has_headers: bool = True,
              delimiter: str = ',',
              silence_errors: bool = True):
    """Parse a CSV file into list of records\n
    filename : The name of the csv file to be parsed\n
    select[Optional]        : List of columns you want to select from the csv file\n
    types[Optional]         : List of types for data to be converted\n
    has_headers[Optional]   : Flag for headers\n
    delimiter[Optional]     : Alternative delimiter, if file type different than CSV\n
    """

    if select and not has_headers:
        raise RuntimeError("Select argument requires column headers")

    with open(filename) as file:

        rows = csv.reader(file, delimiter=delimiter)
        records = []
        if not has_headers:
            # If headers not provided we can add our own headers 
            # When providing data, remove custom headers
            row_val = next(rows)
            num_headers = len(row_val)
            headers = ["col"+str(num) for num in range(num_headers)]
            record = dict(zip(headers, row_val))
            records.append(record)
        else:
            headers = next(rows)

        for row in rows:
            if not row:
                continue
            record = dict(zip(headers, row))
            records.append(record)

        # Change records if selective columns are needed
        not_needed_columns = list(set(headers) - set(select))
        selective_records = []
        if select:
            for record in records:
                modified_record = record
                for col in not_needed_columns:
                    modified_record.pop(col)
                selective_records.append(modified_record)

            records = selective_records
        else:
            select = headers

        # Type conversion
        if types:
            type_dict = dict(zip(select, types))
            converted_records = []

            for record_num, record in enumerate(records, start=1):
                conv_record = {}
                try:
                    for col_name, value in record.items():
                        conv_record[col_name] = type_dict[col_name](value)
                    converted_records.append(conv_record)
                    records = converted_records
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {record_num} : Cannot convert {record}")
                        print(f"Error at row num {record_num}: {e}")

        # If no headers, provide only values
        if not has_headers:
            tuple_records = []
            for record in records:
                tuple_records.append(tuple(record.values()))
            records = tuple_records

    return records

# portfolio = parse_csv('Data/missing.csv', types=[str,int,float], silence_errors=False)
# pprint(portfolio)