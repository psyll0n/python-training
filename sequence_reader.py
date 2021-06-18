#! python3
# sequence_reader.py - Auxiliary python script used to read the sequence of numbers generated with recaman_sequence.py.

from os import name
import sys

def read_series(filename):
    try:
        f = open(filename, mode='rt', encoding='utf-8')
        series = []
        for line in f:
            a = int(line.strip())
            series.append(a)
    finally:
        f.close
    return series

        
def main(filename):
    series = read_series(filename)
    print(series)
    
if __name__ == '__main__':
    read_series()
    
    