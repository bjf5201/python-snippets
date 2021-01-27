# Dictionary

daily_temps_list = [71.1, 71.5, 80.2, 79.2, 75.6, 73.5, 75.2]
daily_names = ['sun', 'mon', 'tues', 'wed', 'thur', 'fri', 'sat']

daily_temps_dict = {'sun':71.1, 'mon':71.5, 'tues':80.2, 'wed':79.2, 'thurs':75.6, 'fri':75.2}

print("This program displays the avg temperature for a given day")

terminate = False
while not terminate:

    day = input("Enter 'sun', 'mon', 'tues', 'wed', 'thur', 'fri', or 'sat': ")

    if day in daily_temps_dict:
        print("The temperature for {} is {}".format(day, daily_temps_dict[day]))
    else:
        print("Invalid input")

    t = input("Do you want to continue? (y/n) ")
    if t in 'Nn':
        terminate = True
