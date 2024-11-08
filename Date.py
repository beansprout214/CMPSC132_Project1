# Name: Hunter Becker, Chris Gallazeski
# Course: CMPSC 132
# File Name: Date.py
# Date: 11/08/24
#
# Description: Contains the Date class
# Attributes: month, day, year


from BaseClass import BaseClass


class Date(BaseClass):
    def __init__(self,
                 month : int,
                 day : int,
                 year : int,
                 ):
        self.__month = month
        self.__day = day
        self.__year = year

    # Getters
    def get_month(self):
        return self.__month

    def get_day(self):
        return self.__day

    def get_year(self):
        return self.__year

    # Setters
    def set_month(self, month: int):
        self.__month = month

    def set_day(self, day: int):
        self.__day = day

    def set_year(self, year: int):
        self.__year = year