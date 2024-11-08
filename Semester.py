# Name: Hunter Becker, Chris Gallazeski
# Course: CMPSC 132
# File Name: Address.py
# Date: 11/08/24
#
# Description: Contains the Semester
# Attributes: season, year


from BaseClass import BaseClass


class Semester(BaseClass):
    def __init__(self,
                 season : str,
                 year : int,
                 ):
        self.__season = season
        self.__year = year

    # Getters
    def get_season(self):
        return self.__season

    def get_year(self):
        return self.__year

    # Setters
    def set_season(self, season : str):
        self.__season = season

    def set_year(self, year : int):
        self.__year = year