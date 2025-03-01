# Multi-AI Agent RAG System

This project showcases a **Multi-AI Agent Retrieval-Augmented Generation (RAG) system** built using **Agno** and **LangChain**. It integrates **8 intelligent agents** to enable dynamic query routing, accurate database retrieval, and seamless external data sourcing, delivering precise and context-aware responses.

---

## 📌 Project Overview

- **Objective:** Develop a robust RAG system that dynamically routes user queries to the most relevant agent, leveraging both structured databases and external data sources.

- **Key Components:**
  - **4 Domain-Specific Agents:** For Defense, Railways, Agriculture, and Finance Ministry databases.
  - **3 Specialized Task Agents:** Web Search Agent, Yahoo Finance Agent, and Content Creation Agent.
  - **1 Routing Agent:** Acts as a smart orchestrator to direct queries to the appropriate agent based on the context.

- **Functionality:** The system intelligently handles diverse queries, ensuring high response relevance through agent collaboration and external fallback mechanisms.

---

## 🛠 Technologies Used

- **Frameworks:** Agno, LangChain  
- **Programming Language:** Python  
- **Agents:** Custom agents for database retrieval, web search, Yahoo Finance data extraction, content generation, and intelligent query routing.

---

## 📂 Project Structure  
- `data/` : Includes sample databases and relevant data files.  
- `vector_db/` : Stores vectorized data for fast retrieval.  
- `.env` : Contains API keys and environment variables.  
- `agentic_rag_main.py` : Entry point for running the RAG system.  
- `chunking_and_vectorstore.py` : Prepares and stores vectorized data.  
- `requirements.txt` : Lists required libraries.  

---

## 🤖 Agent Descriptions

1. **Defense Agent:** Handles queries related to defense databases.  
2. **Railways Agent:** Retrieves and processes information from railway databases.  
3. **Agriculture Agent:** Manages agricultural data and responds to related queries.  
4. **Finance Ministry Agent:** Provides information from financial databases.  
5. **Web Search Agent:** Fetches real-time information from the web for external queries.  
6. **Yahoo Finance Agent:** Extracts stock and financial data from Yahoo Finance.  
7. **Content Creation Agent:** Generates and refines content based on the input.  
8. **Routing Agent:** Dynamically directs queries to the appropriate agent.  

---

## ⚙️ Setup and Execution

### 1. Create a virtual environment and install dependencies:
```bash
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate
pip install -r requirements.txt
