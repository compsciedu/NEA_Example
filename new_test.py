import csv
import sys

def mainmenu(username_enter):
    print("*****************************")
    print("   Video System  ")
    print("*****************************")           
    print("Hello " + username_enter)
    print()
    #Do more stuff
    input()

def loginmenu():
    print("*****************************")
    print("   Login  ")
    print("*****************************") 
    logged_in = False
    login = []
    with open('password.csv','r') as f:
        reader = csv.reader(f)
        login = list(reader)
    f.close()
    username_enter = input("enter username")
    password_enter = input("enter password")
    if username_enter in [row[0] for row in login]:
        if password_enter ==(login[[row[0] for row in login].index(username_enter)][1]):
            print("Logged in")
            logged_in = True
        else:
            print("Incorrect log in details")
    return logged_in, username_enter

def signupmenu():
     print("*****************************")
     print("   Signup  ")
     print("*****************************")
     username_signup_enter = input("enter username")
     password_signup_enter = input("enter password")
     with open('password.csv','a') as f: #appends to file
        writer=csv.writer(f)
        writer.writerow([username_signup_enter,password_signup_enter])
     f.close()
     print("New user "+username_signup_enter+" added")
     print()

def firstmenu(): 
    choice = 0
    while choice !=3:
        print("Press 1 Login")
        print("Press 2 Sign Up")
        print("Press 3 to Exit")
        try:
            choice = int(input("Enter your choice [1-3]: "))
            if choice==1:
                print ("Menu 1 has been selected")
                logged_in,username_enter = loginmenu()
                if logged_in == True:
                    mainmenu(username_enter)
            elif choice==2:
                print("Menu 2 has been selected")
                signupmenu()
            elif choice ==3:
                print("bye")
                exit
            else:
                print("Wrong option selection. Enter any key to try again..")
        except ValueError:
            print("Choose an option 1-3")



##Start Code
firstmenu()
