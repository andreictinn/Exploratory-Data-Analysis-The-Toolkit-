import pandas as pd

def remove_outliers_and_save(input_file_path, output_file_path):
    """
    Remove outliers from a DataFrame, save the cleaned DataFrame, and print the Interquartile Range (IQR) for each numerical column.

    Parameters:
    - input_file_path (str): The file path of the CSV file containing the data.
    - output_file_path (str): The file path to save the cleaned DataFrame without outliers.

    Returns:
    - None
    """
    # Load the cleaned DataFrame
    df = pd.read_csv(input_file_path)

    # Select numerical columns
    numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns

    # Calculate IQR for each column
    Q1 = df[numerical_columns].quantile(0.25)
    Q3 = df[numerical_columns].quantile(0.75)
    IQR = Q3 - Q1

    # Define the lower and upper bounds for outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Filter out outliers
    df_no_outliers = df[~((df[numerical_columns] < lower_bound) | (df[numerical_columns] > upper_bound)).any(axis=1)]

    # Save the cleaned DataFrame without outliers
    df_no_outliers.to_csv(output_file_path, index=False)

    # Calculate IQR for each column in the cleaned data without outliers
    Q1_no_outliers = df_no_outliers[numerical_columns].quantile(0.25)
    Q3_no_outliers = df_no_outliers[numerical_columns].quantile(0.75)
    IQR_no_outliers = Q3_no_outliers - Q1_no_outliers

    # Print the IQR for each column
    print("Interquartile Range (IQR) for each column in the cleaned data without outliers:")
    print(IQR_no_outliers)

# Example usage
input_path = '...'
output_path = '...'
remove_outliers_and_save(input_path, output_path)
