import yaml

def load_credentials():
    with open('credentials.yaml', 'r') as file:
        credentials = yaml.safe_load(file)
    return credentials
import pandas as pd
import pymysql
from sqlalchemy import create_engine
import yaml

class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.host = credentials['RDS_HOST']
        self.user = credentials['RDS_USER']
        self.password = credentials['RDS_PASSWORD']
        self.database = credentials['RDS_DATABASE']
        self.port = credentials['RDS_PORT']
        self.connection = None
        self.engine = None

    def establish_connection(self):
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print('Connected to the database.')
            return self.connection
        except Exception as e:
            print(f'Error connecting to the database: {str(e)}')
            return None

    def execute_query(self, query):
        if not self.connection:
            print('Not connected to the database. Call establish_connection() first.')
            return None

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(f'Error executing query: {str(e)}')
            return None

    def fetch_data(self, query):
        if not self.connection:
            print('Not connected to the database. Call establish_connection() first.')
            return None

        try:
            engine = create_engine(f'mysql+pymysql://{self.user}:{self.password}@{self.host}/{self.database}')
            data = pd.read_sql_query(query, engine)
            return data
        except Exception as e:
            print(f'Error fetching data: {str(e)}')
            return None

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print('Connection closed.')
class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.host = credentials['RDS_HOST']
        self.user = credentials['RDS_USER']
        self.password = credentials['RDS_PASSWORD']
        self.database = credentials['RDS_DATABASE']
        self.port = credentials['RDS_PORT']
        self.connection = None
        self.engine = None
    def init_engine(self):
        try:
            self.engine = create_engine(f'postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}')
            print('Engine initialized.')
        except Exception as e:
            print(f'Error initializing engine: {str(e)}')
    def extract_data(self):
        if not self.engine:
            print('Engine not initialized. Call init_engine() first.')
            return None

        try:
            query = 'SELECT * FROM loan_payments;'
            data = pd.read_sql_query(query, self.engine)
            print('Data extracted.')
            return data
        except Exception as e:
            print(f'Error extracting data: {str(e)}')
            return None
    def save_to_csv(self, data, filename='loan_payments.csv'):
        try:
            data.to_csv(filename, index=False)
            print(f'Data saved to {filename}.')
        except Exception as e:
            print(f'Error saving data to CSV: {str(e)}')
