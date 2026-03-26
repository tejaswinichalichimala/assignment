AI Secure Data Intelligence Platform
An advanced AI-powered log analysis and security intelligence system that detects sensitive data, identifies threats, and provides actionable insights using a hybrid approach combining rule-based detection and large language models.

Overview
The AI Secure Data Intelligence Platform functions as:
AI Gateway
Data Scanner
Log Analyzer
Risk Engine
It processes structured and unstructured data, detects security vulnerabilities, and generates intelligent insights and recommendations.

Key Features

Detection Engine
Regex-based detection of:
Emails
Phone numbers
API keys
Passwords
Tokens

AI Intelligence
Context-aware reasoning (not just summarization)
Risk explanation
Impact analysis
Actionable recommendations

Log Analysis
Stack trace detection
Error analysis
Debug information leaks
Credential exposure detection

Real-Time Processing
WebSocket-based live log analysis
Instant risk detection

Correlation Engine
Detect repeated failed logins
Identify suspicious IP activity
Brute-force attack detection

Anomaly Detection
AI-based detection of unusual patterns
Identification of unknown threats

Risk Engine
Risk scoring system
Risk classification:
Low
Medium
High
Critical

Policy Engine
Mask sensitive data
Block high-risk content

Chat with Logs
Query logs using natural language
Example:
What caused this error?
Is this a security issue?

Project Structure
AI Secure Data Intelligence Platform/
│
├── app/                          # Backend (FastAPI)
│   ├── main.py
│   ├── routes/
│   │    ├── analyze.py
│   │    └── chat.py
│   │
│   ├── services/
│   │    ├── parser.py
│   │    ├── detector.py
│   │    ├── log_analyzer.py
│   │    ├── correlation_engine.py
│   │    ├── anomaly_engine.py
│   │    ├── risk_engine.py
│   │    ├── policy_engine.py
│   │    └── ai_engine.py
│   │
│   ├── utils/
│   │    └── patterns.py
│   │
│   └── requirements.txt
│
├── frontend/                     # Frontend (React + Vite)
│   ├── src/
│   │    ├── components/
│   │    │    ├── Upload.jsx
│   │    │    ├── LogViewer.jsx
│   │    │    ├── Insights.jsx
│   │    │    ├── Chat.jsx
│   │    │    └── LiveLogs.jsx
│   │    └── App.jsx
│
├── logs/
│   └── sample.log
│
└── README.md

Installation and Setup

Clone Repository
git clone <your-repo-url>
cd AI-Secure-Data-Intelligence-Platform

Backend Setup
cd app
pip install -r requirements.txt

Run backend:
uvicorn app.main:app --reload

API documentation:
http://localhost:8000/docs

Frontend Setup
cd frontend
npm install
npm run dev

Frontend:
http://localhost:5173/

API Usage

POST /analyze
Request:
{
  "input_type": "log",
  "content": "your log data",
  "options": {
    "mask": true,
    "block_high_risk": true,
    "log_analysis": true
  }
}

Response:
{
  "summary": "Logs contain sensitive credentials",
  "findings": [
    {
      "type": "api_key",
      "risk": "high"
    }
  ],
  "risk_score": 10,
  "risk_level": "high",
  "insights": ["API key exposed"],
  "recommendations": ["Use environment variables"]
}

WebSocket (Real-Time Logs)
Endpoint:
ws://localhost:8000/live

Capabilities:
Live log streaming
Instant detection
Real-time AI insights

Chat API
POST /chat
{
  "question": "What is the issue?",
  "logs": "log content"
}

Example Log
INFO User login
[email=admin@company.com](mailto:email=admin@company.com)
password=admin123
api_key=sk-prod-xyz
ERROR stack trace: NullPointerException

AI Capabilities
Root cause analysis
Threat detection
Security recommendations
Context-aware reasoning

Advanced Features
Real-time log streaming
Cross-log correlation
Anomaly detection using AI
Hybrid detection system (Regex + LLM)
Chat-based log exploration

Future Improvements
User authentication
Dashboard analytics
Cloud deployment
SIEM integration
Alerting system (Email or Slack)

Author
Tejaswini Chalichimala

License
This project is intended for educational and hackathon use.
