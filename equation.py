class Equation():
    def __init__(self, eq):
        self.eq = eq
        self._isBalanced  = False
        self._left = self._right = {}

    def print(self):
        return self.eq

