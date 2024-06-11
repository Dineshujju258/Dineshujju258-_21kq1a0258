names_list = input("Enter item names separated by spaces: ").split()
quantities_list = [int(qty) for qty in input("Enter item quantities separated by spaces: ").split()]
prices_list = [float(price) for price in input("Enter item prices separated by spaces: ").split()]

def create_row(name, quantity, price):
  name_col = name.ljust(20)
  quantity_col = str(quantity).ljust(15)
  price_col = str(price).ljust(10)
  return name_col + quantity_col + price_col

print(create_row("Item Name", "Item Quantity", "Item Price"))

for name, quantity, price in zip(names_list, quantities_list, prices_list):
  print(create_row(name, quantity, price))

bill_items = []
total_amount = 0.0

print("\nbilled items")
for index in range(len(names_list)):
  print(f"{index + 1}. {names_list[index]}")

while True:
  choice = input("Enter item number or 'done': ").strip()
  if choice.lower() == 'done':
    break
  elif choice.isdigit():
    choice = int(choice)
    if 0 < choice <= len(names_list):
      index = choice - 1
      bill_items.append((names_list[index], quantities_list[index], prices_list[index]))
      total_amount += quantities_list[index] * prices_list[index]
      print(f"Added {names_list[index]} to the bill.")
    else:
      print("Invalid choice. Please select a valid number.")
  else:
    print("Invalid input. Please enter a number or 'done'.")

print("\nFinal Bill:")
print(create_row("Item Name", "Item Quantity", "Item Price"))
for name, quantity, price in bill_items:
  # No need to recalculate total_price here
  Total= quantity*price
  print(create_row(name, quantity, price))

print(f"\nTotal Amount: {total_amount:.2f}")
