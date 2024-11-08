from BaseClass import BaseClass


from PhoneNumber import PhoneNumber
from Semester import Semester
from Address import Address
from Email import Email
from Date import Date
from Student import Student
from Tester import students


def create_student():
    stud_name = input("What is the students name?")

    stud_id = int(input("Student ID: "))

    stud_mail_add = input("Student street address: ")
    stud_mail_city = input("Student city: ")
    stud_mail_state = input("Student state: ")
    stud_mail_zip = int(input("Student zip code: "))
    stud_mail_type = input("Address type: ")
    stud_mail = Address(stud_mail_add,stud_mail_city,stud_mail_state,stud_mail_zip,stud_mail_type)

    stud_email_add = input("Student email address: ")
    stud_email_type = input("Student email type: ")
    stud_email = Email(stud_email_add,stud_email_type)

    stud_phone = int(input("Student phone number: "))
    stud_phone_type = input("Phone type: ")
    stud_phone_info = PhoneNumber(stud_phone,stud_phone_type)

    stud_birthday = int(input("Student birthday: "))
    stud_birth_month = int(input("Student birthmonth: "))
    stud_birth_year = int(input("Student birthyear: "))
    stud_birthdate = Date(stud_birth_month,stud_birthday,stud_birth_year)


    stud_accept_day = int(input("Student acceptance date: "))
    stud_accept_month = int(input("Student acceptance month: "))
    stud_accept_year = int(input("Student acceptance year: "))
    stud_accept_date = Date(stud_accept_month,stud_accept_day,stud_accept_year)

    stud_sem_season = input("What season will you start?\n")
    stud_start_year = int(input("What year will you start?\n"))
    stud_start_sem = Semester(stud_sem_season,stud_start_year)


    stud_major = input("Student intended major: ")

    stud_x = Student(stud_name,stud_id, stud_mail, stud_email, stud_phone_info, stud_birthdate, stud_accept_date, stud_start_sem, stud_major)
    return stud_x



def edit_student():
    valid = False
    while not valid:
        print("What info would you like to edit?")
        print("1. Student ID number.\n"
              "2. Student name(first, middle, last).\n"
              "3. Student mailing address.\n"
              "4. Student email address.\n"
              "5. Student phone number.\n"
              "6. Student birthday.\n"
              "7. Student Acceptance date.\n"
              "8. Starting semester.\n")
        user_choice = int(input("Enter your choice from the available options: "))
        if 1 <= user_choice <= 8:
            valid = True
        else:
            valid = False
    #edit student commands


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
        students = []
        if user_opt == 1:
            # add student via student class
            new_student = create_student()
            students.append(new_student)


        if user_opt == 2:  # print list and edit student via student class
            print("Which student would you like to edit?")
            for student in students:
                print(student)
                print("hi")


        if user_opt == 3:  # print student list and delete selected student
            for student in students:
                print(student)
            print("Which student would you like to delete?")


        if user_opt == 4:
            for student in students:
                print("What student would you like to display?")


        if user_opt == 5:
            print(exit())
            valid = False

        else:
            print("Invalid input, please try again.")



if __name__ == '__main__':

    student_test = create_new_student()
    print(student_test.display())
    students.append(student_test)
    for index,student in enumerate(students):
        print(f'{index+1}. {student.get_name()}')



