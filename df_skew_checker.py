import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_skewness(dataset_path):
    """
    Load a dataset, calculate skewness for numerical columns, and create a bar plot to visualize skewness values.

    Parameters:
    - dataset_path (str): The file path of the CSV file containing the dataset.

    Returns:
    - None
    """
    # Load the dataset
    df = pd.read_csv(dataset_path)

    # Calculate skewness for numerical columns
    numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
    skewness_values = df[numerical_columns].apply(lambda x: x.skew())

    # Create a bar plot for skewness
    plt.figure(figsize=(12, 6))
    sns.barplot(x=skewness_values.index, y=skewness_values)
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.title('Skewness of Numerical Columns')
    plt.xlabel('Numerical Columns')
    plt.ylabel('Skewness')
    plt.show()

# Example usage
dataset_path = 'D:/Coding/df_no_outliers.csv'
plot_skewness(dataset_path)
