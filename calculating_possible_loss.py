import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def calculate_loss_and_visualize_risk(file_path):
    """
    Calculate the percentage of users currently behind on loan payments, the total amount, and the projected loss.

    Parameters:
    - file_path (str): The file path of the CSV file containing the loan data.

    Returns:
    tuple: A tuple containing the percentage of users behind on payments, the total amount, and the projected loss.
    """
    # Load the DataFrame
    df = pd.read_csv(file_path)

    # Filter customers currently behind on loan payments
    late_customers = df[df['loan_status'].isin(['Late (16-30 days)', 'Late (31-120 days)'])]

    # Calculate the percentage of users currently behind on payments
    percentage_late_customers = (len(late_customers) / len(df)) * 100

    # Calculate the total amount of customers in this bracket
    total_late_customers = len(late_customers)

    # Calculate the loss the company would incur if the status was changed to Charged Off
    loss_if_charged_off = late_customers['out_prncp'].sum()

    # Calculate the projected loss if customers finish the full loan term
    projected_loss = late_customers['out_prncp_inv'].sum()

    # Calculate the percentage of total expected revenue represented by late and charged-off customers
    total_expected_revenue = df['funded_amount_inv'].sum()
    total_loss_percentage = ((loss_if_charged_off + projected_loss) / total_expected_revenue) * 100

    # Visualize the risk
    plt.figure(figsize=(12, 6))
    sns.countplot(x='loan_status', data=late_customers)
    plt.title('Loan Status of Customers Currently Behind on Payments')
    plt.xlabel('Loan Status')
    plt.ylabel('Number of Customers')
    plt.show()

    return percentage_late_customers, total_late_customers, loss_if_charged_off, projected_loss, total_loss_percentage

# Example usage
file_path = 'D:/Coding/loan_payments.csv'
result = calculate_loss_and_visualize_risk(file_path)

# Display the results
percentage_late_customers, total_late_customers, loss_if_charged_off, projected_loss, total_loss_percentage = result
print(f"Percentage of Users Currently Behind on Payments: {percentage_late_customers:.2f}%")
print(f"Total Amount of Customers Currently Behind on Payments: {total_late_customers}")
print(f"Loss if Customers Currently Behind on Payments Converted to Charged Off: ${loss_if_charged_off:.2f}")
print(f"Projected Loss if Customers Finish Full Loan Term: ${projected_loss:.2f}")
print(f"Percentage of Total Expected Revenue Represented by Late and Charged-Off Customers: {total_loss_percentage:.2f}%")
