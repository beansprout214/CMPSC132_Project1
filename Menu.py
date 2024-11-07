import Tester
from BaseClass import BaseClass

from PhoneNumber import PhoneNumber
from Semester import Semester
from Address import Address
from Email import Email
from Date import Date
from Student import Student
from Tester import students


def create_new_student():
    new_id = int(input("Enter new student ID: "))

    new_name = input("Enter new student name: ")

    new_street = input("What is the street address?")
    new_city = input("What is the city?")
    new_state = input("What is the state?")
    new_zip = int(input("What is the zip code?"))
    new_type = input("What type of residence?")
    new_mailing_address = Address(new_street, new_city, new_state, new_zip, new_type)

    new_email = input("Enter new student email: ")
    new_email_type = input("What kind of email?")
    new_student_email = Email(new_email, new_email_type)

    new_number = int(input("Enter new student number: "))
    new_phone_type = input("What kind of phone number?")
    new_phone = PhoneNumber(new_number, new_phone_type)

    new_month = int(input("What month was the student born(number from 01-12): "))
    new_day = int(input("What day was the student born(number from 01-31): "))
    new_year = int(input("What year was the student born(number from 1900): "))
    new_birthday = Date(new_month, new_day, new_year)

    new_acc_month = int(input("What month was the student accepted(number form 01-12): "))
    new_acc_day = int(input("What number day was the student accepted(number from 01-31): "))
    new_acc_year = int(input("What year was the student accepted: "))
    new_acceptance = Date(new_acc_month, new_acc_day, new_acc_year)

    new_season = input('What season will you start(spring,summer,fall)? ')
    new_sem_year = int(input("What year will you start? "))
    starting_sem = Semester(new_season, new_sem_year)

    new_major = input("What is your new intended major?")

    new_student = Student(new_name, new_id, new_mailing_address, new_student_email, new_phone, new_birthday,
                          new_acceptance, starting_sem, new_major)

    return new_student

def edit_student():
    valid = False
    for index,student in enumerate(students):
        print(f'{index+1}. {student}')
    choice = int(input("Which student would you like to edit?"))
    current_student = students[choice-1]

    while not valid:
        print("What info would you like to edit?")
        print("1. Student ID number.\n"
              "2. Student name(first, middle, last).\n"
              "3. Student mailing address.\n"
              "4. Student email address.\n"
              "5. Student phone number.\n"
              "6. Student birthday.\n"
              "7. Student Acceptance date.\n"
              "8. Starting semester.\n"
              "9. Intended Major.\n")
        user_choice = int(input("Enter your choice from the available options: "))

        if user_choice == 1:
            valid = True
            new_id = int(input("Enter new student ID: "))
            current_student.set_id(new_id)

        if user_choice == 2:
            valid = True
            new_name = input("Enter new student name: ")
            current_student.set_name(new_name)

        if user_choice == 3:
            valid = True
            new_street = input("What is the street address?")
            new_city = input("What is the city?")
            new_state = input("What is the state?")
            new_zip = int(input("What is the zip code?"))
            new_type = input("What type of residence?")
            new_mailing_address = Address(new_street, new_city, new_state, new_zip, new_type)
            current_student.set_mailing_address(new_mailing_address)

        if user_choice == 4:
            valid = True
            new_email = input("Enter new student email: ")
            new_email_type = input("What kind of email?")
            new_student_email = Email(new_email, new_email_type)
            current_student.set_email_address(new_student_email)

        if user_choice == 5:
            valid = True
            new_number = int(input("Enter new student number: "))
            new_phone_type = input("What kind of phone number?")
            new_phone = PhoneNumber(new_number, new_phone_type)
            current_student.set_phone_number(new_phone)

        if user_choice == 6:
            valid = True
            new_month = int(input("What month was the student born(number from 01-12): "))
            new_day = int(input("What day was the student born(number from 01-31): "))
            new_year = int(input("What year was the student born(number from 1900): "))
            new_birthday = Date(new_month, new_day, new_year)
            current_student.set_birth_date(new_birthday)

        if user_choice == 7:
            valid = True
            new_acc_month = int(input("What month was the student accepted(number form 01-12): "))
            new_acc_day = int(input("What number day was the student accepted(number from 01-31): "))
            new_acc_year = int(input("What year was the student accepted: "))
            new_acceptance = Date(new_acc_month, new_acc_day, new_acc_year)
            current_student.set_acceptance_date(new_acceptance)

        if user_choice == 8:
            valid = True
            new_season = input('What season will you start(spring,summer,fall)? ')
            new_sem_year = int(input("What year will you start? "))
            starting_sem = Semester(new_season, new_sem_year)
            current_student.set_start_semester(starting_sem)

        if user_choice == 9:
            valid = True
            new_major = input("What is your new intended major?")
            current_student.set_intended_major(new_major)

        else:
            valid = False

def exit():
    return "Thank you for using the application!"


def menu():
    valid = True
    while valid == True:
        print('1. Add students to list.')
        print('2. Edit existing student info.')
        print('3. Delete existing student from list.')
        print('4. Display student info.')
        print('5. Exit the program.')
        user_opt = int(input("What would you like to do?\n"))


        if user_opt == 1:
            # add student via student class
            new_student = create_new_student()
            students.append(new_student)


        if user_opt == 2:  # print list and edit student via student class
            print("Which student would you like to edit?")
            edit_student()

        if user_opt == 3:  # print student list and delete selected student
            for index,student in enumerate(students):
                print(f'{index+1}. {student.get_name()}')
            usr_choice = int(input("Which student would you like to delete?"))
            del[students[usr_choice-1]]
            print("New list:")
            for index,student in enumerate(students):
                print(f'{index+1}. {student}')
            print()

        if user_opt == 4:
            for index,student in enumerate(students):
                print(f'{index+1}.{student.get_name()}')

            choice = int(input("What student would you like to display?"))
            s_index = choice-1
            current_student = students[s_index]
            print(current_student.display())


        if user_opt == 5:
            print(exit())
            valid = False

if __name__ == '__main__':
    menu()