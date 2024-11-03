from BaseClass import BaseClass


class Email(BaseClass):
    def __init__(self,
                 address : str,
                 type : str,
                 ):
        self.__address = address
        self.__type = type

    # Getters
    def get_address(self):
        return self.__address

    def get_type(self):
        return self.__type

    # Setters
    def set_address(self, address):
        self.__address = address

    def set_type(self, type):
        self.__type = type