# Name: Hunter Becker, Chris Gallazeski
# Course: CMPSC 132
# File Name: Menu.py
# Date: 11/08/24
#
# Description: Allows for the organization of the Student class in a single list


import Tester
from BaseClass import BaseClass

from PhoneNumber import PhoneNumber
from Semester import Semester
from Address import Address
from Email import Email
from Date import Date
from Student import Student
from Tester import students


# Utilities
# Allows for type and integrity checks to ensure input is as expected

def is_int(data):
    if (data is False) or (data is None):
        return False
    casted = None
    if type(data) == int:
        return data
    try:
        casted = int(data)
    except ValueError:
        return False
    return casted

def input_integer():
    user_input = False
    while user_input is False:
        user_input = is_int(input())
        if user_input is False:
            print("Field only accepts integer values.")
    return user_input

def input_string():
    user_input = 1
    while is_int(user_input) or user_input == "":
        user_input = input()
        if is_int(user_input):
            print("Field only accepts string values.")
        if user_input == "":
            print("Field does not accept empty strings.")
    return user_input


# Functions for object creation
# Handles the creation of objects like Emails, Dates, etc.

def create_new_phone_number_instance():
    print(f"Creating a new phone number list!\n"
          f'To stop adding new numbers, enter\n'
          f'"-1" in place of the digits.')

    def create_new_phone_number():
        print(f"Please enter the digits:")
        new_number = input_integer()

        if new_number == -1:
            return False
        
        print(f"Please enter the number type:")
        new_type = input_string()

        PhoneNumber(
            new_number,
            new_type
        )
        return PhoneNumber

    new_phone_number_list = []
    new_phone_number = create_new_phone_number()

    while new_phone_number:
        new_phone_number_list.append(new_phone_number)
        print(f"Creating a new phone number (-1 to stop)")
        new_phone_number = create_new_phone_number()

    if len(new_phone_number_list) == 0:
        print(f"List creation cancelled!")
        return False

    return new_phone_number_list

def create_new_semester():
    print(f"Creating a new semester!")
    
    print(f"Please enter the semester season. (ex. Fall, Spring)")
    new_season = input_string()
    print(f"Please enter the year. (ex. 1994, 2013)")
    new_year = input_integer()

    new_semester = Semester(
        new_season,
        new_year
        )
    return new_semester 

def create_new_address():
    print(f"Creating a new address!")

    print(f"Please enter the street name.")
    new_street = input_string()
    print(f"Please enter the city name.")
    new_city = input_string()
    print(f"Please enter the state name.")
    new_state = input_string()
    print(f"Please enter the zip code.")
    new_zip = input_integer()
    print(f"Please enter the address type. (ex. Business, Home)")
    new_type = input_string()
    
    new_address = Address(
        new_street,
        new_city,
        new_state,
        new_zip,
        new_type
    )
    return new_address

def create_new_email():
    print(f"Creating a new email!")

    print(f"Please enter the email address.")
    new_address = input_string()
    print(f"Please enter the email type. (ex. Personal, School)")
    new_type = input_string()

    new_email = Email(
        new_address,
        new_type
    )
    return new_email

def create_new_date():
    print(f"Creating a new date!")

    print(f"Please enter the month:")
    new_month = input_string()
    print(f"Please enter the day:")
    new_day = input_integer()
    print(f"Please enter the year:")
    new_year = input_integer()

    new_date = Date(
        new_month,
        new_day,
        new_year
    )
    return new_date

def create_new_student():
    print(f"Creating a new student!")

    print(f"Please enter their name:")
    new_name = input_string()
    print(f"Please enter their student ID")
    new_id = input_integer()
    print(f"Please enter their mailing address:")
    new_mailing_address = create_new_address()
    print(f"Please enter their email address:")
    new_email_address = create_new_email()
    print(f"Please enter a list of their phone numbers:")
    new_phone_number_list = create_new_phone_number_instance()
    print(f"Please enter their birth date:")
    new_birth_date = create_new_date()
    print(f"Please enter their acceptance date:")
    new_acceptance_date = create_new_date()
    print(f"Please enter their start semester:")
    new_start_semester = create_new_semester()
    print(f"Please enter their intended major:")
    new_intended_major = input_string()

    new_student = Student(
        new_name,
        new_id,
        new_mailing_address,
        new_email_address,
        new_phone_number_list,
        new_birth_date,
        new_acceptance_date,
        new_start_semester,
        new_intended_major
    )
    new_student.display()
    print(f"Are you sure you'd like to create this student?"
          f"Enter -1 to cancel.")
    cancel = is_int(input()) == -1
    if cancel:
        return False
    return new_student


# Functions for student management
# Handles the manipulation of Student objects within the Students list

def edit_student(student : Student):
    student.display()
    print(f"What attribute would you like to edit?")
    print(f"1 - Name")
    print(f"2 - Student ID")
    print(f"3 - Mailing Address")
    print(f"4 - Email Address")
    print(f"5 - Phone Number List")
    print(f"6 - Birth Date")
    print(f"7 - Acceptance Date")
    print(f"8 - Start Semester")
    print(f"9 - Intended Major")
    user_choice = input_integer()
    if user_choice == 1:
        new_name = input_string()
        student.set_name(new_name)

    elif user_choice == 2:
        new_id = input_integer()
        student.set_id(new_id)

    elif user_choice == 3:
        new_mailing_address = create_new_address()
        student.set_mailing_address(new_mailing_address)

    elif user_choice == 4:
        new_email_address = create_new_email()
        student.set_email_address(new_email_address)

    elif user_choice == 5:
        new_phone_number_list = create_new_phone_number_instance()
        student.set_phone_number(new_phone_number_list)

    elif user_choice == 6:
        new_birth_date = create_new_date()
        student.set_birth_date(new_birth_date)

    elif user_choice == 7:
        new_acceptance_date = create_new_date()
        student.set_acceptance_date(new_acceptance_date)

    elif user_choice == 8:
        new_start_semester = create_new_semester()
        student.set_start_semester(new_start_semester)

    elif user_choice == 9:
        new_intended_major = input_string()
        student.set_intended_major(new_intended_major)

    else:
        print(f"Nothing selected! Cancelling edit.")
    
    return

def add_student(student : Student):
    students.append(student)

def delete_student(student : Student):
    students.pop(students.index(student))

def display_student(student : Student):
    student.display()

def pick_student():
    if len(students) == 0:
        print(f"Cannot proceed further; No students in list!")
        return False
    
    index = 0
    print(f"Pick a student from this list, or -1 to cancel:")
    for student in students:
        print(f"{index} : {student.get_name()}")
        index += 1
    
    user_choice = input_integer()
    while (user_choice < -1) or (user_choice > len(students) - 1):
        print(f"Selection outside of range!")
        user_choice = input_integer()
    
    if user_choice == -1:
        return False
    return students[user_choice]


# Menu definition
# Handles user input and uses the other defined functions accordingly

def menu():
    user_option = 0
    while user_option != 5:
        print(f"\nWhat would you like to do?")
        print(f"1 - Add a student to the list")
        print(f"2 - Edit a student from the list")
        print(f"3 - Delete a student from the list")
        print(f"4 - Display a student's info")
        print(f"5 - Exit the application")
        user_option = input_integer()
        if user_option == 1:
            new_student = create_new_student()
            if new_student:
                add_student(new_student)

        elif user_option == 2:
            chosen_student = pick_student()
            if chosen_student:
                edit_student(chosen_student)

        elif user_option == 3:
            chosen_student = pick_student()
            if chosen_student:
                delete_student(chosen_student)

        elif user_option == 4:
            chosen_student = pick_student()
            if chosen_student:
                chosen_student.display()

    print(f"Thank you for using this student management program.")


# Main

if __name__ == '__main__':
    menu()