#!/usr/bin/env python3
# table_formatter.py - Demonstrates the concept of inheritance in Python.

import sys
from abc import ABC, abstractmethod


def print_table(objects, colnames, formatter):
    """
    Make a nicely formatted table showing attributes from a list of objects.
    """
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")

    formatter.headings(colnames)
    for obj in objects:
        rowdata = [str(getattr(obj, colname)) for colname in colnames]
        formatter.row(rowdata)


class TablePrinter(object):
    def __init__(self, formatter):
        self.formatter = formatter

    def print_table(self, objects, colnames):
        """
        Make a nicely formatted table showing attributes from a list of objects.
        """
        self.formatter.headings(colnames)
        for obj in objects:
            rowdata = [str(getattr(obj, colname)) for colname in colnames]
            self.formatter.row(rowdata)


# Parent class
class TableFormatter(ABC):
    def __init__(self, outfile=None):
        if outfile == None:
            outfile = sys.stdout
        self.outfile = outfile

    def print_table(self, objects, colnames):
        """
        Make a nicely formatted table showing attributes from a list of objects.
        """
        self.headings(colnames)
        for obj in objects:
            rowdata = [str(getattr(obj, colname)) for colname in colnames]
            self.row(rowdata)

    # Serves as a design spec for making tables (use inheritance to customize).
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass


class TextTableFormatter(TableFormatter):
    def __init__(self, outfile=None, width=10):
        super().__init__(outfile)  # Parent initialization, i.e. TableFormatter class.
        self.width = width

    def headings(self, headers):
        for header in headers:
            print("{:>{}s}".format(header, self.width), end=" ", file=self.outfile)
        print(file=self.outfile)

    def row(self, rowdata):
        for item in rowdata:
            print("{:>{}s}".format(item, self.width), end=" ", file=self.outfile)
        print(file=self.outfile)


class CSVTableFormatter(object):
    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print("<tr>", end="")
        for h in headers:
            print("<th>{}</th>".format(h), end=" ")
        print("</tr>")

    def row(self, row):
        print("<tr>", end="")
        for d in rowdata:

            print("<td>{}</td>".format(d), end=" ")
        print("</tr>")


class QuotedMixin(object):
    def row(self, rowdata):
        quoted = ['"{}"'.format(d) for d in rowdata]
        super().row(quoted)
