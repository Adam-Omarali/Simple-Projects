# this is a calander the user can add or delete events from

from time import sleep, strftime

USER_NAME = (input("What is your name: "))

calendar = {}


def welcome():
    print("Welcome " + USER_NAME + ". This is your new calander!")
    print("calander is openning...")
    sleep(1)
    print(strftime("%A, %B, %d, %Y"))
    print(strftime("%H:%M:%S"))
    sleep(1)
    print("What would you like to do?")


def start_calendar():
    welcome()
    start = True
    while start == True:
        user_choice = (input("A to Add, U to Update, V to View, D to Delete, X to Exit: "))
        user_choice = user_choice.upper()

        if user_choice == "V":

            if len(calendar.keys()) < 1:
                print("The calendar is empty")


            else:
                print(calendar)

        elif user_choice == "U":
            date = input("What date? ")
            update = input("Enter the update: ")
            calendar[date] = update
            print("Update Successful!")
            print(calendar)

        elif user_choice == "A":
            event = input("Enter your event: ")
            date = input("Enter date (MM/DD/YYYY): ")

            if len(date) > 10 or int(strftime("%Y")) > int(date[6:10]):
                print("Make sure to enter the right format")

                try_again = (input("Try Again? Y for Yes, N for No: "))
                try_again = try_again.upper()

                if try_again == "Y":
                    continue  # starts the program over

                else:
                    start = False

            else:
                calendar[date] = event
                print("Your Event was Successfully Added")
                print(calendar)

        elif user_choice == "D":
            if len(calendar.keys()) < 1:
                print("Calendar is empty!")

            else:
                event = input("What Event? ")
                for date in calendar.keys():
                    if event == calendar[date]:  # checks if event exists
                        del (calendar[date])
                        print("Delete Successful")
                        print(calendar)

                    else:
                        print("An incorrect even was specified")

        elif user_choice == "X":
            start = False


start_calendar()