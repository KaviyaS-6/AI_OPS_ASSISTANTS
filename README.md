# 🤖 AI Ops Multi-Agent Assistant

## 📌 Project Overview

AI Ops Multi-Agent Assistant is an intelligent automation system that interprets user tasks, creates execution plans using Large Language Models (LLMs), executes tasks via external tools, and verifies outputs for correctness.

This project demonstrates how multiple AI agents collaborate to perform real-world DevOps and automation tasks.

---

## 🚀 Features

✅ Natural Language Task Understanding  
✅ Multi-Agent Architecture  
✅ Automated Task Planning  
✅ Tool-Based Execution  
✅ Output Verification  
✅ GitHub Automation  
✅ Weather Information Retrieval  
✅ Modular & Scalable Design  

---

## 🧠 System Architecture

```
User Input
   ↓
Planner Agent
   ↓
Executor Agent
   ↓
External Tools
   ├── GitHub API
   └── Weather API
   ↓
Verifier Agent
   ↓
Final Output
```

---

## ⚙️ Tech Stack

| Component | Technology |
|-----------|------------|
| Programming Language | Python |
| LLM Provider | Groq API |
| Version Control Automation | GitHub REST API |
| Weather Data | OpenWeather API |
| HTTP Requests | requests |
| Environment Management | python-dotenv |

---

## 📂 Project Structure

```
ai_ops_assistant/
│
├── agents/
│   ├── planner.py
│   ├── executor.py
│   └── verifier.py
│
├── tools/
│   ├── github_tool.py
│   └── weather_tool.py
│
├── llm/
│   └── llm_client.py
│
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

## 🔧 Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai_ops_assistant.git
cd ai_ops_assistant
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key
GITHUB_TOKEN=your_github_personal_access_token
WEATHER_API_KEY=your_openweather_api_key
```

---

### 4️⃣ Run the Application

```bash
python main.py
```

---

### 5️⃣ Running via API

```bash
uvicorn app:app --reload
```

Then open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 💡 Example Usage

### 🔹 Create GitHub Repository

```
Enter your task: Create a new GitHub repository named ai-test-repo
```

---

### 🔹 Get Weather Information

```
Enter your task: Get weather in Chennai
```

---

## 📊 Sample Output

```
PLAN:
{'steps': [{'tool': 'weather', 'input': 'Chennai'}]}

RAW RESULTS:
{'city': 'Chennai', 'temperature': 26.6, 'description': 'mist'}

FINAL OUTPUT:
Weather in Chennai is 26.6°C with mist conditions.
```

---

## 🧩 Agent Responsibilities

### 🧭 Planner Agent
- Interprets natural language queries
- Converts tasks into structured execution plans

### ⚙️ Executor Agent
- Reads planner output
- Calls appropriate tools
- Handles external API integrations

### 🔍 Verifier Agent
- Validates execution results
- Generates structured summaries
- Improves result readability

---

## 🛠 Tools Implemented

### 📁 GitHub Tool
Supports:
- Repository creation
- GitHub automation tasks

### 🌤 Weather Tool
Retrieves:
- Current temperature
- Weather description
- Location-based data

---

## 🧪 Error Handling

The system handles:
- API authentication failures
- Permission errors
- Network connectivity issues
- Invalid user input

---

## 📈 Design Decisions

- Modular agent architecture for scalability
- Tool-based execution allows easy extension
- Verification layer improves output reliability
- Environment variables ensure security

---

## 🔮 Future Improvements

- Slack / Email automation support
- Docker container deployment
- Database logging system
- Multi-step workflow memory
- Web UI dashboard
- Support for additional DevOps tools

---

## 🧑‍💻 Author

**Kaviya S**

---

## 📜 License

This project is developed for learning, demonstration, and research purposes.

---

## ⭐ Acknowledgements

- Groq LLM API
- OpenWeather API
- GitHub REST API
- Open-source Python community

---

# 🎯 Project Highlights

✔ Demonstrates multi-agent AI collaboration  
✔ Real-world API integrations  
✔ Scalable automation framework  
✔ Production-style modular coding  
