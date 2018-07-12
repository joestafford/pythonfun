import sys

#account balance 
account_balance = float(500.25)

#printbalance function
def print_balance():
  print('Your current balance:\n' + str(account_balance))

#deposit function
def deposit():
  deposit_amount = float(input("How much would you like to deposit today?\n"))
  balance = account_balance + deposit_amount
  print('Deposit was $%.2f' % deposit_amount + ', current balance is $%.2f' % balance)

#withdraw function
def withdrawal():
  global account_balance
  withdrawal_amount = float(input("How much would you like to withdraw today?\n"))
  if withdrawal_amount > account_balance:
    # Codio will not pass this function unless improper grammer is used in the message, using "greater that" instead of "greater than"
    print('$%.2f' % withdrawal_amount + ' is greater that your account balance of ' + '$%.2f' % account_balance)
  elif withdrawal_amount <= account_balance:
    account_balance = account_balance - withdrawal_amount
    print('Withdrawal amount was $%.2f' % withdrawal_amount + ', current balance is $%.2f' % account_balance)

#User Input goes here, use if/else conditional statement to call function based on user input

userchoice = input("What would you like to do?\n").upper()

if (userchoice == 'D'):
  deposit()
elif (userchoice == 'W'):
  withdrawal()
elif (userchoice == 'B'):
  print_balance()
elif (userchoice == 'Q'):
  print('Thank you for banking with us.')