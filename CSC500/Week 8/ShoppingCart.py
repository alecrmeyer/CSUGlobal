from item import ItemToPurchase

class ShoppingCart:
    def __init__(self, customer_name = "none", current_date = "January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart = []
    
    def add_item(self, item: ItemToPurchase):
        self.cart.append(item) 

    def remove_item(self, item_name: str):       
        for item in self.cart:
            if item.item_name == item_name:
                self.cart.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_modify: ItemToPurchase):
        for item in self.cart:
            if item_to_modify.item_name == item.item_name:
                quantity = input("Enter the new quantity\n")
                item.item_quantity = float(quantity)
       
    def get_num_items_in_cart(self):
        return len(self.cart)
    
    def get_cost_of_cart(self):
        total = 0
        for item in self.cart:
            total += item.item_price * item.item_quantity
        return total
    
    def print_total(self):
        if self.get_cost_of_cart() == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print('OUTPUT SHOPPING CART')
            print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
            print(f'Number of Items: {self.get_num_items_in_cart()}')
            for item in self.cart:
                item.print_item_cost()
            print(f'Total ${self.get_cost_of_cart()}')

    def print_descriptions(self):
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
        print('Item Descriptions')
        for item in self.cart:
            print(f'{item.item_name}: {item.item_description}')

    def item_in_cart(self, item_name: str):
        for item in self.cart:
            if item.item_name == item_name:
                return True
        return False