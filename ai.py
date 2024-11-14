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
                            Your task is to create a diff that will patch the current file to make the tests pass.
                               the current source file is: {code}
                               the test results are: {test_results}
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
        message = ai.get_code_diff("print('Hello World!')", "test failed because it should say Hello Hippo!").strip()
        assert("hippo" in message.lower())
