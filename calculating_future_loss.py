import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def calculate_projected_loss_and_visualize(file_path):
    """
    Calculate the projected loss of loans marked as Charged Off and visualize the loss projected over the remaining term.

    Parameters:
    - file_path (str): The file path of the CSV file containing the loan data.

    Returns:
    float: The projected loss amount.
    """
    # Load the DataFrame
    df = pd.read_csv(file_path)

    # Filter only charged-off loans
    charged_off_loans = df[df['loan_status'] == 'Charged Off']

    # Calculate the projected loss
    projected_loss = charged_off_loans['out_prncp'].sum()

    # Visualize the loss projected over the remaining term
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='term', y='out_prncp', data=charged_off_loans)
    plt.title('Projected Loss Over Remaining Term for Charged-Off Loans')
    plt.xlabel('Loan Term')
    plt.ylabel('Projected Loss')
    plt.show()

    return projected_loss

# Example usage
file_path = '...'
projected_loss = calculate_projected_loss_and_visualize(file_path)

# Display the projected loss
print(f"Projected Loss Amount: ${projected_loss:.2f}")
