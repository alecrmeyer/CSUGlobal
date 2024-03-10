from item import ItemToPurchase
from groceryList import GroceryList

grocery_list = GroceryList()

while(True):
    print(f'Item {grocery_list.get_size() + 1}')

    try:
        name = input("Enter the item name: ")
        price = input("Enter the item price: ")
        quantity = input("enter the item quantity: ")

        item = ItemToPurchase(name, float(price), int(quantity))
    except:
        # Default Constructor
        item = ItemToPurchase()

    grocery_list.add(item)

    option = input("Add another item? (yes) ")
    if str(option) != "yes":
        break

print(f'TOTAL COST')
grocery_list.print_items()
print(f'Total: ${grocery_list.total_cost()}')

