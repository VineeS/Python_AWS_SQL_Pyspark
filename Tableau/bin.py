import pandas as pd

# Sample streaming data (replace this with your actual streamed data)
streamed_data = [
    {'value': 10},
    {'value': 20},
    {'value': 30},
    {'value': 40},
    {'value': 50}
]

# Convert streamed data to a pandas DataFrame
df = pd.DataFrame(streamed_data)

# Create bins using pandas
bins = [0, 25, 50, 75, 100]  # Define bin edges
labels = ['Bin 1', 'Bin 2', 'Bin 3', 'Bin 4']  # Define bin labels
df['bin'] = pd.cut(df['value'], bins=bins, labels=labels, right=False)

# Display the binned data
print(df)
