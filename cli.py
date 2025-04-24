from agno.models.openai import OpenAIChat
import asyncio
from agno.tools.mcp import MCPTools
from agno.utils.pprint import apprint_run_response
from agno.agent import Agent
from dotenv import load_dotenv

load_dotenv()

async def run_agent(message: str) -> None:
    async with MCPTools(
        "npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt"
    ) as mcp_tools:
        agent = Agent(
            model=OpenAIChat(id="gpt-4o"),
            tools=[mcp_tools],
            markdown=True,
        )

        response_stream = await agent.arun(message, stream=True)
        await apprint_run_response(response_stream, markdown=True)
if __name__ == "__main__":
    asyncio.run(
        run_agent(
            "What listings are available in Kuala Lumpur for 6 people for 2 nights from 22 to 24 May 2025? Also give me the hotel name and the price and the location of the hotel and rating of the hotel in tabular format. Also give the contact number of the hotel and the exact address of the hotel."
        )
    )