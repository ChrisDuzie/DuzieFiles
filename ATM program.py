def bank_operations():
      name = input("Welcome to our banking platform. Please enter your name: ")
      bank_name = input("Enter your bank name:")
      balance = 5000.00

      print(f"Hello {name}! Welcome to {bank_name}. Your current balance is ${balance}.")

      while True:
          print("Please choose an option:")
          print("1.Check balance")
          print("2.Deposit")
          print("3.Withdraw")
          print("4.Exit")

          option = int(input())

          if option == 1:
              check_balance(balance)

          elif option == 2:
               deposit(balance)

          elif option == 3:
               withdraw(balance)

          elif option == 4:
               break

          else:
              print("Invalid option. Please do try again.")

def check_balance(balance):
    print("Your balance is $" + str(balance))

def deposit(balance):
    amount = float(input("Enter the amount:"))
    balance += amount
    print("You have deposited $" + str(amount) + ". Your new balance is $" + str(balance))

def withdraw(balance):
    amount = float(input("Enter amount."))
    if amount > balance:
        print("Error: Insufficient funds.")
    else:
        balance -= amount
        print("You have withdrawn $" + str(amount) + " . Your new balance is $" + str(balance))

bank_operations()


