from langchain.callbacks import get_openai_callback
from langchain.agents import initialize_agent, load_tools
from langchain.llms import OpenAI

# Initialize OpenAI language model
llm = OpenAI(temperature=0.1)

# Load necessary tools for the agent
tools = load_tools(["serpapi"], llm)

# Initialize the agent with tools and the OpenAI language model
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

# Define the query
query = "What is the most universal meaning of life?"

# Use OpenAI callback to calculate cost
with get_openai_callback() as cb:
    response = agent.run(query)

    # Print the response and cost details
    print("\nResponse:", response)
    print(f"Tokens: {cb.total_tokens}")
    print(f"Cost [USD]: ${cb.total_cost:.5f}")
