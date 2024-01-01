import pandas as pd

def load_csv_file(file_path):
    """
    Load a CSV file into a DataFrame.

    Parameters:
    - file_path (str): The path to the CSV file.

    Returns:
    - pd.DataFrame: The DataFrame containing the CSV data.
    """
    df = pd.read_csv(file_path)
    return df

def display_first_few_lines(df, num_lines=5):
    """
    Display the first few lines of a DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame to display.
    - num_lines (int): The number of lines to display. Default is 5.
    """
    print(f"First {num_lines} lines of the DataFrame:")
    print(df.head(num_lines))

def display_column_names_and_types(df):
    """
    Extract and display column names with their data types from a DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame to extract column information from.
    """
    print("\nColumn names with data types:")
    print(df.dtypes)

def print_entire_dataframe(df):
    """
    Print the entire DataFrame (not recommended for large files).

    Parameters:
    - df (pd.DataFrame): The DataFrame to print.
    """
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    print(df)
    pd.reset_option('display.max_columns')
    pd.reset_option('display.max_rows')

# Load the CSV file
file_path = '...'
df = load_csv_file(file_path)

# Display the first few lines of the CSV file
display_first_few_lines(df)

# Extract and display column names with data types
display_column_names_and_types(df)

# Optional: Print the entire DataFrame (not recommended for large files)
# print_entire_dataframe(df)
