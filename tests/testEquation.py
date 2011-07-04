import unittest
from equation import *

class testEquation(unittest.TestCase):
    def setUp(self):
        self.eqText = 'H2 + O2 -> H2O'
        self.left = {
            'H2': {
                'coef': None,
                'H': 2
            },
            'O2': {
                'coef': None,
                'O': 2
            }
        }
        self.right = {
            'H2O': {
                'coef': None,
                'H': 2,
                'O': 1
            }
        }
        self.goodEquations = [
            'H2 + O2 -> H2O',
            'P2I4 + H3PO4 = P4 + H2O + PH4I',
            'Na + Cl2 > NaCl',
            'Cu(OH)2 + H2S -> CuS H2O',
            'Cu + S > CuS',
            'Mg + H3PO4 = Mg3(PO4)2 H2',
            'MgO + H3PO4 -> Mg3(PO4)2 + H2O',
            'Mg(OH)2 + H3PO4 -> Mg3(PO4)2 + H2O',
            'MgO + P4O10 -> Mg3(PO4)2',
            'Mg(OH)2 P4O10 -> Mg3(PO4)2 + H2O',
            '[Cr(N2H4CO)6]4[Cr(CN)6]3 KMnO4 H2SO4 -> K2Cr2O7 MnSO4 CO2 KNO3 K2SO4 H2O',
            'H2 Ca(CN)2 NaAlF4 FeSO4 MgSiO3 KI H3PO4 PbCrO4 BrCl CF2Cl2 SO2 -> PbBr2 CrCl3 MgCO3 KAl(OH)4 Fe(SCN)3 PI3 Na2SiO3 CaF2 H2O',
        ]
        self.badEquations = [
            'MgO + P4O10 Mg3(PO4)2',    # no left/right side separator
            'CU + s = CUs'              # elements written in wrong case
        ]

    def testInit(self):
        """
            Tests creation of Equation objects

            At first, they are not balanced thus _isBalanced == False and
            the coefficients are None. __init__ method immediately creates the _left and _right
            dictionary structures
        """
        equation = Equation(self.eqText)

        self.assertEqual(self.eqText, equation.print(), 'Prints the original equation')
        self.assertEqual(equation._isBalanced, False)
        self.assertEqual(equation._left, self.left, 'Left variable is a dictionary')
        self.assertEqual(equation._right, self.right, 'Right variable is a dictionary')

    def testGoodEquations(self):
        """
            Every equation on the goodEquations list should pass the regexp test
        """
        for eq in self.goodEquations:
            equation = Equation(eq)
            self.assertEqual(equation.eq, eq, 'If the regex passed, eqs will be the same here')


suite = unittest.TestLoader().loadTestsFromTestCase(testEquation)
unittest.TextTestRunner(verbosity=2).run(suite)