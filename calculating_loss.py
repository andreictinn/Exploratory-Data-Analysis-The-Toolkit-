import pandas as pd

def calculate_charged_off_percentage_and_recovery(file_path):
    """
    Calculate the percentage of charged-off loans historically and the total amount paid towards these loans before being charged off.

    Parameters:
    - file_path (str): The file path of the CSV file containing the loan data.

    Returns:
    float: The percentage of charged-off loans.
    float: The total amount paid towards charged-off loans.
    """
    # Load the DataFrame
    df = pd.read_csv(file_path)

    # Filter only charged-off loans
    charged_off_loans = df[df['loan_status'] == 'Charged Off']

    # Calculate the percentage of charged-off loans historically
    charged_off_percentage = (charged_off_loans.shape[0] / df.shape[0]) * 100

    # Calculate the total amount paid towards charged-off loans
    total_amount_paid = charged_off_loans['total_payment'].sum()

    return charged_off_percentage, total_amount_paid

# Example usage
file_path = '...'
charged_off_percentage, total_amount_paid = calculate_charged_off_percentage_and_recovery(file_path)

# Display the results
print(f"Percentage of Charged-Off Loans Historically: {charged_off_percentage:.2f}%")
print(f"Total Amount Paid Towards Charged-Off Loans: ${total_amount_paid:.2f}")
