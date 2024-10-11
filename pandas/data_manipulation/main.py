import pandas

# import csv


# Accessing and reading a file.
# with open("./weather_data.csv") as file:
#     data = file.readlines()
#     print(data)


# Reading the second row in CSV file and adding the values to the `temperatures` list
# with open("./weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)


# Alternatively, the csv.DictReader can be used for the same purpose
# with open("./weather_data.csv") as file:
#     data = csv.DictReader(file, delimiter=",")
#     temperatures = []
#     for row in data:
#         temperatures.append(int(row['temp']))
#
# print(temperatures)

print(
    "====== The Pandas module can also be used for easy access to data in CSV files. ======="
)

# The Pandas module can also be used for easy access to data in CSV files.
data = pandas.read_csv("weather_data.csv")
print(data)

print("======= Access the data values in the 2nd row of the CSV file. ========")

# Access the data values in the 2nd row of the CSV file.
print(data["temp"])

print("======== Check what is the type of the data in the 2nd row. ==========")

# Check what is the type of the data in the 2nd row
print(type(data["temp"]))

print(
    "====== Alternatively, the following syntax can be used to achieve the same result. ========"
)

# Alternatively, the following syntax can be used to achieve the same result.
# The column name should be typed EXACTLY as it is in the CSV file.
print(data.condition)

print("============ Search for and get specific data in a row. =============")

# Search for and get specific data in a row.
print(data[data.day == "Monday"])

print("======== Create a list from the 2nd row in `data`. ========")

# Create a list from the 2nd row in `data`.
temp_list = data["temp"].to_list()
print(temp_list)

print(
    "====== Calculate the average temperature by using the `temp_list` dict created above. ========"
)

# Calculate the average temperature by using the `temp_list` dict created above.
average_temp = sum(temp_list) / len(temp_list)
print(average_temp)

print("============ Create a dictionary out of the CSV file data. =================")

# Create a dictionary out of the CSV file data.
data_dict = data.to_dict()
print(data_dict)

print(
    "===== Calculate the average temperature by using Pandas `.mean()` built-in method. ======="
)

# Calculate the average temperature by using Pandas `.mean()` built-in method.
print(data["temp"].mean())

print("================= Get the highest value in a data series. ==================")

# Get the highest value in a data series
print(data["temp"].max())

print("======= Access the row with the highest value in a data series. ==============")

# Access the row with the highest value in a data series
print(data[data.temp == data.temp.max()])

print(
    "========= Find and convert the first value in the series in the column 'Monday'. =========="
)
print("======== Convert the temperature from Celsius to Fahrenheit. =========")
# Find and convert the first value in the series in the column "Monday".
# Convert the temperature from Celsius to Fahrenheit
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9 / 5 + 32
print(monday_temp_F)

print("====== Create a new dataframe from scratch by using Pandas. =========")

# Create a dataframe from scratch by using Pandas
data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}

data = pandas.DataFrame(data_dict)
print(data)

print("====== Create a CSV file out of the newly created Data frame. =========")

# Create a CSV file out of the newly created Data frame.
data.to_csv("new_data.csv")

print("================================================================")
