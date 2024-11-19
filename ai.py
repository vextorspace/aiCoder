import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

import unittest

load_dotenv()

class Ai:
    def __init__(self):
        self.llm = ChatOpenAI(
            model_name="gpt-4o",
            temperature=0,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )

    def get_code_diff(self, code, test_results):
        prompt_template = """
                            You are a terse and efficient developer.
                            You make code work with minimal fuss.
                            You write short but descriptive names for functions.
                            You will not write the output with code block markers.
                            Your task is to create a diff that will patch the current file to make the tests pass without modifying the tests.
                               the current source file is: {code}
                               the test results are: {test_results}

                            An example diff would be something like:
                            diff
                            @@ -1,3 +1,3 @@
                            -print('Hello World!')
                            +print('Hello Universe!')
                        """

        commit_prompt = ChatPromptTemplate.from_template(prompt_template)

        # Create the chain
        commit_chain = commit_prompt | self.llm

        # Run the chain
        commit = commit_chain.invoke({"code": code, "test_results": test_results})
        return commit.content.strip()

class TestAi(unittest.TestCase):
    def test_loads_environment_variables(self):
        ai = Ai()
        assert(bool(os.getenv('OPENAI_API_KEY')))

    def test_get_commit_message(self):
        ai = Ai()
        message = ai.get_code_diff("print('Hello World!')", "test failed because it should say Hello Hippo!")

        self.assertTrue(message.startswith("diff"), f"{message} does not start with 'diff'")
        self.assertIn("-print('Hello World!')", message)
        self.assertIn("+print('Hello Hippo!')", message)

    def test_get_commit_message_realistic(self):
        ai = Ai()
        file = open("resources/Pello.py", "r")
        code = file.read()
        file.close()

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
        message = ai.get_code_diff(code, test_results)

        self.assertTrue(message.startswith("diff"), f"{message} does not start with 'diff'")
        self.assertIn("+    def print(self):", message)
        self.assertIn("+        print(\"Hello World!\")", message)
