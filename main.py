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


def test_case_5():
    # This test case should return True

    a = Variable("a")
    b = Variable("b")
    c = Variable("c")

    assumptions = [
        a,
        Implies(a, b),
        Implies(b, c)
    ]

    proof = [
        b,
        c
    ]

    test = Proof(assumptions, proof)

    return test.verify()


def test_case_6():
    # This test case should return False

    a = Variable("a")
    b = Variable("b")
    c = Variable("c")

    assumptions = [
        a,
        Implies(a, b),
        Implies(b, c)
    ]

    proof = [
        c,
        b
    ]

    test = Proof(assumptions, proof)

    return test.verify()


def test_case_7():
    # This test case should return True

    a = Variable("a")
    b = Variable("b")

    assumptions = [
        a
    ]

    proof = [
        Implies(
            Implies(Not(a), Not(b)),
            Implies(b, a)
        ),
        Implies(a, Implies(b, a)),
        Implies(b, a)
    ]

    test = Proof(assumptions, proof)

    return test.verify()


def test_case_8():
    # This test case should return False

    a = Variable("a")
    b = Variable("b")

    assumptions = [
        a
    ]

    proof = [
        Implies(
            Implies(Not(a), Not(b)),
            Implies(b, a)
        ),
        Implies(b, a)
    ]

    test = Proof(assumptions, proof)

    return test.verify()


if __name__ == "__main__":
    print("Test case 1:")
    t1 = test_case_1()
    print("Proof correct: ", t1)
    assert not t1, "Test 1 failed"

    print("Test case 2:")
    t2 = test_case_2()
    print("Proof correct: ", t2)
    assert t2, "Test 2 failed"

    print("Test case 3:")
    t3 = test_case_3()
    print("Proof correct: ", t3)
    assert t3, "Test 3 failed"

    print("Test case 4:")
    t4 = test_case_4()
    print("Proof correct: ", t4)
    assert t4, "Test 4 failed"

    print("Test case 5:")
    t5 = test_case_5()
    print("Proof correct: ", t5)
    assert t5, "Test 5 failed"

    print("Test case 6:")
    t6 = test_case_6()
    print("Proof correct: ", t6)
    assert not t6, "Test 6 failed"

    print("Test case 7:")
    t7 = test_case_7()
    print("Proof correct: ", t7)
    assert t7, "Test 7 failed"

    print("Test case 8:")
    t8 = test_case_8()
    print("Proof correct: ", t8)
    assert not t8, "Test 8 failed"

    print("---")
    print("All tests passed!")
