import yaml
import pandas as pd
from sqlalchemy import create_engine

class RDSDatabaseConnector:
    @classmethod
    def load_credentials(cls):
        """
        Load database credentials from a YAML file.

        Returns:
        - dict: A dictionary containing database connection credentials.
        """
        with open('credentials.yaml', 'r') as file:
            credentials = yaml.safe_load(file)
        return credentials

    def __init__(self, credentials):
        """
        Initialize the RDSDatabaseConnector instance.

        Parameters:
        - credentials (dict): A dictionary containing database connection credentials.
        """
        self.credentials = credentials
        self.engine = self.create_engine()

    def create_engine(self):
        """
        Create a SQLAlchemy engine using the provided database credentials.

        Returns:
        - sqlalchemy.engine.Engine: An SQLAlchemy engine for connecting to the RDS database.
        """
        db_credentials = self.credentials
        connection_string = f"postgresql+psycopg2://{db_credentials['RDS_USER']}:{db_credentials['RDS_PASSWORD']}@{db_credentials['RDS_HOST']}:{db_credentials['RDS_PORT']}/{db_credentials['RDS_DATABASE']}"
        engine = create_engine(connection_string)
        return engine

    def extract_data(self):
        """
        Extract data from the RDS database.

        Returns:
        - pd.DataFrame: A DataFrame containing the extracted data from the RDS database.
        """
        # Assuming the table name is 'loan_payments'
        query = "SELECT * FROM loan_payments"
        data_frame = pd.read_sql_query(query, self.engine)
        return data_frame

    def save_data_to_csv(self, data_frame, file_path='loan_payments.csv'):
        """
        Save DataFrame to a CSV file.

        Parameters:
        - data_frame (pd.DataFrame): The DataFrame to be saved to a CSV file.
        - file_path (str): The file path for the CSV file (default is 'loan_payments.csv').

        Returns:
        - None
        """
        data_frame.to_csv(file_path, index=False)

# Load credentials from the credentials.yaml file
credentials = RDSDatabaseConnector.load_credentials()

# Create an instance of RDSDatabaseConnector
rds_connector = RDSDatabaseConnector(credentials)

# Extract data from the RDS database
data = rds_connector.extract_data()

# Save data to a CSV file
rds_connector.save_data_to_csv(data)

