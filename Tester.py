from PhoneNumber import PhoneNumber
from Semester import Semester
from Address import Address
from Student import Student
from Email import Email
from Date import Date

student1_phone_number = PhoneNumber(
    9876543210, 
    "Personal"
)

student1_semester = Semester(
    "Spring", 
    2025
)

student1_address = Address(
    "Baker Street", 
    "Gotham", 
    "New York", 
    67890, 
    "Temporary"
)

student1_email = Email(
    "another_example@mail.com", 
    "Work"
)

student1_birth_date = Date(
    12, 
    25, 
    1995
)

student1_acceptance_date = Date(
    8, 
    15, 
    2024
)

student1_student = Student(
    "Jane Doe", # Student Name
    456, # Student ID
    student1_address, # Student Mailing Address
    [student1_email], # Student Email Addresses (Contains at least 1 email address)
    [student1_phone_number], # Student Phone Numbers (Contains at least 1 phone number)
    student1_birth_date, # Birth Date
    student1_acceptance_date, # Acceptance Date
    student1_semester, # Start semester
    "Engineering" # Student Intended Major
)
student2_phone_number = PhoneNumber(
    1230984567, 
    "Personal"
)

student2_semester = Semester(
    "Summer", 
    2024
)

student2_address = Address(
    "155 Cornelia Street", 
    "New York", 
    "New York", 
    10014, 
    "Temporary"
)

student2_email = Email(
    "taylor.swift@music.com", 
    "Personal"
)

student2_birth_date = Date(
    12, 
    13, 
    1989
)

student2_acceptance_date = Date(
    9, 
    10, 
    2024
)

student2_student = Student(
    "Taylor Swift", # Student Name
    666, # Student ID
    student2_address, # Student Mailing Address
    [student2_email], # Student Email Addresses (Contains at least 1 email address)
    [student2_phone_number], # Student Phone Numbers (Contains at least 1 phone number)
    student2_birth_date, # Birth Date
    student2_acceptance_date, # Acceptance Date
    student2_semester, # Start semester
    "Music" # Student Intended Major
)

student3_phone_number = PhoneNumber(
    1234567890,
    "Work"
)

student3_semester = Semester(
    "Winter",
    2024
)

student3_address = Address(
    "10880 Malibu Point",
    "Malibu",
    "California",
    90265,
    "Permanent"
)

student3_email = Email(
    "tony.stark@starkindustries.com",
    "Work"
)

student3_birth_date = Date(
    5,
    29,
    1970
)

student3_acceptance_date = Date(
    9,
    1,
    2024
)

student3_student = Student(
    "Tony Stark", # Student Name
    999, # Student ID
    student3_address, # Student Mailing Address
    [student3_email], # Student Email Addresses (Contains at least 1 email address)
    [student3_phone_number], # Student Phone Numbers (Contains at least 1 phone number)
    student3_birth_date, # Birth Date
    student3_acceptance_date, # Acceptance Date
    student3_semester, # Start semester
    "Engineering" # Student Intended Major
)
student4_phone_number = PhoneNumber(
    9876543210,
    "Home"
)

student4_semester = Semester(
    "Fall",
    2024
)

student4_address = Address(
    "4 Privet Drive",
    "Little Whinging",
    "Surrey",
    12345,
    "Temporary"
)

student4_email = Email(
    "hermione.granger@hogwarts.com",
    "School"
)

student4_birth_date = Date(
    9,
    19,
    1979
)

student4_acceptance_date = Date(
    8,
    10,
    2024
)

student4_student = Student(
    "Hermione Granger", # Student Name
    888, # Student ID
    student4_address, # Student Mailing Address
    [student4_email], # Student Email Addresses (Contains at least 1 email address)
    [student4_phone_number], # Student Phone Numbers (Contains at least 1 phone number)
    student4_birth_date, # Birth Date
    student4_acceptance_date, # Acceptance Date
    student4_semester, # Start semester
    "Magic" # Student Intended Major
)
student5_phone_number = PhoneNumber(
    5551234567,
    "Personal"
)

student5_semester = Semester(
    "Spring",
    2025
)

student5_address = Address(
    "1007 Mountain Drive",
    "Gotham",
    "New Jersey",
    67890,
    "Permanent"
)

student5_email = Email(
    "bruce.wayne@wayneenterprises.com",
    "Work"
)

student5_birth_date = Date(
    2,
    19,
    1972
)

student5_acceptance_date = Date(
    9,
    15,
    2024
)

student5_student = Student(
    "Bruce Wayne", # Student Name
    777, # Student ID
    student5_address, # Student Mailing Address
    [student5_email], # Student Email Addresses (Contains at least 1 email address)
    [student5_phone_number], # Student Phone Numbers (Contains at least 1 phone number)
    student5_birth_date, # Birth Date
    student5_acceptance_date, # Acceptance Date
    student5_semester, # Start semester
    "Business Administration" # Student Intended Major
)



students = [student1_student, student2_student, student3_student, student4_student, student5_student]
for student in students:
    print(student)




"""
Student Class
__name : Jane Doe
__id : 456
__mailing_address : Address : Baker Street
__mailing_address : Address : Gotham
__mailing_address : Address : New York
__mailing_address : Address : 67890
__mailing_address : Address : Temporary
__email_address : Email : another_example@mail.com
__email_address : Email : Work
__phone_number : PhoneNumber : 9876543210
__phone_number : PhoneNumber : Personal
__birth_date : Date : 12
__birth_date : Date : 25
__birth_date : Date : 1995
__acceptance_date : Date : 8
__acceptance_date : Date : 15
__acceptance_date : Date : 2024
__start_semester : Semester : Spring
__start_semester : Semester : 2025
__intended_major : Engineering


Student Class
__name : Taylor Swift
__id : 666
__mailing_address : Address : 155 Cornelia Street
__mailing_address : Address : New York
__mailing_address : Address : New York
__mailing_address : Address : 10014
__mailing_address : Address : Temporary
__email_address : Email : taylor.swift@music.com
__email_address : Email : Personal
__phone_number : PhoneNumber : 1230984567
__phone_number : PhoneNumber : Personal
__birth_date : Date : 12
__birth_date : Date : 13
__birth_date : Date : 1989
__acceptance_date : Date : 9
__acceptance_date : Date : 10
__acceptance_date : Date : 2024
__start_semester : Semester : Summer
__start_semester : Semester : 2024
__intended_major : Music


Student Class
__name : Tony Stark
__id : 999
__mailing_address : Address : 10880 Malibu Point
__mailing_address : Address : Malibu
__mailing_address : Address : California
__mailing_address : Address : 90265
__mailing_address : Address : Permanent
__email_address : Email : tony.stark@starkindustries.com
__email_address : Email : Work
__phone_number : PhoneNumber : 1234567890
__phone_number : PhoneNumber : Work
__birth_date : Date : 5
__birth_date : Date : 29
__birth_date : Date : 1970
__acceptance_date : Date : 9
__acceptance_date : Date : 1
__acceptance_date : Date : 2024
__start_semester : Semester : Winter
__start_semester : Semester : 2024
__intended_major : Engineering


Student Class
__name : Hermione Granger
__id : 888
__mailing_address : Address : 4 Privet Drive
__mailing_address : Address : Little Whinging
__mailing_address : Address : Surrey
__mailing_address : Address : 12345
__mailing_address : Address : Temporary
__email_address : Email : hermione.granger@hogwarts.com
__email_address : Email : School
__phone_number : PhoneNumber : 9876543210
__phone_number : PhoneNumber : Home
__birth_date : Date : 9
__birth_date : Date : 19
__birth_date : Date : 1979
__acceptance_date : Date : 8
__acceptance_date : Date : 10
__acceptance_date : Date : 2024
__start_semester : Semester : Fall
__start_semester : Semester : 2024
__intended_major : Magic


Student Class
__name : Bruce Wayne
__id : 777
__mailing_address : Address : 1007 Mountain Drive
__mailing_address : Address : Gotham
__mailing_address : Address : New Jersey
__mailing_address : Address : 67890
__mailing_address : Address : Permanent
__email_address : Email : bruce.wayne@wayneenterprises.com
__email_address : Email : Work
__phone_number : PhoneNumber : 5551234567
__phone_number : PhoneNumber : Personal
__birth_date : Date : 2
__birth_date : Date : 19
__birth_date : Date : 1972
__acceptance_date : Date : 9
__acceptance_date : Date : 15
__acceptance_date : Date : 2024
__start_semester : Semester : Spring
__start_semester : Semester : 2025
__intended_major : Business Administration
"""