class GroceryList:
    def __init__(self):
        self.list = []

    def add(self, item):
        self.list.append(item)

    def remove(self, item):
        self.list.remove(item)
    
    def get_size(self):
        return len(self.list)

    def total_cost(self):
        total = 0
        for item in self.list:
            total += item.get_total()
        return total
    
    def print_items(self):
        for item in self.list:
            item.print_item_cost()
        
