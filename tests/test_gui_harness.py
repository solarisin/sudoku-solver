import unittest
import xmlrunner
from tests.test_ui import TestSudokuGUI
from tests.test_logic import TestSudokuSolver

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestSudokuGUI))
    test_suite.addTest(unittest.makeSuite(TestSudokuSolver))

    with open('test-reports/test-results.xml', 'wb') as output:
        xmlrunner.XMLTestRunner(output=output).run(test_suite)
