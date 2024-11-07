class Name:
    def __init__(self,
                 first:str,
                 middle:str,
                 last:str
                 ):
        self.__first = first
        self.__middle = middle
        self.__last = last

    def set_first(self,first):
        self.__first = first

    def set_middle(self,middle):
        self.__middle = middle

    def set_last(self,last):
        self.__last = last

    def get_first(self):
        return self.__first

    def get_middle(self):
        return self.__middle

    def get_last(self):
        return self.__last

    def __str__(self):
        return f"{self.__first} {self.__middle} {self.__last}"

