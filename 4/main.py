import pandas as pd
json_file = 'Sample-employee-JSON-data.json'
data = pd.read_json(json_file)
csv_file = 'Sample-employee-JSON-data.csv'
data.to_csv(csv_file, index=False)
