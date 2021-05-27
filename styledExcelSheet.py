#! python3
# styledExcelSheet.py - Font styling in Excel with openpyxl.

"""
In this example, Font(size=24, italic=True) returns a Font object, which
is stored in italic24Font. The keyword arguments to Font(), size and italic,
configure the Font object’s style attributes. This Font object is then passed
into the Style(font=italic24Font) call, which returns the value you stored in
styleObj v. And when styleObj is assigned to the cell’s style attribute w, all
that font styling information gets applied to cell A1
"""


import openpyxl
from openpyxl.styles import Font, NamedStyle  


wb = openpyxl.Workbook()
sheet = wb['Sheet']
italic24Font = NamedStyle(name="italic24Font") 
italic24Font.font = Font(size=24, italic=True)
sheet['A1'].style = italic24Font
sheet['A1'] = 'Hello world!'


fontObj1 = Font(name='Times New Roman', bold=True)
styleObj1 = NamedStyle(name="styleObj1") 
styleObj1.font = fontObj1  
sheet['A2'].style = styleObj1 
sheet['A2'] = 'Bold Times New Roman'

fontObj2 = Font(size=24, italic=True)
styleObj2 = NamedStyle(name="StyleObj2") 
styleObj2.font = fontObj2  
sheet['B3'].style = styleObj2
sheet['B3'] = '24 pt Italic'


wb.save('styled_test.xlsx')