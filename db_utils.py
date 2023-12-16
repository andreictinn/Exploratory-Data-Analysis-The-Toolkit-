import pandas as pd
import pymysql
from sqlalchemy import create_engine
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

    def _establish_connection(self):
        """
        Establish database connection.
        """
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.logger.info('Connected to the database.')
        except pymysql.MySQLError as e:
            self.logger.error(f'Error establishing connection: {str(e)}')
            raise  # Reraise the exception

    def _handle_query_execution(self, query):
        """
        Execute SQL query.

        Parameters:
            query (str): SQL query.

        Returns:
            result (list or None): Result of the query.
        """
        if not self.connection:
            self.logger.warning('Not connected to the database. Call _establish_connection() first.')
            return None

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except pymysql.MySQLError as e:
            self.logger.error(f'Error executing query: {str(e)}')
            raise  # Reraise the exception

    def _handle_data_fetching(self, query):
        """
        Fetch data from the database.

        Parameters:
            query (str): SQL query.

        Returns:
            data (pd.DataFrame or None): DataFrame containing the fetched data.
        """
        if not self.engine:
            self.logger.warning('Engine not initialized. Call _establish_connection() first.')
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
            raise  # Reraise the exception

    def establish_and_fetch(self, query):
        """
        Establish connection, execute query, and fetch data.

        Parameters:
            query (str): SQL query.

        Returns:
            result (list or None): Result of the query.
            data (pd.DataFrame or None): DataFrame containing the fetched data.
        """
        try:
            self._establish_connection()
            result = self._handle_query_execution(query)
            data = self._handle_data_fetching(query)
            return result, data
        finally:
            self.close_connection()

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

if __name__ == "__main__":
    


