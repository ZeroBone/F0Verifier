from variable import Variable
from implies import Implies
from negation import Not
from proof import Proof


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


def test_case_4():
    # This test case should return True

    a = Variable("a")

    na = Not(a)
    nna = Not(na)
    nnna = Not(nna)
    nnnna = Not(nnna)

    assumptions = [
        nna
    ]

    proof = [
        # Axiom 1
        Implies(nna, Implies(nnnna, nna)),
        # Modus ponens on the last step and the assumption
        Implies(nnnna, nna),
        # Axiom 3
        Implies(Implies(nnnna, nna), Implies(na, nnna)),
        # Modus ponens on the last 2 steps
        Implies(na, nnna),
        # Axiom 3
        Implies(Implies(na, nnna), Implies(nna, a)),
        # Modus ponens on the last 2 steps
        Implies(nna, a),
        # Modus ponens on the last step and the assumption
        a
    ]

    test = Proof(assumptions, proof)

    return test.verify()


if __name__ == "__main__":
    print("Test case 1: ", test_case_1())
    print("---")
    print("Test case 2: ", test_case_2())
    print("---")
    print("Test case 3: ", test_case_3())
    print("---")
    print("Test case 4: ", test_case_4())
