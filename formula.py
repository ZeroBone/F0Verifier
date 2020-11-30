from enum import Enum


class FormulaType(Enum):
    VARIABLE = 1
    IMPLICATION = 2
    NEGATION = 3


class Formula:

    def __init__(self, kind):
        self.kind = kind

    def __str__(self):
        raise RuntimeError("Raw formula cannot be converted to a string")

    def __hash__(self):
        return hash(self.kind)

    def __eq__(self, other):
        return self.kind == other.kind

    def modus_ponens(self, a, b):
        pass

    def is_axiom1(self):

        if self.kind != FormulaType.IMPLICATION:
            return False

        p = self.get_left()
        q_implies_p = self.get_right()

        if q_implies_p.kind != FormulaType.IMPLICATION:
            return False

        q_implies_p_p = q_implies_p.get_right()

        return p.is_equal(q_implies_p_p)

    def is_axiom2(self):

        if self.kind != FormulaType.IMPLICATION:
            return False

        left = self.get_left()
        right = self.get_right()

        if left.kind != FormulaType.IMPLICATION or right.kind != FormulaType.IMPLICATION:
            return False

        p = left.get_left()
        q_implies_r = left.get_right()
        p_implies_q = right.get_left()
        p_implies_r = right.get_right()

        if (q_implies_r.kind != FormulaType.IMPLICATION
                or p_implies_q.kind != FormulaType.IMPLICATION
                or p_implies_r.kind != FormulaType.IMPLICATION):
            return False

        q_implies_r_q = q_implies_r.get_left()
        q_implies_r_r = q_implies_r.get_right()

        p_implies_q_p = p_implies_q.get_left()
        p_implies_q_q = p_implies_q.get_right()

        p_implies_r_p = p_implies_r.get_left()
        p_implies_r_r = p_implies_r.get_right()

        return (
                p.is_equal(p_implies_q_p) and
                p.is_equal(p_implies_r_p) and
                q_implies_r_q.is_equal(p_implies_q_q) and
                q_implies_r_r.is_equal(p_implies_r_r)
        )

    def is_axiom3(self):

        if self.kind != FormulaType.IMPLICATION:
            return False

        notp_implies_notq = self.get_left()
        q_implies_p = self.get_right()

        if (notp_implies_notq.kind != FormulaType.IMPLICATION
                or q_implies_p.kind != FormulaType.IMPLICATION):
            return False

        not_p = notp_implies_notq.get_left()
        not_q = notp_implies_notq.get_right()

        if not_p.kind != FormulaType.NEGATION or not_q.kind != FormulaType.NEGATION:
            return False

        q = q_implies_p.get_left()
        p = q_implies_p.get_right()

        return not_q.get_form().is_equal(q) and not_p.get_form().is_equal(p)

    def is_axiom(self):
        return self.is_axiom1() or self.is_axiom2() or self.is_axiom3()

    def is_equal(self, formula):
        return self == formula
