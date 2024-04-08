class ItemToPurchase:
    def __init__(self, item_name = "none", item_price = 0.0, item_quantity = 0, item_description = "none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
        self.total_cost = self.item_price * self.item_quantity


    # Print the formatted item cost
    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.total_cost}')
    
    # Return item total cost
    def get_total(self):
        return self.total_cost
    
    