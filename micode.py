import pandas as pd

def is_column_present(file_path, target_column):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Check if the target column is present in the DataFrame's columns
    return target_column in df.columns

# Example usage
file_path = 'your_csv_file.csv'  # Replace with the path to your CSV file
target_column_name = 'your_target_column'

result = is_column_present(file_path, target_column_name)

if result:
    print(f"The column '{target_column_name}' is present in the CSV file.")
else:
    print(f"The column '{target_column_name}' is not present in the CSV file.")
