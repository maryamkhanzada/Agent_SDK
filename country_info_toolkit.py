from agents import Agent, Runner
import asyncio

# Tool Agent 1: Capital of a country
capital_agent = Agent(
    name="CapitalToolAgent",
    instructions="You are a bot that tells the capital of a given country.",
    tools=[],
)

# Tool Agent 2: Language of a country
language_agent = Agent(
    name="LanguageToolAgent",
    instructions="You are a bot that tells the official language of a given country.",
    tools=[],
)

# Tool Agent 3: Population of a country
population_agent = Agent(
    name="PopulationToolAgent",
    instructions="You are a bot that tells the population of a given country.",
    tools=[],
)

# Orchestrator Agent
orchestrator_agent = Agent(
    name="CountryOrchestratorAgent",
    instructions=(
        "You are a smart assistant. Take a country name from the user and use the 3 tools "
        "(CapitalToolAgent, LanguageToolAgent, PopulationToolAgent) to provide full information."
    ),
    tools=[capital_agent, language_agent, population_agent],
)

# Runner
async def main():
    country_name = input("Enter a country name: ")
    result = await Runner.run(orchestrator_agent, country_name)
    print("\n📍 Country Info:")
    print(result.output)

if __name__ == "__main__":
    asyncio.run(main())
