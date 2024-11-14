import unittest
from ai_coder import TestAiCoder
from ai_diff_gen import TestAiDiffGen
from ai import TestAi

import sys

def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(TestAiCoder))
    suite.addTests(loader.loadTestsFromTestCase(TestAiDiffGen))
    suite.addTests(loader.loadTestsFromTestCase(TestAi))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    result = runner.run(suite())
    sys.exit(not result.wasSuccessful())
