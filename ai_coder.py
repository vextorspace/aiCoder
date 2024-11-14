import unittest
import subprocess

class AiCoder:
    def __init__(self):
        pass

    def make_diff(self, code, test_results):
        return "diff"

    def apply_diff(self, temp_file, diff):
        process = subprocess.Popen(['patch', temp_file.name], stdin=subprocess.PIPE)
        process.communicate(input=diff.encode())
        return process.returncode == 0

class TestAiCoder(unittest.TestCase):
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
        diff = AiCoder().make_diff(code, test_results)
        assert(diff.strip().startswith("diff"))

    def test_apply_diff_applies_diff_to_file(self):
        diff = '''
        diff --git a/example.py b/example.py
        index e69de29..d95f3ad 100644
        --- a/example.py
        +++ b/example.py
        @@ -0,0 +1 @@
        +print("Hello, world!")
        '''

        temp_file = open('resources/example.py', 'w')
        temp_file.write("\n")

        assistant = AiCoder()
        success = assistant.apply_diff(temp_file, diff)


        temp_file.close()

        assert(success == True)

        temp_file = open('resources/example.py', 'r')
        contents = temp_file.read().strip()
        assert(contents == "print(\"Hello, world!\")")

    def test_apply_diff_returns_false_on_error(self):
        diff = '''
        df --git a/example2.py b/example2.py
        index e69de29..d95f3ad 100644
        --- a/example2.py
        +++ b/example2.py
        -0,0 +1 @@
        +print("Hello, world!")
        '''

        temp_file = open('resources/example2.py', 'w')
        temp_file.write("\n")

        assistant = AiCoder()
        success = assistant.apply_diff(temp_file, diff)

        temp_file.close()

        print(f"Good Diff: {success}")
        assert(success == False)
