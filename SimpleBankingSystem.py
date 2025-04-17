# William Starks
# proj4.py
# March 5, 2025
# A simple banking menu system for deposits, withdrawals, and repeating payments.

print("Enter starting balance:")
balance = float(input())

print("You have a balance of $" + format(balance, ",.2f"))

choice = ""

while choice != "q":
    choice = input("Enter d for Deposit, w for Withdrawal, r for Repeating Payments, or q to Quit: ")
    
    if choice == "d":  # Deposit
        deposit = -1
        while deposit <= 0:
            deposit = float(input("Enter deposit amount: "))
            if deposit <= 0:
                print("Deposit amount must be positive.")
        
        balance += deposit
        print("You deposited $" + format(deposit, ",.2f") + ". Your balance is now $" + format(balance, ",.2f"))

    elif choice == "w":  # Withdrawal
        withdrawal = -1
        while withdrawal <= 0:
            withdrawal = float(input("Enter withdrawal amount: "))
            if withdrawal <= 0:
                print("Withdrawal amount must be positive.")

        if withdrawal > balance:
            print("You only have $" + format(balance, ",.2f") + " in your account and cannot withdraw $" + format(withdrawal, ",.2f") + ". Withdrawal denied.")
        else:
            balance -= withdrawal
            print("You withdrew $" + format(withdrawal, ",.2f") + ". Your balance is now $" + format(balance, ",.2f"))

    elif choice == "r":  # Repeating Payments
        payment = float(input("Enter payment amount: "))
        num_payments = int(input("Enter number of payments: "))
        total_cost = payment * num_payments

        if total_cost > balance:
            print("You only have $" + format(balance, ",.2f") + " but require $" + format(total_cost, ",.2f") + " to cover all payments. Repeating payments denied.")
        else:
            for i in range(1, num_payments + 1):
                balance -= payment
                print("Payment " + str(i) + " for $" + format(payment, ",.2f") + " made. Your balance is now $" + format(balance, ",.2f") + ".")

    elif choice != "q":
        print(choice + " is an invalid option")

print("Your balance is $" + format(balance, ",.2f") + ". Have a nice day!")

