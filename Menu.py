from PhoneNumber import PhoneNumber
from Semester import Semester
from Address import Address
from Student import Student
from Email import Email
from Date import Date

def define_phone_number():
    print("Defining a new phone number")
    print("Enter the phone number:")
    busy = True
    while busy:
        new_number = input()


def main():
    print("menu start")
    while True:
        user_input = input()
        if user_input == "add":
            print("adding a student")
        elif user_input == "remove":
            print("removing a student")
        elif user_input == "edit":
            print("editing a student")
        elif user_input == "display":
            print("displaying a student")
        elif user_input == "exit":
            print("exiting application")
            return
        else:
            print("invalid command")
main()