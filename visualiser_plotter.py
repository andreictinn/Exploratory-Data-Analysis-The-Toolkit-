import seaborn as sns
import matplotlib.pyplot as plt

class Plotter:
    """
    A class providing methods for visualizing data using plots.

    Methods:
    - plot_null_distribution(df): Plot the distribution of null values in a DataFrame.

    """

    @staticmethod
    def plot_null_distribution(df):
        """
        Plot the distribution of null values in a DataFrame.

        Parameters:
        - df (pd.DataFrame): The DataFrame to visualize null values for.

        Returns:
        - None
        """
        plt.figure(figsize=(12, 6))
        sns.heatmap(df.isnull(), cmap='viridis', cbar=False, yticklabels=False)
        plt.title('Null Values Distribution')
        plt.show()



