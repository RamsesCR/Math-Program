def appMenu():
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Option 4")
    print("5. Option 5")
    print("6. Exit")

def option1():
    print("")
    ## option 1 code here

def option2():
    print("")
    ## option 2 code here

def option3():
    print("")
    ## option 3 code here

def option4():
    print("")
    ## option 4 code here

def option5():
    print("")
    ## option 5 code here


while True:
    appMenu()
    choice = input("Enter your choice: ")
    if choice == "1":
        option1()
    elif choice == "2":
        option2()
    elif choice == "3":
        option3()
    elif choice == "4":
        option4()
    elif choice == "5":
        option5()
    elif choice == "6":
        print("Exiting")
        break
    else:
        print("Invalid choice. Try again.")