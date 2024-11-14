import os
import unittest
import subprocess
from ai_coder import AiCoder

class DevelopingAcceptanceTests(unittest.TestCase):

    def test_assistant_makes_hello_world_from_test(self):

        pello_file = open('resources/Pello.py', 'r')
        code = pello_file.read()
        pello_file.close()

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
        AttributeError: 'HelloWorld' object has no attribute 'print'

        ----------------------------------------------------------------------
        Ran 1 test in 0.001s

        FAILED (errors=1)
        """
        assistant = AiCoder()
        diff = assistant.make_diff(code, test_results)

        temp_file = open('resources/PelloTemp.py', 'w')
        temp_file.write(code)
        assistant.apply_diff(temp_file, diff)
        temp_file.close()

        result = subprocess.run(['python', 'resources/PelloTemp.py'], capture_output=True, text=True)
        assert(result.stdout.strip() == "Hello World!")

    def tearDown(self):
        self.cleanup_temp_file()

    def cleanup_temp_file(self):
        try:
            os.remove('resources/PelloTemp.py')
        except OSError as e:
            print(f"Error: {e.strerror}")
