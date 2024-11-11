import unittest

class AiCoder:
    def __init__(self):
        pass


class TestAiCoder(unittest.TestCase):
    def setUp(self):
        self.ai_coder = AiCoder()

    def test_ai_coder(self):
        self.assertTrue(self.ai_coder)

    def tearDown(self):
        self.ai_coder = None
