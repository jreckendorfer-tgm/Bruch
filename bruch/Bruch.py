class Bruch(object):
    def __init__(self, zaehler, nenner=None):
        """
        Initialize fractions in different ways
        :param zaehler: num
        :param nenner: denom
        """
        # Exception handling
        if nenner == 0:
            raise ZeroDivisionError
        if isinstance(zaehler, float) or isinstance(nenner, float):
            raise TypeError

        if nenner is not None:
            self.zaehler = zaehler
            self.nenner = nenner
        elif nenner is None and isinstance(zaehler, int):
            self.zaehler = zaehler
            self.nenner = 1
        else:
            self.zaehler = zaehler.zaehler
            self.nenner = zaehler.nenner

    # COMPARE
    def __eq__(self, other):
        """
        returns true if equals
        :param other: other fraction
        :return: euqality
        """
        return float(self) == other

    def __ge__(self, other):
        """
        greater than or equals
        :param other: other fraction
        :return: true/false
        """
        return float(self) >= float(other)

    def __le__(self, other):
        """
        less than or equals
        :param other: other fraction
        :return: true/false
        """
        return float(self) <= float(other)

    def __lt__(self, other):
        """
        less than
        :param other: other fraction
        :return: true/false
        """
        return float(self) < float(other)

    def __gt__(self, other):
        """
        graeter than
        :param other: other fraction
        :return: true/false
        """
        return float(self) > float(other)

    def __float__(self):
        """
        return fraction as float
        :return: float value of fraction
        """
        return self.zaehler / self.nenner

    def __int__(self):
        """
        return int value of fraction
        :return: int value of fraction
        """
        return int(self.zaehler / self.nenner)

    def __invert__(self):
        """
        returns inverted fraction
        :return: inverted fraction
        """
        return Bruch(self.nenner, self.zaehler)

    def __str__(self):
        """
        return fraction as string
        :return: fraction as string
        """
        if self.nenner == 1:
            return '(' + str(self.zaehler) + ')'
        elif self.zaehler < 0 and self.nenner < 0:
            self = abs(self)
        return str('(' + str(self.zaehler) + '/' + str(self.nenner) + ')')

    def __abs__(self):
        """
        return fraction as positiv (no minus)
        :return:
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __neg__(self):
        """
        negate fraction
        :return: negated fraction
        """
        return Bruch(self.zaehler * (-1), self.nenner)

    def __pow__(self, power, modulo=None):
        """
        returns frations with a specified power
        :param power: power
        :param modulo:
        :return: fration with a specified power
        """
        return Bruch(self.zaehler ** power, self.nenner ** power)

    def _Bruch__makeBruch(value):
        """
        make fraction out of a single value
        :return: Bruch
        """
        if isinstance(value, str):
            raise TypeError
        else:
            return Bruch(value, value)

    # ADD
    def __add__(self, other):
        """
        add two fractions together
        :param other: other fraction
        :return: addition
        """
        other = Bruch(other)
        return Bruch(self.zaehler * other.nenner + other.zaehler * self.nenner, self.nenner * other.nenner)

    def __iadd__(self, other):
        """
        add fraction with += notation
        :param other: other fraction
        :return: addition
        """
        if isinstance(other, (float, str)):
            raise TypeError
        return self + other

    def __radd__(self, other):
        """
        add normal number to fraction
        :param other: normal number
        :return: addition
        """
        return Bruch(self.zaehler * other, self.nenner)

    # SUBTRACT
    def __sub__(self, other):
        """
        subtract fractions
        :param other: other fraction
        :return: fraction
        """
        other = Bruch(other)
        return Bruch(self.zaehler * other.nenner - other.zaehler * self.nenner, self.nenner * other.nenner)

    def __isub__(self, other):
        """
        substract fractions with -=
        :param other:
        :return: fraction
        """
        if isinstance(other, (float, str)):
            raise TypeError
        other = Bruch(other)
        return self - other

    def __rsub__(self, other):
        """
        substract number from fraction
        :param other: normal number
        :return: fraction
        """
        if isinstance(other, (float, str)):
            raise TypeError
        return Bruch(other) - self

    # MULTIPLY
    def __mul__(self, other):
        """
        multiply tow fractions
        :param other: other fraction
        :return: two function multiplied
        """
        other = Bruch(other)
        return Bruch(self.zaehler * other.zaehler, self.nenner * other.nenner)

    def __rmul__(self, other):
        """
        multiply tow fractions
        :param other: other fraction
        :return: two function multiplied
        """
        return Bruch(other) * self

    def __imul__(self, other):
        """
        multiply with \*=
        :param other: other fraction or number
        :return: fraction
        """
        if isinstance(other, (float, str)):
            raise TypeError
        return Bruch(other) * self

    # DIVIDE
    def __truediv__(self, other):
        """
        Devide two fractions
        :param other: other fraction
        :return: division
        """
        return Bruch(self.zaehler * Bruch(other).nenner, self.nenner * Bruch(other).zaehler)

    def __rtruediv__(self, other):
        """
        Inverted devition of frations
        :param other: other fraction
        :return: division
        """
        other = Bruch(other)
        return ~(self / other)

    def __itruediv__(self, other):
        """
        divide with /=
        :param other:
        :return:
        """
        if isinstance(other, (float, str)):
            raise TypeError
        return self / Bruch(other)

    def __iter__(self):
        """
        Return fractions in lists
        :return: list elements
        """
        lst = [self.zaehler, self.nenner]
        for x in lst:
            yield x
