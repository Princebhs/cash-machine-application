"""
Simple ATM (Automated Teller Machine) Program
Features:
- PIN Authentication
- Balance Checking
- Money Deposits
- Money Withdrawals
- Transaction History

"""
# PIN verification function
def check_pin(enter_pin):
    """
    Verify if the entered PIN matches the correct PIN
    """    
    correct_pin = "1234"
    if enter_pin == correct_pin:
        return True
    return False

balance = 1000 # Starting balance for the account
transaction_history = [] # List to store all transactions

def check_balance(): 
    """
    shows the current balance of the account
    """    

    return balance

def deposit(amount):
    """
    Deposit money into the account
    """    

    global balance 
    if amount > 0: 
        balance += amount
        transaction_history.append(f"deposit: +£{amount}")
        return True
    return False

def withdraw(amount):
    """
    Withdraw money from the account
    """    
    
    global balance
    if amount > 0 and amount <= balance:  # Check if withdrawal is valid
        balance -= amount
        transaction_history.append(f"Withdrawal: -£{amount}")
        return True
    return False

def show_history():
    """
    Display all transactions made in the current session
    Prints each transaction line by line
    """    

    if len(transaction_history) == 0:
        print("No transaction history available")
    else:
        print("\nTransaction History:")
        for transaction in transaction_history:
            print(transaction)

def main():
    """
    Main function that runs the ATM program
    Handles:
    - PIN verification
    - Menu display
    - User input processing
    - Error handling
    """

    attempts = 3 

    while attempts > 0:
        pin = input("Enter your PIN: ")

        if check_pin(pin):
            print("\nPIN accepted! Welcome to the ATM")

            while True:
                print("\n=== ATM Menu ===")
                print("1. Check Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. View Transaction History")
                print("5. Exit")

                choice = input("\nEnter your choice (1-5): ")

                 # Handle user's menu choice
                if choice == '1':
                    # Balance checking
                    print(f"\nYour balance is: £{check_balance()}")
                
                elif choice == '2':
                    # Deposit handling
                    try:
                        amount = float(input("Enter amount to deposit: £"))
                        if deposit(amount):
                            print(f"Deposit successful! New balance: £{check_balance()}")
                        else:
                            print("Invalid deposit amount")
                    except ValueError:
                        print("Please enter a valid number")
                
                elif choice == '3':
                    # Withdrawal handling
                    try:
                        amount = float(input("Enter amount to withdraw: £"))
                        if withdraw(amount):
                            print(f"Withdrawal successful! New balance: £{check_balance()}")
                        else:
                            print("Invalid withdrawal amount or insufficient funds")
                    except ValueError:
                        print("Please enter a valid number")
                
                elif choice == '4':
                    # Transaction history display
                    show_history()
                
                elif choice == '5':
                    # Exit program
                    print("Thank you for using our ATM. Goodbye!")
                    return
                
                else:
                    # Invalid menu choice
                    print("Invalid choice. Please try again.")
            
        else:
            # Handle incorrect PIN
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect PIN. {attempts} attempts remaining")
            else:
                print("Too many incorrect attempts. Your account has been locked.")

# Program entry point
if __name__ == "__main__":
    print("Welcome to the ATM")
    main()






    


