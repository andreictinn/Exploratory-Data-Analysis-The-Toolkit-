import pandas as pd

class DataFrameTransform:
    """
    A class providing methods for common DataFrame transformations.

    Methods:
    - null_percentage(df): Calculate the percentage of null values in each column of a DataFrame.
    - drop_columns(df, columns_to_drop): Drop specified columns from a DataFrame.
    - impute_mean(df, columns_to_impute): Impute missing values in specified columns with the mean of each column.
    - impute_median(df, columns_to_impute): Impute missing values in specified columns with the median of each column.
    """

    @staticmethod
    def null_percentage(df):
        """
        Calculate the percentage of null values in each column of a DataFrame.

        Parameters:
        - df (pd.DataFrame): The DataFrame to calculate null percentages for.

        Returns:
        - pd.Series: A Series containing null percentages for each column.
        """
        return df.isnull().mean() * 100

    @staticmethod
    def drop_columns(df, columns_to_drop):
        """
        Drop specified columns from a DataFrame.

        Parameters:
        - df (pd.DataFrame): The DataFrame from which columns will be dropped.
        - columns_to_drop (list): A list of column names to be dropped.

        Returns:
        - pd.DataFrame: The DataFrame with specified columns removed.
        """
        return df.drop(columns=columns_to_drop)

    @staticmethod
    def impute_mean(df, columns_to_impute):
        """
        Impute missing values in specified columns with the mean of each column.

        Parameters:
        - df (pd.DataFrame): The DataFrame to perform mean imputation on.
        - columns_to_impute (list): A list of column names for mean imputation.

        Returns:
        - pd.DataFrame: The DataFrame with missing values imputed using mean.
        """
        for column in columns_to_impute:
            df[column].fillna(df[column].mean(), inplace=True)
        return df

    @staticmethod
    def impute_median(df, columns_to_impute):
        """
        Impute missing values in specified columns with the median of each column.

        Parameters:
        - df (pd.DataFrame): The DataFrame to perform median imputation on.
        - columns_to_impute (list): A list of column names for median imputation.

        Returns:
        - pd.DataFrame: The DataFrame with missing values imputed using median.
        """
        for column in columns_to_impute:
            df[column].fillna(df[column].median(), inplace=True)
        return df

