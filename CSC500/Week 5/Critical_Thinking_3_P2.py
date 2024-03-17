while(True):
    try:
        total = int(input("How many books have you purchased this month? "))
        break
    except:
        print("Invalid input, please print an integer")
points = 0
if(total < 2):
    points = 0
elif(total < 4 and total >= 2):
    points = 5
elif(total < 6 and total >= 4):
    points = 15
elif(total < 8 and total >= 6):
    points = 30
else:
    points = 60
print(f'You currently have {points} points')
