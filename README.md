# Multi-AI Agent RAG System

This project is a Multi-AI Agent Retrieval-Augmented Generation (RAG) system built using **Agno** and **LangChain**. It integrates 7 agents for intelligent query routing, database retrieval, and external data sourcing to generate accurate responses.

---

## 📌 **Project Overview**
- Designed to handle queries across multiple databases (4 DBs) and external sources using a dynamic query routing mechanism.
- Integrates 7 agents: 4 for domain-specific databases and 3 for external tasks like web search and content generation.
- Ensures precise data retrieval and response accuracy through efficient agent collaboration.

---

## 🚀 **Key Features**
- **Dynamic Query Routing:** Routes user queries to the most relevant agent for accurate information retrieval.
- **Multi-Agent Integration:** Combines 7 agents for database and external data handling.
- **Enhanced Accuracy:** Implements fallback strategies for situations when database information is insufficient.

---

## 🛠 **Technologies Used**
- **Frameworks:** Agno, LangChain  
- **Languages:** Python  
- **Agents:** Custom agents for database retrieval, web search, Yahoo Finance, and content generation.  

---

## 📂 **Project Structure**
- `agents/` : Contains code for all 7 agents.  
- `router/` : Manages query routing logic.  
- `data/` : Includes sample databases and data files.  
- `main.py` : Entry point for running the system.  

---

## ⚙️ **Setup and Installation**
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Multi-AI-Agent-RAG.git
   cd Multi-AI-Agent-RAG
