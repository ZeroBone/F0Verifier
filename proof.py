from formula import *
from implies import Implies


class Proof:

    def __init__(self, assumptions: list, proof: list):
        self.assumptions = set(assumptions)
        self.proof = proof
        # set of already proven formulas
        self.proven = set()
        # dictionary with possible modus ponens derivations
        # key: formula derivable using modus ponens
        # value: set of formulas from which the key can be derived with modus ponens
        self.modus_ponens = {}

    # Adds the formula to the set of already proven formulas
    # and makes sure that the possible modus ponens rules are also registered
    def add_proven(self, formula: Formula) -> None:

        self.proven.add(formula)

        if formula.kind == FormulaType.IMPLICATION:

            assert isinstance(formula, Implies)

            right = formula.get_right()
            left = formula.get_left()

            # check that this right hand side hasn't already been proven
            if right not in self.modus_ponens:
                self.modus_ponens[right] = {left}
            else:
                self.modus_ponens[right].add(left)

    # returns whether the formula can be proven by using modus ponens
    # on some already proven formula
    def proven_with_modus_ponens(self, formula: Formula) -> bool:

        if formula not in self.modus_ponens:
            return False

        possible_left_sides = self.modus_ponens[formula]

        # there is a proof if and only if the intersection
        # of the set of left hand sides with the set of proven formulas
        # is not empty
        return bool(possible_left_sides & self.proven)

    # verifies whether the proof is correct
    def verify(self) -> bool:

        for formula in self.assumptions:

            if formula in self.proven:
                print(str(formula) + " is a redundant assumption")
                continue

            self.add_proven(formula)

        for formula in self.proof:

            if formula.is_axiom():
                self.add_proven(formula)
                print(str(formula) + " is an axiom")
                continue

            if formula in self.proven:
                print(str(formula) + " is already proven and redundant")
                continue

            # check whether modus ponens was applied in this step
            # if the formula can be the right hand side of modus ponens
            # and the left hand side is already proven
            if self.proven_with_modus_ponens(formula):
                self.add_proven(formula)
                print(str(formula) + " is proven by modus ponens")
                continue

            print(str(formula) + " <-- This formula cannot be derived")
            # invalid proof step
            return False

        return True
