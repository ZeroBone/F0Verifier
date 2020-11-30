from formula import *


class Proof:

    def __init__(self, assumptions: list, proof: list):
        self.assumptions = set(assumptions)
        self.proof = proof

    def verify(self):

        # key: the formula that may be derived using modus ponens
        # value:
        backImplications = {}

        for formula in self.proof:

            if formula.is_axiom():
                continue

            if formula in self.assumptions:
                continue

            # invalid proof step
            return False

        return True
