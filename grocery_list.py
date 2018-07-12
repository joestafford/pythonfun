# Create the empty data structure
grocery_item = {}

grocery_history = []

#Variable used to check if the while loop condition is met
stop = 'go'

while stop not in ('q') :
  # Prompt user for input
  item_name = input('Item name:\n')
  quantity = input('Quantity purchased:\n')
  cost = input('Price per item:\n')
  
  # Populate dictionary with user input
  grocery_item = {'name':item_name, 'number': int(quantity), 'price': float(cost)}
  
  # Add dictionary to list
  grocery_history.append(grocery_item)
  
  # Prompt user to continue or quit
  stop = input('Would you like to enter another item?\nType \'c\' for continue or \'q\' to quit:\n')

# Define variable to hold grand total called 'grand_total'
grand_total = 0

# Define the loop.  

for grocery_item in grocery_history:
  #Calculate the total cost for the grocery_item.
  item_total = grocery_item['number'] * grocery_item['price']
  
  #Add the item_total to the grand_total
  grand_total = grand_total + float(item_total)
  
  #Output grocery item
  print(str(grocery_item['number']) + ' ' + grocery_item['name'] + ' @ $%.2f' % grocery_item['price'] + ' ea $%.2f' % item_total)
  
  #Set the item_total equal to 0
  item_total = 0

#Print the grand total
print('Grand total: $%.2f' % grand_total)