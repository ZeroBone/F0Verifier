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

    proof = [
        a,
        b,
        Implies(a, Implies(b, a))
    ]

    test = Proof(assumptions, proof)

    return test.verify()


def test_case_3():
    # This test case should return True
    # in this test case we prove a -> a

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


def test_case_9():
    # This test case should return True

    a = Variable("a")
    b = Variable("b")
    c = Variable("c")

    na = Not(a)
    nna = Not(na)

    ab = Implies(a, b)
    bc = Implies(b, c)

    assumptions = [
        a,
        Implies(a, nna)
    ]

    proof = [
        nna,
        # Axiom 1
        Implies(
            nna,
            Implies(
                Not(Implies(ab, Not(bc))),
                nna
            )
        ),
        # MP
        Implies(
            Not(Implies(ab, Not(bc))),
            nna
        ),
        # Axiom 3
        Implies(
            Implies(
                Not(Implies(ab, Not(bc))),
                nna
            ),
            Implies(
                na,
                Implies(ab, Not(bc))
            )
        ),
        # MP
        Implies(
            na,
            Implies(ab, Not(bc))
        ),
        # Axiom 2
        Implies(
            Implies(
                na,
                Implies(ab, Not(bc))
            ),
            Implies(
                Implies(na, ab),
                Implies(na, Not(bc))
            )
        ),
        # MP
        Implies(
            Implies(na, ab),
            Implies(na, Not(bc))
        )
    ]

    test = Proof(assumptions, proof)

    return test.verify()


def test_case_10():
    # This test case should return True

    a = Variable("a")
    b = Variable("b")
    c = Variable("c")

    na = Not(a)
    nb = Not(b)

    assumptions = [
        # Proof by contradiction
        Implies(
            Implies(a, b),
            Implies(Implies(a, nb), na)
        ),
        # Proof by contradiction - deduction theorem
        Implies(a, b),
        Implies(a, nb),
        # Implication of inconsistency
        Implies(na, Implies(a, c))
    ]

    proof = [
        Implies(Implies(a, nb), na),
        na,
        Implies(a, c)
    ]

    test = Proof(assumptions, proof)

    return test.verify()


# constructs a proof of a -> c assuming a -> b and b -> c are proven
def prove_implication_transitivity(a, b, c):

    ab = Implies(a, b)
    bc = Implies(b, c)
    ac = Implies(a, c)

    ax2_q = Implies(a, bc)

    ax2_r = Implies(ab, ac)

    return [
        # Axiom 1
        Implies(
            Implies(
                Implies(a, bc),
                Implies(ab, ac)
            ),
            Implies(
                bc,
                Implies(
                    Implies(a, bc),
                    Implies(ab, ac)
                )
            )
        ),
        # Axiom 2
        Implies(
            Implies(a, bc),
            Implies(ab, ac)
        ),
        # Modus ponens
        Implies(
            bc,
            Implies(
                Implies(a, bc),
                Implies(ab, ac)
            )
        ),
        # Axiom 2
        Implies(
            Implies(bc, Implies(ax2_q, ax2_r)),
            Implies(Implies(bc, ax2_q), Implies(bc, ax2_r))
        ),
        # Modus ponens
        Implies(Implies(bc, ax2_q), Implies(bc, ax2_r)),
        # Axiom 1
        Implies(bc, Implies(a, bc)),
        # Modus ponens
        Implies(bc, Implies(ab, ac)),
        # Unfold this formula with modus ponens to get a -> c
        Implies(ab, ac),
        ac
    ]


def test_case_11():
    # This test case should return True

    a = Variable("a")
    b = Variable("a")
    c = Variable("a")

    assumptions = [
        Implies(a, b),
        Implies(a, c)
    ]

    proof = prove_implication_transitivity(a, b, c)

    test = Proof(assumptions, proof)

    return test.verify()


def test_case_12():
    # This test case should return True

    a = Variable("a")

    aa = Implies(a, a)
    a_aa = Implies(a, aa)

    n_a_aa = Not(a_aa)
    nn_a_aa = Not(n_a_aa)

    na = Not(a)
    nna = Not(na)

    assumptions = [
        Implies(
            a_aa,
            Implies(Implies(a_aa, a), a)
        )
    ]

    proof = [
        # Axiom 1
        a_aa,
        # Axiom 3
        Implies(Implies(nn_a_aa, nna), Implies(na, n_a_aa)),
        # Axiom 3
        Implies(Implies(na, n_a_aa), Implies(a_aa, a)),
        # Combine last 2 steps
        *prove_implication_transitivity(
            Implies(nn_a_aa, nna),
            Implies(na, n_a_aa),
            Implies(a_aa, a)
        ),
        # It is now proven that:
        Implies(Implies(nn_a_aa, nna), Implies(a_aa, a)),
        # Axiom 1
        Implies(nna, Implies(nn_a_aa, nna)),
        # Combine last 2 steps
        *prove_implication_transitivity(
            nna,
            Implies(nn_a_aa, nna),
            Implies(a_aa, a)
        ),
        # It is now proven that
        Implies(nna, Implies(a_aa, a)),
        # Modus ponens for the assumption and the first formula
        Implies(Implies(a_aa, a), a),
        # Combine the last step with proof[6]
        *prove_implication_transitivity(
            nna,
            Implies(a_aa, a),
            a
        ),
        # We have proven that
        Implies(nna, a)
    ]

    print(len(proof))

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

    print("Test case 9:")
    t9 = test_case_9()
    print("Proof correct: ", t9)
    assert t9, "Test 9 failed"

    print("Test case 10:")
    t10 = test_case_10()
    print("Proof correct: ", t10)
    assert t10, "Test 10 failed"

    print("Test case 11:")
    t11 = test_case_11()
    print("Proof correct: ", t11)
    assert t11, "Test 11 failed"

    print("Test case 12:")
    t12 = test_case_12()
    print("Proof correct: ", t12)
    assert t12, "Test 12 failed"

    print("---")
    print("All tests passed!")
