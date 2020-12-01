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

    # compares two negation formulas
    def __eq__(self, other):

        if not super().__eq__(other):
            return False

        assert isinstance(other, Not)

        return self.operand == other.operand

    # getter for the operand of the formula
    def get_form(self) -> Formula:
        return self.operand
