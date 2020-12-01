from formula import *


class Implies(Formula):

    def __init__(self, left: Formula, right: Formula):
        super().__init__(FormulaType.IMPLICATION)
        self.left = left
        self.right = right

    def __str__(self):
        return "(" + str(self.left) + "->" + str(self.right) + ")"

    def __hash__(self):
        return hash((super().__hash__(), self.left, self.right))

    def __eq__(self, other):

        if not super().__eq__(other):
            return False

        return self.left == other.left and self.right == other.right

    def get_left(self) -> Formula:
        return self.left

    def get_right(self) -> Formula:
        return self.right
