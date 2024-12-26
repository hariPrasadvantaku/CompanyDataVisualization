import pandas as pd  

# Load the CSV  
data = pd.read_csv("C:/Users/ravi kumar nirujogi/Desktop/Stock Dashboard/dump.csv")  

# Convert to JSON  
json_path = "C:/Users/ravi kumar nirujogi/Desktop/Stock Dashboard/data.json"  
data.to_json(json_path, orient='records')  

print(f"Data successfully converted to JSON and saved to {json_path}")
