from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from agno.tools.yfinance import YFinanceTools
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()



# Load FAISS DBs
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
defense_db = FAISS.load_local(r"vector_db\defence", embeddings, allow_dangerous_deserialization=True)
agriculture_db = FAISS.load_local(r"vector_db\agriculture", embeddings, allow_dangerous_deserialization=True)
railways_db = FAISS.load_local(r"vector_db\railways", embeddings, allow_dangerous_deserialization=True)
finance_db = FAISS.load_local(r"vector_db\fianance", embeddings, allow_dangerous_deserialization=True)

# Define FAISS Retrievers
defense_retriever = defense_db.as_retriever(search_kwargs={"k": 5})
agriculture_retriever = agriculture_db.as_retriever(search_kwargs={"k": 5})
railways_retriever = railways_db.as_retriever(search_kwargs={"k": 5})
finance_retriever = finance_db.as_retriever(search_kwargs={"k": 5})

custom_prompt = ChatPromptTemplate.from_template(
    "Retrieve relevant information from the database and generate a structured response.\n\n"
    "User Query: {query}\n"
    "Relevant Information: {retrieved_data}\n\n"
    "Provide a well-structured and detailed answer based on the retrieved data."
)

# Define FAISS Retrieval Functions
def retrieve_defense(query):
    docs = defense_retriever.invoke(query)
    retrieved_data = docs if docs else "No relevant information found."
    # Apply custom prompt
    formatted_prompt = custom_prompt.format(query=query, retrieved_data=retrieved_data)
    return formatted_prompt

def retrieve_agriculture(query):
    docs = agriculture_retriever.invoke(query)
    retrieved_data = docs if docs else "No relevant information found."

    # Apply custom prompt
    formatted_prompt = custom_prompt.format(query=query, retrieved_data=retrieved_data)
    return formatted_prompt

def retrieve_railways(query):
    docs = railways_retriever.invoke(query)
    retrieved_data = docs if docs else "No relevant information found."
    # Apply custom prompt
    formatted_prompt = custom_prompt.format(query=query, retrieved_data=retrieved_data)
    return formatted_prompt

def retrieve_finance(query):
    docs = finance_retriever.invoke(query)
    retrieved_data = docs if docs else "No relevant information found."
    # Apply custom prompt
    formatted_prompt = custom_prompt.format(query=query, retrieved_data=retrieved_data)
    return formatted_prompt

# Create FAISS Retrieval Agents
defense_agent = Agent(
    model=Groq(id="qwen-2.5-32b"),
    name="Defense Agent",
    description="Retrieves and provides insights on defense-related topics, including policies, procurement, and strategic initiatives, using FAISS.",
    tools=[retrieve_defense],
    show_tool_calls=True,
    markdown=True
)

agriculture_agent = Agent(
    model=Groq(id="qwen-2.5-32b"),
    name="Agriculture Agent",
    description="Fetches relevant agricultural information, covering farming practices, policies, and market trends, from a FAISS-powered database.",
    tools=[retrieve_agriculture],
    show_tool_calls=True,
    markdown=True
)

railways_agent = Agent(
    model=Groq(id="qwen-2.5-32b"),
    name="Railways Agent",
    description="Offers railway-related details, including operations, infrastructure, and policies, by retrieving relevant information from FAISS.",
    tools=[retrieve_railways],
    show_tool_calls=True,
    markdown=True
)

finance_ministry_agent = Agent(
    model=Groq(id="qwen-2.5-32b"),
    name="Finance Ministry Agent",
    description="Retrieves information on India's financial policies, budgets, taxation, and economic reforms.",
    tools=[retrieve_finance],  # You'll need to create a FAISS retriever for finance data.
    show_tool_calls=True,
    markdown=True
)

# Create Web Search Agent
web_search_agent = Agent(
    model=Groq(id="qwen-2.5-32b"),
    name="Web Search Agent",
    description="Fetches up-to-date information from the internet on general knowledge, current events, and trending topics using real-time web search tools.",
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)


# Create Yahoo Finance Agent
finance_agent = Agent(
    model=Groq(id="qwen-2.5-32b"),
    name="Finance Agent",
    description="Handles financial queries, providing real-time stock prices, market trends, company insights, and analyst recommendations using Yahoo Finance data.",
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    show_tool_calls=True,
    markdown=True
)

# Create Content Writer Agent
content_writer_agent = Agent(
    model=Groq(id="qwen-2.5-32b"),
    name="Expert Content Writer Agent",
    description="An expert AI writer that generates well-structured and engaging content, including blogs, articles, reports, and creative writing pieces.",
    show_tool_calls=True,
    markdown=True
)



# Create Routing Agent
router_agent = Agent(
    name="Router Agent",
    description="Acts as the central decision-maker, intelligently routing user queries to the most relevant agent based on topic analysis. Ensures efficient information retrieval from internal databases or external sources as needed.",
    instructions=[
        "If the query is about Defense, route it to the Defense Agent.",
        "If the query is about Agriculture, route it to the Agriculture Agent.",
        "If the query is about Railways, route it to the Railways Agent.",
        "If the query is about India's government finance, policies, taxation, budgets, or economic regulations, route it to the Finance Ministry Agent.",
        "If the query is about recent news or information, route it to the Web Search Agent.",
        "If the query is about financial data, route it to the Finance Agent.",
        "If the query is about writing content, route it to the Content Writer Agent.",
    ],
    team=[defense_agent, agriculture_agent, railways_agent, finance_ministry_agent, web_search_agent, finance_agent, content_writer_agent],
    show_tool_calls=True,
    markdown=True,
)


# Example Query
# query = "In what temperature does sugarcane grow?" # agriculture
# query = "What are the cancellation policy if IRCTC?" # railways
# query = "what are defence major capital procurement?" # defence
# query = "Tell me about the investments of india in 2022-23?" # finance_ministry
# query = "What is the latest stock price of APPLE?" # finance
# query = "What is the latest news about OPENAI" # web_search
query = "Write a short blog about Latest trends in AI Agents?" # content_creation


router_agent.print_response(query, stream=True)

