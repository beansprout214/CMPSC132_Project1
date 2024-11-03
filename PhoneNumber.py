from BaseClass import BaseClass


class PhoneNumber(BaseClass):
    def __init__(self,
                 number : int,
                 type : str,
                 ):
        self.__number = number
        self.__type = type

    # Getters
    def get_number(self):
        return self.__number

    def get_type(self):
        return self.__type

    # Setters
    def set_number(self, number: int):
        self.__number = number

    def set_type(self, type: str):
        self.__type = type