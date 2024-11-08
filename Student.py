# Name: Hunter Becker, Chris Gallazeski
# Course: CMPSC 132
# File Name: Address.py
# Date: 11/08/24
#
# Description: Contains the Student class
# Attributes: name, id, mailing_address, email_address, phone_number, birth_date, acceptance_date, start_semester, intended_major


from BaseClass import BaseClass


from PhoneNumber import PhoneNumber
from Semester import Semester
from Address import Address
from Email import Email
from Date import Date


class Student(BaseClass):
    def __init__(self,
                 name : str,
                 id : int,
                 mailing_address : Address,
                 email_address : Email,
                 phone_number : PhoneNumber,
                 birth_date : Date,
                 acceptance_date : Date,
                 start_semester : Semester,
                 intended_major : str,
                 ):
        self.__name = name
        self.__id = id
        self.__mailing_address = mailing_address
        self.__email_address = email_address
        self.__phone_number = phone_number
        self.__birth_date = birth_date
        self.__acceptance_date = acceptance_date
        self.__start_semester = start_semester
        self.__intended_major = intended_major

    # Getters
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_mailing_address(self):
        return self.__mailing_address

    def get_email_address(self):
        return self.__email_address

    def get_phone_number(self):
        return self.__phone_number

    def get_birth_date(self):
        return self.__birth_date

    def get_acceptance_date(self):
        return self.__acceptance_date

    def get_start_semester(self):
        return self.__start_semester

    def get_intended_major(self):
        return self.__intended_major

    # Setters
    def set_name(self, name: str):
        self.__name = name

    def set_id(self, id: int):
        self.__id = id

    def set_mailing_address(self, mailing_address: Address):
        self.__mailing_address = mailing_address

    def set_email_address(self, email_address: Email):
        self.__email_address = email_address

    def set_phone_number(self, phone_number: PhoneNumber):
        self.__phone_number = phone_number

    def set_birth_date(self, birth_date: Date):
        self.__birth_date = birth_date

    def set_acceptance_date(self, acceptance_date: Date):
        self.__acceptance_date = acceptance_date

    def set_start_semester(self, start_semester: Semester):
        self.__start_semester = start_semester

    def set_intended_major(self, intended_major: str):
        self.__intended_major = intended_major

    def __str__(self):
        return (f'Name: {self.__name}\n'
                f'ID: {self.__id}\n'
                f'Mailing Address: {self.__mailing_address}\n'
                f'Email Address: {self.__email_address}\n'
                f'Phone Number: {self.__phone_number}\n'
                f'Birth Date: {self.__birth_date}\n'
                f'Acceptance Date: {self.__acceptance_date}\n'
                f'Starting Semester: {self.__start_semester}\n'
                f'Intended Major: {self.__intended_major}')
