import unittest
from ai_coder import TestAiCoder

def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(TestAiCoder))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    result = runner.run(suite())
