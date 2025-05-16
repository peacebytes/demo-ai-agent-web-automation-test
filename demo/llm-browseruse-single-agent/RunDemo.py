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

# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))

prompt = """
Go to http://eaapp.somee.com and perform login
Then log off from site
Close browser in the end
"""

async def main():
	agent = Agent(
		task=prompt,
		llm=llm,
	)

	await agent.run()

if __name__ == '__main__':
	asyncio.run(main())