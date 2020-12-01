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
        # value: formula from which the key can be derived with modus ponens
        self.modus_ponens = {}

    # Adds the formula to the set of already proven formulas
    # and makes sure that the possible modus ponens rules are also registered
    def add_proven(self, formula: Formula):

        self.proven.add(formula)

        if formula.kind == FormulaType.IMPLICATION:

            assert isinstance(formula, Implies)

            # check that this right hand side hasn't already been proven
            if formula.get_right() not in self.modus_ponens:
                self.modus_ponens[formula.get_right()] = formula.get_left()

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
            if formula in self.modus_ponens and self.modus_ponens[formula] in self.proven:
                self.add_proven(formula)
                print(str(formula) + " is proven by modus ponens")
                continue

            print(str(formula) + " <-- This formula cannot be derived")
            # invalid proof step
            return False

        return True
