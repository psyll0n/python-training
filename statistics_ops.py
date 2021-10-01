#!/usr/bin/env python3
# Using Python static functions.

import array
import csv
import statistics


# Simple statistics operations.
sample_data1 = [1, 3, 5, 7]
sample_data2 = [2, 3, 5, 3, 5, 3, 2, 6, 5, 4, 3]

# TODO: Use the mean function - calculates the average value.
# print(statistics.mean(sample_data1))


# TODO: Use the different median functions.
print(statistics.median(sample_data1))
print(statistics.median_low(sample_data1))
print(statistics.median_high(sample_data1))

# TODO: The mode function indicates which data item occurs most frequently.
print(statistics.mode(sample_data2))


# Read data from a CSV file and calculate statistics.
def readData():
    with open("StockQuotes.csv") as dataFile:
        data = array.array("f", [])

        reader = csv.reader(dataFile)
        currentLine = 0

        for row in reader:
            if currentLine == 0:
                pass  # This is the header row.
            else:
                # Get the closing value from column 4.
                item = float(row[4])
                data.append(item)
            currentLine += 1
        print(f"Read {currentLine+1} rows of data.")
        return data


def calcStats():
    # Read the data from the CSV file.
    data = readData()

    # TODO: Calculate interesting data points.
    data_mean = round(statistics.mean(data), 2)
    data_med = round(statistics.median(data), 2)
    data_std = round(statistics.stdev(data), 2)
    data_var = round(statistics.variance(data), 2)

    print("Mean: ", data_mean)
    print("Median: ", data_med)
    print("Standard Deviation: ", data_std)
    print("Variance: ", data_var)


# TODO: Calculate stats values from a CSV file of data.
calcStats()
