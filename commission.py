class CommissionCalculator:
    def __init__(self, commission_rate):
        self.commission_rate = commission_rate

    def calculate_commission(self, sales_amount):
        if sales_amount < 0:
            raise ValueError("Sales amount cannot be negative.")
        return sales_amount * self.commission_rate

def get_user_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    commission_rate = 0.1  # 10%
    calculator = CommissionCalculator(commission_rate)

    # Get two sales amounts from the user
    sales_amount1 = get_user_input("Enter sales amount 1: ")
    sales_amount2 = get_user_input("Enter sales amount 2: ")

    # Calculate and display commissions
    for sales in [sales_amount1, sales_amount2]:
        try:
            commission = calculator.calculate_commission(sales)
            print(f"Sales Amount: ${sales:.2f} | Commission: ${commission:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
