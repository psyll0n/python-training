#! python3
# writeFormula.py - A function that uses an Excel formula to sum up the values in a range of cells.

import openpyxl


"""
The cells in A1 to A5 all have values asigned to them. The value in cell A6 is set to 
a formula that sums the values in A1 and A5. When the spreadsheet is opened in Excel,
cell A6 will display its value as 4535.
"""


def main():
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet["A1"] = 200
    sheet["A2"] = 300
    sheet["A3"] = 450
    sheet["A4"] = 1240
    sheet["A5"] = 2345
    sheet["A6"] = "=SUM(A1:A5)"

    wb.save("writeFormula.xlsx")


if __name__ == "__main__":
    main()
