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


    print("Test case1: ", test_case_1())
    print("Test case2: ", test_case_2())
