import io
import sys
import unittest

class HelloWorld:
    def __init__(self):
        pass

class TestHelloWorld(unittest.TestCase):
    def test_hello_world_prints(self):
        output = io.StringIO()

        HelloWorld().print()

        captured_output = output.getvalue()

        self.assertEqual(captured_output.strip(), "Hello World!")

if __name__ == '__main__':
    HelloWorld().print()
