while(True):  
    try:
        current_time = int(input("Please enter the current time: "))
        if(current_time < 0 or current_time >= 24 ):
            print("Please enter a valid current time") 
            continue 
        alarm_hours = int(input("Please enter the number of hours to wait: "))
        if(alarm_hours < 0):
            print("Please enter a time greater than 0")
            continue
    except:
        print("Invalid input, please enter a time")

    print("Current time: " + str(current_time))
    print("Time after " + str(alarm_hours) + " hours: " + str((alarm_hours + current_time) % 24))
    break