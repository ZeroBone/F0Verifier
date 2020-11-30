from variable import Variable
from implies import Implies
from proof import Proof


if __name__ == "__main__":
    def test_case_1():
        # This test case should return False
        a = Variable("a")
        b = Variable("b")
        test = Proof([a, b], [a, b, Implies(a, b)])
        return test.verify()


    def test_case_2():
        # This test case should return True
        a = Variable("a")
        b = Variable("b")
        assumptions = [a, b]
        proof = [a, b, Implies(a, Implies(b, a))]
        test = Proof(assumptions, proof)
        return test.verify()

    def test_case_3():
        # This test case should return True

        a = Variable("a")

        assumptions = []

        proof = [
            # Axiom 2 with a -> a instead of q
            Implies(
                Implies(a, Implies(Implies(a, a), a)),
                Implies(Implies(a, Implies(a, a)), Implies(a, a))
            ),
            # Axiom 1 with a -> a instead of q
            Implies(a, Implies(Implies(a, a), a)),
            # Modus ponens of the first 2 axioms
            Implies(Implies(a, Implies(a, a)), Implies(a, a)),
            # Axiom 1
            Implies(a, Implies(a, a)),
            # Modus ponens
            Implies(a, a)
        ]

        test = Proof(assumptions, proof)

        return test.verify()

    print("Test case 1: ", test_case_1())
    print("Test case 2: ", test_case_2())
    print("Test case 3: ", test_case_3())
