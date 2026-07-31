# FinAgent

An AI-powered financial assistant built with **FastAPI**, **LangChain**, **Groq LLM**, and **Yahoo Finance**.

FinAgent combines a real-time financial dashboard with an intelligent AI agent capable of answering investment and stock market questions using live financial data.

---

## Live Demo

### Frontend

https://finance-agent-4.netlify.app/

### Backend API

https://finagent-sp3u.onrender.com/

### Swagger Documentation

https://finagent-sp3u.onrender.com/docs

---

## Features

- Real-Time Financial Dashboard
- AI Financial Assistant
- Latest Financial News
- Live Market Overview
- Company Information Lookup
- Stock Price Lookup
- Financial Metrics Analysis
- LangChain Tool Calling
- REST API
- Docker Support

---

## Application

### Dashboard

The dashboard provides a quick overview of the financial market before interacting with the AI assistant.

- Live Market Overview
- Latest Financial News

### AI Assistant

Ask natural language questions such as:

```text
Should I invest in Apple?

Analyze Tesla stock.

What is NVIDIA's market cap?

Show Microsoft's financial metrics.

What is happening in today's market?
```

The AI agent automatically selects the appropriate tool, retrieves live financial data, and generates concise responses.

---

## System Architecture

```text
                              User
                                │
               ┌────────────────┴────────────────┐
               │                                 │
               ▼                                 ▼
        Dashboard API                      Ask AI API
               │                                 │
               ▼                                 ▼
      Dashboard Service                 LangChain Agent
                                                 │
                          ┌──────────────────────┼──────────────────────┐
                          ▼                      ▼                      ▼
                  Company Tool           Market Tool             News Tool
                          │                      │                      │
                          └──────────────┬───────┴──────────────┬───────┘
                                         ▼
                                   Service Layer
                                         │
                                         ▼
                             Yahoo Finance + Google News
                                         │
                                         ▼
                                     Groq LLM
```

---

## Project Structure

```text
app
│
├── agent
│   ├── agent.py
│   ├── llm.py
│   ├── prompts.py
│   └── tools.py
│
├── api
│   ├── ask.py
│   └── dashboard.py
│
├── schemas
│
├── services
│   ├── company_service.py
│   ├── financial_service.py
│   ├── market_service.py
│   └── news_service.py
│
├── config.py
└── main.py
```

---

## Request Flow

### Dashboard

```text
Client
   │
   ▼
Dashboard API
   │
   ▼
Dashboard Service
   │
   ├────────────► Yahoo Finance
   │
   └────────────► Google News
   │
   ▼
JSON Response
```

### AI Assistant

```text
Client
   │
   ▼
Ask API
   │
   ▼
LangChain Agent
   │
   ▼
Automatic Tool Selection
   │
   ▼
Financial Services
   │
   ▼
Yahoo Finance
   │
   ▼
Groq LLM
   │
   ▼
Answer
```

---

## REST API

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/v1/dashboard` | Returns market overview and latest news |
| POST | `/api/v1/ask` | Ask the AI financial assistant |

---

## Tech Stack

- Python
- FastAPI
- LangChain
- Groq LLM
- Yahoo Finance
- Google News
- Pydantic
- Docker

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/finagent.git

cd finagent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=YOUR_API_KEY
MODEL_NAME=openai/gpt-oss-20b
```

Run the application:

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://localhost:8000/docs
```

---

## Docker

```bash
docker compose up --build
```

---

## Roadmap

- Portfolio Analysis
- Watchlist Management
- Interactive Stock Charts
- Financial Report Analysis (RAG)
- Multi-Agent Financial Assistant
- Multi-LLM Support (Groq, Gemini, OpenAI)

---

## Future Improvements

- Authentication
- Conversation Memory
- Vector Database Integration
- Company Report Analysis
- Streaming Responses
- Deployment Monitoring

---

## License

This project is intended for educational and portfolio purposes.
