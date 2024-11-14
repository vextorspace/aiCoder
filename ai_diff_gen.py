import unittest

class AiDiffGen:
    def __init__(self):
        pass

    def make_diff(self, code, test_results):
        return "diff"

class TestAiDiffGen(unittest.TestCase):
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
        diff = AiDiffGen().make_diff(code, test_results)
        assert(diff.strip().startswith("diff"))
