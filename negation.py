from formula import *


class Not(Formula):

    def __init__(self, operand: Formula):
        super().__init__(FormulaType.NEGATION)
        self.operand = operand

    def __str__(self):
        if self.operand.kind == FormulaType.NEGATION or self.operand.kind == FormulaType.VARIABLE:
            return "!" + str(self.operand)
        else:
            return "!(" + str(self.operand) + ")"

    def __hash__(self):
        return hash((super().__hash__(), self.operand))

    def __eq__(self, other):

        if not super().__eq__(other):
            return False

        return self.operand == other.operand

    def to_string(self):
        return self.__str__()

    def get_form(self):
        return self.operand
