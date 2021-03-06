# Dictionary

daily_temps_dict = {'sun':71.1, 'mon':71.5, 'tues':80.2, 'wed':79.2, 'thur':75.6, 'fri':75.2, 'sat':81.4}

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
