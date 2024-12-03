import unittest
from ai_coder import TestAi

import sys

def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(TestAi))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    result = runner.run(suite())
    sys.exit(not result.wasSuccessful())
