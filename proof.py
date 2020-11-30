from formula import *


class Proof:

    def __init__(self, assumptions: list, proof: list):
        self.assumptions = set(assumptions)
        self.proof = proof
        # set of already proven formulas
        self.proven = set()
        self.modus_ponens = {}

    def add_proven(self, formula):

        self.proven.add(formula)

        if formula.kind == FormulaType.IMPLICATION:
            # check that this right hand side hasn't already been proven
            if formula.get_right() not in self.modus_ponens:
                self.modus_ponens[formula.get_right()] = formula.get_left()

    def verify(self):

        for formula in self.assumptions:
            self.add_proven(formula)

        for formula in self.proof:

            if formula.is_axiom():
                self.add_proven(formula)
                print(str(formula) + " is an axiom")
                continue

            if formula in self.proven:
                print(str(formula) + " is already proven")
                continue

            # check whether modus ponens was applied in this step
            if formula in self.modus_ponens and self.modus_ponens[formula] in self.proven:
                self.add_proven(formula)
                print(str(formula) + " is proven by modus ponens")
                continue

            print(str(formula) + " <-- Invalid proof step")
            # invalid proof step
            return False

        return True
