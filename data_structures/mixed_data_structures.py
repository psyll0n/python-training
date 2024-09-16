# A complex dictionary data structure that contains the names 
# of several countries as `keys` and lists with city names as a `values` 

travel_log = {
    "France": ["Paris", "Lille", "Dijon" ],
    "Germany": ["Stuttgart", "Berlin", "Frankfurt"],
    "Spain": ["Madrid", "Barcelona", "Seville"],
}

# Access the 2nd item in the list with cities in the France key entry:
print(travel_log["France"][1])

# A nested list example
nested_list = ["A", "B", ["C", "D"]]

# Access the item at index `1` of the nested list with index `2`
print(nested_list[2][1])

# A complex dictionary that nests other dictionaries as its key, value pairs
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon" ],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Stuttgart", "Berlin", "Frankfurt"],
        "total_visits": 5
    },
    "Spain": {
        "cities_visited": ["Madrid", "Barcelona", "Seville"],
        "total_visits": 6
    },
}

# Access an entry in the `Germany` dictionary that exists in the `cities_visited` 
# list as 2nd entry...
print(travel_log["Germany"]["cities_visited"][1])