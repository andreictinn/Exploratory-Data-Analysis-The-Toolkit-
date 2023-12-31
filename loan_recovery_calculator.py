import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_loan_recovery(df):
    """
    Analyzes the loan recovery data and visualizes the results.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing loan recovery data.

    Returns:
    None
    """
    # Assuming 'loan_status' is a categorical column
    df['loan_status'] = df['loan_status'].astype('category')

    # Calculate percentage of loans recovered against investor funding
    df['recovery_percentage_investor'] = (df['recoveries'] / df['funded_amount_inv']) * 100

    # Calculate percentage of loans recovered against total amount funded
    df['recovery_percentage_total'] = (df['recoveries'] / df['funded_amount']) * 100

    # Visualize recovery percentages
    plt.figure(figsize=(18, 9))
    plt.subplot(3, 1, 1)
    sns.barplot(x='loan_status', y='recovery_percentage_investor', data=df)
    plt.title('Percentage of Loans Recovered Against Investor Funding')
    plt.ylabel('Recovery Percentage')

    plt.subplot(3, 1, 2)
    sns.barplot(x='loan_status', y='recovery_percentage_total', data=df)
    plt.title('Percentage of Loans Recovered Against Total Amount Funded')
    plt.ylabel('Recovery Percentage')

    # Visualize recovery percentages up to 6 months in the future
    df['recovery_percentage_6_months'] = ((df['recoveries'] + df['total_rec_int']) / df['funded_amount']) * 100

    plt.subplot(3, 1, 3)
    sns.barplot(x='loan_status', y='recovery_percentage_6_months', data=df)
    plt.title('Percentage of Total Amount Recovered Up to 6 Months in the Future')
    plt.ylabel('Recovery Percentage')

    plt.tight_layout()

    # Increase x-axis label font size and rotate labels for all subplots
    for ax in plt.gcf().axes:
        plt.sca(ax)
        plt.xticks(rotation=45, ha='right', fontsize=12)

    plt.show()

if __name__ == "__main__":
    # Load the DataFrame from the CSV file
    file_path = 'file_path'
    df = pd.read_csv(file_path)

    # Example usage
    analyze_loan_recovery(df)