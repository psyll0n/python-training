import pandas as pd  # Use standard alias 'pd' for Pandas

# Load the squirrel data CSV into a Pandas DataFrame
data = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Specify the column that contains the fur color information
column_name = "Primary Fur Color"

# Count occurrences of specific fur colors
gray = data[column_name].str.contains("Gray", na=False).sum()      # Count squirrels with Gray fur
black = data[column_name].str.contains("Black", na=False).sum()    # Count squirrels with Black fur
red = data[column_name].str.contains("Cinnamon", na=False).sum()   # Count squirrels with Cinnamon fur (red-colored)

# Create a dictionary with color names as keys and corresponding counts as values
squirrel_count_by_fur_color = {
    "Color": ["Gray", "Black", "Cinnamon"],  # List of colors
    "Count": [gray, black, red]              # Corresponding counts
}

# Convert the dictionary into a DataFrame
squirrel_count = pd.DataFrame(squirrel_count_by_fur_color)

# Print the resulting DataFrame to the console
print(squirrel_count)

# Save the DataFrame to a CSV file
squirrel_count.to_csv("squirrel_count_by_fur_color.csv", index=False)  # index=False to avoid saving index as an extra column
