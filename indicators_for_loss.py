import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_loan_indicators(file_path):
    """
    Analyzes loan indicators to identify factors contributing to loans not being paid off.

    Parameters:
    - file_path (str): The file path of the CSV file containing the loan data.

    Returns:
    None
    """
    # Load the DataFrame
    df = pd.read_csv(file_path)

    # Create a subset of users who have stopped paying (Charged Off) or are currently behind on payments
    subset = df[df['loan_status'].isin(['Charged Off', 'Late (16-30 days)', 'Late (31-120 days)'])]

    # Visualize the impact of loan grade on loan status
    plt.figure(figsize=(12, 6))
    sns.countplot(x='grade', hue='loan_status', data=subset, order=sorted(df['grade'].unique()))
    plt.title('Impact of Loan Grade on Loan Status')
    plt.xlabel('Loan Grade')
    plt.ylabel('Number of Customers')
    plt.show()

    # Visualize the impact of purpose on loan status
    plt.figure(figsize=(16, 8))
    sns.countplot(x='purpose', hue='loan_status', data=subset, order=sorted(df['purpose'].unique()))
    plt.title('Impact of Loan Purpose on Loan Status')
    plt.xlabel('Loan Purpose')
    plt.ylabel('Number of Customers')
    plt.xticks(rotation=45, ha='right')
    plt.show()

    # Visualize the impact of home ownership on loan status
    plt.figure(figsize=(10, 6))
    sns.countplot(x='home_ownership', hue='loan_status', data=subset, order=sorted(df['home_ownership'].unique()))
    plt.title('Impact of Home Ownership on Loan Status')
    plt.xlabel('Home Ownership')
    plt.ylabel('Number of Customers')
    plt.show()

if __name__ == "__main__":
    # Example usage
    file_path = '...'
    analyze_loan_indicators(file_path)
