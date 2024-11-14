import unittest

class AiCoder:
    def __init__(self):
        pass

    def make_diff(self, code, test_results):
        return "diff"

class TestAiCoder(unittest.TestCase):
    def setUp(self):
        self.ai_coder = AiCoder()

    def test_ai_coder(self):
        self.assertTrue(self.ai_coder)

    def test_make_diff_returns_actual_diff(self):
        code = "print('Hello World!')"
        test_results = """
        (aimaster) vextorspace@vNitro:~/repos/aiCoder$ python resources/Pello.py
        E
        ======================================================================
        ERROR: test_hello_world_prints (__main__.TestHelloWorld.test_hello_world_prints)
        ----------------------------------------------------------------------
        Traceback (most recent call last):
          File "/home/vextorspace/repos/aiCoder/resources/Pello.py", line 13, in test_hello_world_prints
            HelloWorld().print()
            ^^^^^^^^^^^^^^^^^^
        """
        diff = self.ai_coder.make_diff(code, test_results)
        assert(diff.strip().startswith("diff"))

    def tearDown(self):
        self.ai_coder = None
