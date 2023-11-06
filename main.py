import pandas as pd
import json

# Read the JSON from the file
with open('tele.json', 'r') as file:
    data = json.load(file)
print(data)
# Create a dictionary with the `ts` values as keys
result = {}
fields = data.keys()
print(fields)
for field in fields:
    for item in data[field]:
        ts = item['ts']
        value = item['value']

        if ts not in result:
            result[ts] = {}

        result[ts][field] = value

# Convert the dictionary to a Pandas DataFrame
df = pd.DataFrame.from_dict(result, orient='index')
print(df)
df.reset_index(inplace=True)
df.rename(columns={'index': 'ts'}, inplace=True)

# Convert the `ts` values to a human-readable date format
df['date'] = pd.to_datetime(df['ts'], unit='ms').dt.strftime('%Y-%m-%d %H:%M:%S')

# Sorting dataframe based on timestamp
df.sort_values(by='ts', inplace=True, ascending=False)
# Save to CSV
df.to_csv('output8.csv', index=False)