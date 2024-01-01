import pandas as pd

def load_and_clean_data(file_path):
    """
    Load a CSV file into a pandas DataFrame and perform date-related cleaning.

    Parameters:
    - file_path : The file path of the CSV file to be loaded.
    - columns to be transformed 

    Returns:
    - pd.DataFrame: A cleaned DataFrame with date columns converted to datetime and year extracted.
    """
    # Load DataFrame from CSV file
    df = pd.read_csv(file_path)

    # List of columns containing date information
    date_columns = ['issue_date', 'earliest_credit_line', 'last_payment_date', 'next_payment_date', 'last_credit_pull_date']

    # Convert date columns to datetime and extract the year
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce').dt.year

    return df


def save_cleaned_data(df, output_file_path):
    """
    Save a cleaned DataFrame to a new CSV file.

    Parameters:
    - df (pd.DataFrame): The cleaned DataFrame to be saved.
    - output_file_path (str): The file path for the new CSV file.

    Returns:
    - None
    """
    df.to_csv(output_file_path, index=False)


# Example Usage:
# Replace 'your_file_path.csv' with the actual file path
file_path = '...'

# Load and clean the data
df = load_and_clean_data(file_path)

# Save the cleaned DataFrame to a new CSV file (replace 'file_path' with the actual output file path)
save_cleaned_data(df, 'output_file_path.csv')
