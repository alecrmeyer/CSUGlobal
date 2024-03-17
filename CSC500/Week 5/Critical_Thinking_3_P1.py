while(True): #Handle input
    try:
        years = int(input("Please enter the number of years: "))
        break
    except:
        print("Invalid input, please enter an integer")
        
total_rain = 0
for year in range(years): #Years
    for month in range(12): #Months
        while(True): #Handle input
            try:
                total_rain += int(input(f'How many inches of rainfall for year {year+1} and month {month+1}: '))
                break
            except:
                print("Invalid input, please enter an integer")
total_months = years*12

print(f'Months: {total_months}')
print(f'Total rainfall: {total_rain}')
print(f'Average rainfall per month: {total_rain / total_months}')