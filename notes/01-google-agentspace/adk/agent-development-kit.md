# Agent Development Kit (ADK)

📘 <a href='https://fern-stop-81f.notion.site/Agent-Development-Kit-ADK-22713f9f5c0380a5bddee40b44f89076'> Agent Development Kit (ADK) - Part 1 </a> 
<br/><br/>
📘 <a href='#'> Part 2 Link Coming Soon... </a> 
<br/>
<br/>

## 🗒️ Summary
### Part 1
The Agent Development Kit (ADK) by Google Cloud is a Python-based SDK designed to help developers build, manage, and deploy powerful AI agents and multi-agent systems with ease, even without deep AI expertise. It supports flexible development approaches—from conversational agents and internal knowledge tools to fully custom systems using LangChain or the Gen AI SDK. ADK enables real-time, LLM-powered interactions with built-in memory, artifact storage, orchestration, evaluation tools, and seamless deployment via Agent Engine. It also integrates with external APIs, supports code execution, and promotes modular, collaborative development using tools and models like Gemini or other LLMs.

### Part 2
ADK (Agent Development Kit) helps build structured multi-agent systems using a tree-based architecture, with LLM agents for intelligent tasks and workflow agents (Sequential, Loop, Parallel, Custom) for deterministic flows. It supports callbacks for customization and control, local testing, and scalable deployment via Agent Engine on Vertex AI. ADK also includes evaluation tools for response accuracy and tool usage, ensuring reliable, production-ready agents.


## 📚 Table of Contents

### Introducing ADK
1. Key areas where AI Agents made an impact
2. Key path for building an Agent
3. What does ADK include

### Develop agents with ADK
1. ADK Key Concepts
2. Components of ADK
3. How to configure ADK
4. Ways to Interact with your agent
   1. Web UI
   2. Command Line Interface CLI
   3. Programmatic Interface
   4. API Server
5. ADK First Agent - **Hands On**
6. Empower ADK with Tools - **Hands On**

### Build Multi-Agent systems with ADK
1. LLM Based Agents
2. Workflow Agents
   1. Sequential Agents
   3. Loop Agents
   4. Parallel Agents
   5. Custom Agents
6. Callbacks
   1. before_agent_callback
   8. after_agent_callback
   9. LLM interaction Callbacks
   10. Tool Execution Callbacks
10. Build Multi-Agent System with ADK - **Hands On**
    1. parent_and_subagents Code
    2. Workflow Agents code
       1. Sequential Agent
       2. Loop Agent & Loop Agent Termination
       3. Parallel Agent

### Deploy ADK agent to Agent Engine
1. Develop & Deploy agents with Agent Engine
   1. Develop & Test
   2. Deploy
   3. Query
2. Hands On

### Evaluate ADK agent system
1. Evaluating the final response
2. Evaluating Trajectory and Tool Use
3. ADK Evaluation Methods
   1. Using Test file
   2. Using Evalset
4. How to run an evaluation with ADK