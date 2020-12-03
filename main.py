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


def test_case_11():
    # This test case should return True

    a = Variable("a")
    b = Variable("b")
    c = Variable("c")
    d = Variable("d")

    assumptions = [
        a,
        Implies(a, b),
        Implies(b, c)
    ]

    proof = [
        # MP
        b,
        # MP
        c,
        # Axiom 1
        Implies(c, Implies(Not(d), c)),
        # MP
        Implies(Not(d), c)
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


def test_case_12():
    # This test case should return True

    a = Variable("a")
    b = Variable("b")
    c = Variable("c")

    assumptions = [
        Implies(a, b),
        Implies(b, c)
    ]

    proof = prove_implication_transitivity(a, b, c)

    test = Proof(assumptions, proof)

    return test.verify()


def test_case_13():
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

    test = Proof(assumptions, proof)

    return test.verify()


def run_test(test_case, expected):
    print("Starting test case", test_case, "...")

    result = test_case()

    print("Proof correct:", result)

    assert result == expected, "Test " + str(test_case) + " failed!"

    print("Test " + str(test_case) + " passed!")
    print("")


if __name__ == "__main__":

    run_test(test_case_1, False)
    run_test(test_case_2, True)
    run_test(test_case_3, True)
    run_test(test_case_4, True)
    run_test(test_case_5, True)
    run_test(test_case_6, False)
    run_test(test_case_7, True)
    run_test(test_case_8, False)
    run_test(test_case_9, True)
    run_test(test_case_10, True)
    run_test(test_case_11, True)
    run_test(test_case_12, True)
    run_test(test_case_13, True)

    print("All tests passed!")
