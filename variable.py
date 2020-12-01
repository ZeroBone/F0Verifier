from formula import *


class Variable(Formula):

    def __init__(self, name: str):
        super().__init__(FormulaType.VARIABLE)
        self.name = name

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash((super().__hash__(), self.name))

    def __eq__(self, other):

        if not super().__eq__(other):
            return False

        return self.name == other.name

    def to_string(self):
        return self.__str__()
