from agents import Agent, Runner

# Agent 1: Mood analyzer
class MoodAnalyzerAgent(Agent):
    def __init__(self):
        super().__init__(name="MoodAnalyzer")

    async def run(self, input: str, config):
        mood = input.lower()
        if "sad" in mood or "stressed" in mood:
            return {"mood": "sad"}
        else:
            return {"mood": "happy"}

# Agent 2: Activity suggester
class ActivitySuggesterAgent(Agent):
    def __init__(self):
        super().__init__(name="ActivitySuggester")

    async def run(self, input: dict, config):
        if input["mood"] == "sad":
            return "Take a walk, talk to a friend, or listen to calming music."
        return "Keep enjoying your good mood!"

# Main runner
async def main():
    user_input = input("How are you feeling today? ")

    mood_agent = MoodAnalyzerAgent()
    activity_agent = ActivitySuggesterAgent()

    mood_result = await Runner.run(mood_agent, user_input)
    print("Detected mood:", mood_result["mood"])

    suggestion = await Runner.run(activity_agent, mood_result)
    print("Suggestion:", suggestion)

# Run the main async function
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
