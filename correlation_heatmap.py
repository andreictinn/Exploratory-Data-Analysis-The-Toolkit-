import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_correlation_heatmap(file_path):
    """
    Visualizes the correlation matrix heatmap for numerical columns in a cleaned DataFrame.

    Parameters:
    - file_path (str): The file path of the cleaned DataFrame CSV file.

    Returns:
    Decide based on the data which columns should be removed to improve future analysis 
    """
    # Load the cleaned DataFrame from the new CSV file
    df = pd.read_csv(file_path)

    # Select numerical columns
    numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns

    # Compute correlation matrix
    correlation_matrix = df[numerical_columns].corr()

    # Set a larger figure size
    plt.figure(figsize=(16, 14))

    # Plot heatmap
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.show()


if __name__ == "__main__":

# Example usage
 file_path ='D:/Coding/df_without_redundant_columns.csv'
visualize_correlation_heatmap(file_path)

# Optional usage - print a numerical version of the heatmap 
file_path = 'D:/Coding/df_cleaned_with_dropped_columns.csv'
# Select numerical columns
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns

# Compute correlation matrix
correlation_matrix = df[numerical_columns].corr()

# Print the correlation matrix
print(correlation_matrix)




 """
   Use the following to remove the chosen columns:
   
    """

# Columns to remove
columns_to_remove = ['funded_amount_inv', 'instalment']

# Drop the specified columns
df = df.drop(columns=columns_to_remove)

# Save the modified DataFrame to a new CSV file
output_path = 'D:/Coding/df_without_redundant_columns.csv'
df.to_csv(output_path, index=False)

print(f"DataFrame with redundant columns removed saved to {output_path}")
