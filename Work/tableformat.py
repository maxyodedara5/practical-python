# Table formatter class

from typing import List

class TableFormatter():
    def headings(self, headers):
        """Emit the table headings"""
        raise NotImplementedError()
    
    def row(self, rowdata):
        """Emit a single row of table data"""
        raise NotImplementedError()



class TextTableFormatter(TableFormatter):
    """Emit a table in plain text format"""
    def headings(self, headers):
        for header in headers:
            print(f"{header:>10s}", end=" ")
        print()
        print(('-'*10 + ' ') * len(headers))

    def row(self, row_data):
        for data in row_data:
            print(f"{data:>10s}", end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    """Emit a table in plain text format"""
    def headings(self, headers):
        print(",".join(headers))

    def row(self, row_data):
        # for data in row_data:
        print(",".join(row_data))

class HTMLTableFormatter(TableFormatter):
    """Emit a table in HTML format"""
    def headings(self, headers):
        print("<tr>", end="")
        for header in headers:
            print(f"<th>{header}</th>", end="")
        print("</tr>")
    
    def row(self, row_data):
        print("<tr>", end="")
        for data in row_data:
            print(f"<td>{data}</td>", end="")
        print("</tr>")

def create_formatter(format_type):
    """Creates the formatter based on the passed format type
    txt, csv, html"""
    if format_type == "txt":
        return TextTableFormatter()
    elif format_type == "csv":
        return CSVTableFormatter()
    elif format_type == "html":
        return HTMLTableFormatter()
    else:
        raise FormtError(f"Unknown format {format_type}")


def print_table(portfolio: List[object], columns: List[str], formatter: TableFormatter):
    formatter.headings(columns)

    for obj in portfolio:
        row_data = []
        for col in columns:
            if hasattr(obj, col):
                row_data.append(str(getattr(obj, col)))
        formatter.row(row_data)


class FormtError(Exception):
    pass