from item import ItemToPurchase
from ShoppingCart import ShoppingCart

def print_menu(shopping_cart: ShoppingCart):
    while(True):
        print("    MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        user_option = input("Choose an option: ")

        if user_option == 'q':
            break

        elif user_option == 'a':
            try:
                name = input("Enter the item name: ")
                price = input("Enter the item price: ")
                quantity = input("Enter the item quantity: ")
                desc = input("Enter the item description: ")

                item = ItemToPurchase(name, float(price), int(quantity), desc)
            except:
                # Default Constructor
                item = ItemToPurchase()
            
            shopping_cart.add_item(item)
        
        elif user_option == 'r':
            item_name = input("What item would you like to remove? ")
            shopping_cart.remove_item(item_name)

        elif user_option == 'c':
            print() ## Milestone 8

        elif user_option == 'o':
            shopping_cart.print_total()
            shopping_cart.print_descriptions()

shopping_cart_name = input("What is your name? ")
shopping_cart_date = input("What is the date? ")
shopping_cart = ShoppingCart(shopping_cart_name, shopping_cart_date)

print_menu(shopping_cart)






        
