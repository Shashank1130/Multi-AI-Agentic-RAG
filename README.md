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

- `agents/` : Contains code for all 8 agents.  
- `router/` : Manages the query routing logic.  
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

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/Multi-AI-Agent-RAG.git
cd Multi-AI-Agent-RAG
Got it! Here’s the updated `README.md` with the improved execution process and brief descriptions for each agent:  

```markdown
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

- `agents/` : Contains code for all 8 agents.  
- `router/` : Manages the query routing logic.  
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

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/Multi-AI-Agent-RAG.git
cd Multi-AI-Agent-RAG
```

### 2. Create a virtual environment and install dependencies:
```bash
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure API keys:
- Create a `.env` file in the root directory.
- Add your API keys as shown below:
  ```plaintext
  API_KEY_1=your_api_key_here
  API_KEY_2=your_api_key_here
  ```

### 4. Prepare vectorized databases:
- Run the script to process and store data:
  ```bash
  python chunking_and_vectorstore.py
  ```
- Store the generated databases inside the `vector_db` folder.

### 5. Run the main script:
```bash
python agentic_rag_main.py
```

---

## 📋 Usage

- Run `agentic_rag_main.py` and input your query.
- The routing agent will automatically select the most relevant agent, process the query, and provide an accurate response.

---

## 🛠 Future Enhancements

- **Expand Agent Capabilities:** Add more domain-specific and external data agents to broaden the system's versatility.
- **Improve Routing Logic:** Optimize the algorithm for faster and more accurate query handling.
- **Integrate Advanced Data Sources:** Enhance the system’s external data retrieval by incorporating additional APIs and web scraping tools.

---

## 📞 Contact

For any questions or feedback, feel free to reach out:  
- **Email:** shashankdubey1130@gmail.com  
- **LinkedIn:** [Shashank Kumar Dubey](https://www.linkedin.com/in/shashank-kumar-dubey/)  

---

**⭐ If you found this project helpful, please give it a star! ⭐**
```

### Key Changes Made:
1. **Execution Process:** Simplified and aligned with your folder structure and file names.
2. **Agent Descriptions:** Added a brief description for each agent.
3. **.env Configuration:** Included instructions for setting up API keys.
4. **Future Enhancements:** Expanded ideas for further development.

This version is more comprehensive and user-friendly. Let me know if you need any tweaks! 😊
