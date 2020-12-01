from enum import Enum


class FormulaType(Enum):
    VARIABLE = 1
    IMPLICATION = 2
    NEGATION = 3


class Formula:

    def __init__(self, kind):
        self.kind = kind

    # str for this abstract class should not be called
    def __str__(self):
        raise RuntimeError("Raw formula cannot be converted to a string")

    def __hash__(self):
        return hash(self.kind)

    # the overloaded == will compare, whether the formulas are of the same type
    def __eq__(self, other):
        return self.kind == other.kind

    # checks whether the formula is the p -> (q -> p) axiom
    def is_axiom1(self) -> bool:

        from implies import Implies

        if self.kind != FormulaType.IMPLICATION:
            return False

        assert isinstance(self, Implies)

        p = self.get_left()
        q_implies_p = self.get_right()

        if q_implies_p.kind != FormulaType.IMPLICATION:
            return False

        assert isinstance(q_implies_p, Implies)

        q_implies_p_p = q_implies_p.get_right()

        return p == q_implies_p_p

    # checks whether the formula is the (p -> (q -> r)) -> ((p -> q) -> (p -> r)) axiom
    def is_axiom2(self) -> bool:

        from implies import Implies

        if self.kind != FormulaType.IMPLICATION:
            return False

        assert isinstance(self, Implies)

        left = self.get_left()
        right = self.get_right()

        if left.kind != FormulaType.IMPLICATION or right.kind != FormulaType.IMPLICATION:
            return False

        assert isinstance(left, Implies)
        assert isinstance(right, Implies)

        p = left.get_left()
        q_implies_r = left.get_right()
        p_implies_q = right.get_left()
        p_implies_r = right.get_right()

        if (q_implies_r.kind != FormulaType.IMPLICATION
                or p_implies_q.kind != FormulaType.IMPLICATION
                or p_implies_r.kind != FormulaType.IMPLICATION):
            return False

        assert isinstance(q_implies_r, Implies)
        assert isinstance(p_implies_q, Implies)
        assert isinstance(p_implies_r, Implies)

        q_implies_r_q = q_implies_r.get_left()
        q_implies_r_r = q_implies_r.get_right()

        p_implies_q_p = p_implies_q.get_left()
        p_implies_q_q = p_implies_q.get_right()

        p_implies_r_p = p_implies_r.get_left()
        p_implies_r_r = p_implies_r.get_right()

        return (
                p == p_implies_q_p and
                p == p_implies_r_p and
                q_implies_r_q == p_implies_q_q and
                q_implies_r_r == p_implies_r_r
        )

    # checks whether the formula is the (!p -> !q) -> (q -> p) axiom
    def is_axiom3(self) -> bool:

        from negation import Not
        from implies import Implies

        if self.kind != FormulaType.IMPLICATION:
            return False

        assert isinstance(self, Implies)

        notp_implies_notq = self.get_left()
        q_implies_p = self.get_right()

        if (notp_implies_notq.kind != FormulaType.IMPLICATION
                or q_implies_p.kind != FormulaType.IMPLICATION):
            return False

        assert isinstance(notp_implies_notq, Implies)
        assert isinstance(q_implies_p, Implies)

        not_p = notp_implies_notq.get_left()
        not_q = notp_implies_notq.get_right()

        if not_p.kind != FormulaType.NEGATION or not_q.kind != FormulaType.NEGATION:
            return False

        q = q_implies_p.get_left()
        p = q_implies_p.get_right()

        assert isinstance(not_q, Not)
        assert isinstance(not_p, Not)

        return not_q.get_form() == q and not_p.get_form() == p

    # returns true if the formula is some axiom and false otherwise
    def is_axiom(self) -> bool:
        return self.is_axiom1() or self.is_axiom2() or self.is_axiom3()
