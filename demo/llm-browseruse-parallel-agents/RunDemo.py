import os
import sys
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio

import dotenv

from browser_use import Agent

dotenv.load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

prompt1 = """
Go to http://eaapp.somee.com 
Then close browser
"""

prompt2 = """
Go to http://saucedemo.com and perform login with standard user
Close browser in the end
"""

prompt3 = """
Go to http://saucedemo.com and perform login with standard user
Then log off from site
Close browser in the end
"""

prompt4 = """
Go to http://saucedemo.com and perform login with locked_out_user
Verify error occurs with message says 'this user has been locked out.'
Close browser in the end
"""
async def run_agent(prompt, model):
	agent = Agent(
		task=prompt,
		llm=ChatGoogleGenerativeAI(model=model, api_key=SecretStr(api_key))
	)
	result = await agent.run()
	print(result)

async def main():
	tasks = [
		run_agent(prompt1, "gemini-2.0-flash"),
		run_agent(prompt2, "gemini-2.0-flash"),
		run_agent(prompt3, "gemini-2.0-flash"),
		run_agent(prompt4, "gemini-2.0-flash")	]

	results = await asyncio.gather(*tasks, return_exceptions=False)
	print(results)

asyncio.run(main())