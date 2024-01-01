import pandas as pd
from visualiser_plotter import Plotter
from data_transform import DataFrameTransform

def clean_and_visualize_data(file_path):
    """
    Load the DataFrame, visualize null distribution, and clean the data by dropping columns with more than 60% null values.

    Parameters:
    - file_path (str): The file path of the CSV file containing the data.

    Returns:
    pd.DataFrame: The cleaned DataFrame.
    list: A list of dropped columns.
    """
    # Load the cleaned DataFrame
    df = pd.read_csv(file_path)

    # Step 1: Initialize the Plotter and DataFrameTransform classes
    plotter = Plotter()
    transformer = DataFrameTransform()

    # Step 2: Use the Plotter to visualize the null distribution
    plotter.plot_null_distribution(df)

    # Step 3: Check for null values in each column and decide which columns to drop
    null_summary = transformer.null_percentage(df)
    columns_to_drop = null_summary[null_summary > 60].index

    # Drop columns with more than 60% null values
    df = transformer.drop_columns(df, columns_to_drop)

    # Display the DataFrame after dropping columns
    print("DataFrame after dropping columns:")
    print(df)

    # Save the DataFrame to a new CSV file
    cleaned_file_path = file_path.replace('.csv', '_cleaned_with_dropped_columns.csv')
    df.to_csv(cleaned_file_path, index=False)
    print(f"Cleaned DataFrame saved to: {cleaned_file_path}")

    return df, list(columns_to_drop)

# Example usage
file_path = '...'
cleaned_df, dropped_columns = clean_and_visualize_data(file_path)

# Display the dropped columns
print("Dropped Columns:")
print(dropped_columns)
