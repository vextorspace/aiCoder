import unittest
from ai_coder import TestAiCoder
from ai_diff_gen import TestAiDiffGen

import sys

def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(TestAiCoder))
    suite.addTests(loader.loadTestsFromTestCase(TestAiDiffGen))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    result = runner.run(suite())
    sys.exit(not result.wasSuccessful())
