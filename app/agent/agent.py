from langchain.agents import create_agent

from app.agent.llm import llm
from app.agent.tools import TOOLS
from app.agent.prompts import SYSTEM_PROMPT

financial_agent = create_agent(model=llm,tools=TOOLS,system_prompt=SYSTEM_PROMPT)