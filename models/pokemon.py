# Pokemon Model

class Pokemon:
    def __init__(self, id, name, types):
        self.__id = id
        self.__name = name
        self.__types = types

    def getID(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getTypes(self):
        return self.__types