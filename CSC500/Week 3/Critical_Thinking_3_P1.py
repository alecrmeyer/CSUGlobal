while(True):
    food_cost_str = input("Please enter the price of your food: ")
    tax_amount = 0.07
    tip_amount = 0.18
    try:
        food_cost = float(food_cost_str)
        tax = food_cost * tax_amount
        tip = food_cost * tip_amount
        print("Tax (" + str(int(tax_amount*100)) +"%%): %5.2f" % (tax))
        print("Tip (" + str(int(tip_amount*100)) +"%%): %5.2f" % (tip))
        print("Total (cost + tax + tip): %.2f"  % (food_cost + tip + tax))
        break
    except:
        print("Invalid input, please enter a dollar amount")
    
