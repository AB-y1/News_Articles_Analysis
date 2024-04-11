import pandas as pd

# Sample data (replace with your actual data)
data = {'product': ['pen', 'pencil', 'eraser', 'marker', 'pen', 'highlighter'],
        'price': [1.25, 0.75, 1.00, 2.50, 1.50, 2.00],
        'brand': ['BIC', None, 'Paper Mate', 'Sharpie', 'Pilot', 'Zebra']}
series = pd.Series(data)
print(data)
print(series)

# # Condition 1: Select items where "pen" is in the product name (case-insensitive)
# condition_1 = series['product'].str.lower().str.contains('pen')

# # Filter the Series based on condition 1
# filtered_series_1 = series[condition_1]

# # Print the result (products containing "pen")
# print("Products containing 'pen':")
# print(filtered_series_1)

# # Condition 2 (combining conditions): Select items with price > 1.0 and brand is not null
# condition_2 = (series['price'] > 1.0) & (series['brand'].notnull())

# # Filter the Series based on condition 2
# filtered_series_2 = series[condition_2]

# # Print the result (price > 1.0 and brand not null)
# print("\nProducts with price > 1.0 and brand not null:")
# print(filtered_series_2)
