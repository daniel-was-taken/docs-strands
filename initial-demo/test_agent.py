from strands import Agent

agent = Agent(system_prompt="You are a helpful assistant that provides information about the world.", model="eu.anthropic.claude-sonnet-4-5-20250929-v1:0")

print(agent("What is the capital of France?"))