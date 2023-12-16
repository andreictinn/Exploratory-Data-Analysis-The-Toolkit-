import pandas as pd
import pymysql
from sqlalchemy import create_engine
import yaml
import logging

class RDSDatabaseConnector:
    def __init__(self, credentials):
        """
        Initialize RDSDatabaseConnector.

        Parameters:
            credentials (dict): Dictionary containing database credentials.
        """
        self.host = credentials['RDS_HOST']
        self.user = credentials['RDS_USER']
        self.password = credentials['RDS_PASSWORD']
        self.database = credentials['RDS_DATABASE']
        self.port = credentials['RDS_PORT']
        self.connection = None
        self.engine = None
        self.logger = logging.getLogger(__name__)

    def initialize(self):
        """
        Initialize database connection and engine.
        """
        try:
            # Establish connection
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.logger.info('Connected to the database.')

            # Initialize engine
            self.engine = create_engine(f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}')
            self.logger.info('Engine initialized.')

        except pymysql.MySQLError as e:
            self.logger.error(f'Error initializing: {str(e)}')

    def execute_query(self, query):
        """
        Execute SQL query.

        Parameters:
            query (str): SQL query.

        Returns:
            result (list or None): Result of the query.
        """
        if not self.connection:
            self.logger.warning('Not connected to the database. Call initialize() first.')
            return None

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result

        except pymysql.MySQLError as e:
            self.logger.error(f'Error executing query: {str(e)}')
            return None

    def fetch_data(self, query):
        """
        Fetch data from the database.

        Parameters:
            query (str): SQL query.

        Returns:
            data (pd.DataFrame or None): DataFrame containing the fetched data.
        """
        if not self.engine:
            self.logger.warning('Engine not initialized. Call initialize() first.')
            return None

        try:
            data = pd.read_sql_query(query, self.engine)
            self.logger.info('Data extracted.')
            return data

        except pd.errors.EmptyDataError:
            self.logger.warning('No data extracted. The query returned an empty result set.')
            return None

        except Exception as e:
            self.logger.error(f'Error fetching data: {str(e)}')
            return None

    def close_connection(self):
        """
        Close the database connection.
        """
        if self.connection:
            self.connection.close()
            self.logger.info('Connection closed.')

    def save_to_csv(self, data, filename='loan_payments.csv'):
        """
        Save DataFrame to a CSV file.

        Parameters:
            data (pd.DataFrame): DataFrame to be saved.
            filename (str): Name of the CSV file.

        Returns:
            None
        """
        try:
            data.to_csv(filename, index=False)
            self.logger.info(f'Data saved to {filename}.')

        except Exception as e:
            self.logger.error(f'Error saving data to CSV: {str(e)}')


def load_local_data(file_path="loan_payments.csv"):
    """
    Load data from a local CSV file into a Pandas DataFrame.

    Parameters:
        file_path (str): Path to the CSV file.

    Returns:
        data (pd.DataFrame or None): DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        logging.info(f"Data loaded successfully. Shape: {data.shape}")
        logging.info("Sample of the data:")
        logging.info(data.head())
        return data

    except pd.errors.EmptyDataError:
        logging.warning('No data loaded. The CSV file is empty.')
        return None

    except Exception as e:
        logging.error(f"Error loading data: {str(e)}")
        return None

