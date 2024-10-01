import pandas as pd

# Replace 'your_file.csv' with your actual CSV file path
csv_file_path = '/Users/davidgarcia/Downloads/productCATALOG.csv'

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Convert the DataFrame to JSON format
json_data = df.to_json(orient='records', indent=4)

# Save the JSON data to a file
with open('output.json', 'w') as json_file:
    json_file.write(json_data)

print('CSV has been successfully converted to JSON!')
