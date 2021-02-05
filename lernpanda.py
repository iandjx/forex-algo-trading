import pandas as pd

# Get rid of $ and , in the SAL-RATE, then convert it to a float
def money_to_float(money_str):
    return float(money_str.replace("$","").replace(",",""))

df['SAL-RATE'].apply(money_to_float)

# Save the result in a new column
df['salary'] = df['SAL-RATE'].apply(money_to_float)


# Create a dataframe from a list of dictionaries
rectangles = [
    { 'height': 40, 'width': 10 },
    { 'height': 20, 'width': 9 },
    { 'height': 3.4, 'width': 4 }
]

rectangles_df = pd.DataFrame(rectangles)
rectangles_df


# Use the height and width to calculate the area
def calculate_area(row):
    return row['height'] * row['width']

rectangles_df.apply(calculate_area, axis=1)

# Use .apply to save the new column if we'd like
rectangles_df['area'] = rectangles_df.apply(calculate_area, axis=1)
rectangles_df