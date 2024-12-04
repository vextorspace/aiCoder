import os
import subprocess
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

import unittest

load_dotenv()

class AiCoder:
    def __init__(self):
        self.llm = ChatOpenAI(
            model_name="gpt-4o",
            temperature=0,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )

    def modify_code(self, code, test_results):
        prompt_template = """
                            You are a terse and efficient developer.
                            You make code work with minimal fuss.
                            You do not solve problems that aren't already defined by the tests.
                            You write short but descriptive names for functions.
                            You will not write the output with code block markers.
                            Your task is to modify the current code to make the tests pass. You may not modify the tests.
                               the current source file is: {code}
                               the test results are: {test_results}

                            The output should not contain any extraneous description of what it is, only code written in the same language as the tests and original code.

                            Do not add or remove any tests.
                            make sure to include the original tests un-modified and do not modify any code that does not need to be modified. In all cases, the code comes before the tests.

                        """

        commit_prompt = ChatPromptTemplate.from_template(prompt_template)

        # Create the chain
        commit_chain = commit_prompt | self.llm

        # Run the chain
        commit = commit_chain.invoke({"code": code, "test_results": test_results})
        return commit.content.strip()

class TestAi(unittest.TestCase):
    def test_loads_environment_variables(self):
        ai = AiCoder()
        assert(bool(os.getenv('OPENAI_API_KEY')))

    def test_modify_code_realistic(self):
        ai = AiCoder()
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
        new_code = ai.modify_code(code, test_results)

        with open('resources/PelloTemp2.py', 'w') as file:
                    file.write(new_code)

        result = subprocess.run(['python', 'resources/PelloTemp2.py'], capture_output=True, text=True)

        self.assertIn("Hello World!", result.stdout)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: ai_coder file_path test_results")
    else:
        file_path = sys.argv[1]
        test_results = sys.argv[2]
        with open(file_path, 'r') as file:
            code = file.read()

            ai = AiCoder()
            new_code = ai.modify_code(code, test_results)

            with open(file_path, 'w') as file:
                file.write(new_code)
