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

async def main():
	if len(sys.argv) < 2:
		print("Usage: python3 RunDemo.py '<your prompt>'")
		return

	prompt = sys.argv[1]

	agent = Agent(
		task=prompt,
		llm=llm,
	)

	await agent.run()

if __name__ == '__main__':
	asyncio.run(main())