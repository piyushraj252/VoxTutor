# 🎓 VoxTutor

### Your Voice-First AI Tutor

VoxTutor is a voice-first AI tutor designed to make learning more natural, interactive, and accessible.

Instead of typing every question, students can simply **speak to their AI tutor**, receive an intelligent explanation, and listen to the response.

---

## 🚨 Problem Statement

Traditional learning is often text-heavy and fragmented, making it difficult for students to get quick and interactive explanations.

## 💡 Our Solution

VoxTutor transforms learning into a **voice-first conversation**.

The student speaks a question, VoxTutor processes it using AI and relevant knowledge, and then responds with a spoken explanation.

---

## ✨ Key Features

- 🎙️ **Voice-first interaction** — Ask questions naturally using your voice.
- 🧠 **AI-powered tutoring** — Generates clear and beginner-friendly explanations.
- 🔍 **Knowledge retrieval** — Uses a vector database to retrieve relevant information.
- 🔊 **AI voice** — Uses Rime for natural voice generation.
- 🛑 **Stop control** — Interrupt the tutor whenever needed.
- ⚡ **Real-time interaction** — Designed for fast conversational learning.

---

## 🏗️ How It Works

```text
        🎓 Student
             │
             │ Voice
             ▼
   ┌───────────────────┐
   │     Frontend      │
   │    HTML/CSS/JS    │
   └─────────┬─────────┘
             │
             │ Question
             ▼
   ┌───────────────────┐
   │   FastAPI Backend  │
   └─────────┬─────────┘
             │
             ▼
   ┌───────────────────┐
   │ Qdrant Knowledge   │
   │  / Vector Search   │
   └─────────┬─────────┘
             │
             │ Relevant Context
             ▼
   ┌───────────────────┐
   │    AI / Gemini     │
   │ Answer Generation  │
   └─────────┬─────────┘
             │
             ▼
   ┌───────────────────┐
   │      Rime AI       │
   │   Text → Speech    │
   └─────────┬─────────┘
             │
             ▼
          🔊 Answer
          🧠 Core Technology: RAG

VoxTutor uses the concept of Retrieval-Augmented Generation (RAG).

Instead of relying only on the AI model's internal knowledge, VoxTutor can retrieve relevant information from its own knowledge base before generating an answer.

The process
Student Question
       ↓
Question Embedding
       ↓
Qdrant Semantic Search
       ↓
Relevant Knowledge
       ↓
AI Model
       ↓
Grounded Answer

This approach allows the knowledge base to be expanded with educational material such as notes, textbooks, and subject-specific resources without requiring the entire AI model to be retrained.

🛠️ Tech Stack
Technology	Purpose
HTML	Frontend structure
CSS	User interface
JavaScript	Voice interaction and frontend logic
Python	Backend
FastAPI	Backend API
Qdrant	Vector database and semantic retrieval
Gemini	AI response generation
Rime AI	Text-to-speech
Git & GitHub	Version control
📁 Project Structure
VoxTutor/
│
├── backend/
│   ├── ingest_knowledge.py
│   ├── main.py
│   ├── setup_qdrant.py
│   └── test_rime.py
│
├── data/
│   └── knowledge.txt
│
├── frontend/
│   └── index.html
│
├── .gitignore
└── README.md
🔄 How VoxTutor Works
1. 🎤 Ask

The student clicks Start Talking and asks a question.

2. 📝 Speech → Text

The browser's speech recognition converts the student's voice into text.

3. 🚀 Send

The frontend sends the question to the FastAPI backend.

4. 🔍 Retrieve

The system searches the Qdrant knowledge base for relevant information.

5. 🤖 Generate

The AI model uses the question and retrieved information to generate an explanation.

6. 🔊 Speak

Rime can convert the generated response into natural speech.

7. 🛑 Control

The student can stop the interaction whenever needed.

🚀 Getting Started
1. Clone the repository
git clone https://github.com/piyushraj252/VoxTutor.git
cd VoxTutor
2. Create a virtual environment
python3 -m venv .venv

Activate it:

source .venv/bin/activate
3. Install dependencies

Install the Python packages required by the backend.

pip install fastapi uvicorn python-dotenv qdrant-client openai requests
4. Configure environment variables

Create a .env file in the project root.

Add your required API keys and configuration.

OPENAI_API_KEY=your_api_key
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
RIME_API_KEY=your_rime_api_key

⚠️ Never upload your real .env file or API keys to GitHub.

5. Start the backend
uvicorn backend.main:app --port 8000

The backend will run at:

http://127.0.0.1:8000
6. Start the frontend

Open the frontend folder in VS Code and run index.html using Live Server.

🔐 Security

VoxTutor keeps sensitive credentials outside the public repository.

The following are excluded using .gitignore:

.env
.venv/
__pycache__/
.DS_Store
backend/rime_test.wav

API keys should never be placed directly inside frontend JavaScript or committed to a public GitHub repository.

🎯 Future Scope

VoxTutor can be expanded with:

📚 Large-scale educational knowledge bases
📄 PDF and textbook ingestion
🎓 Personalized learning paths
📊 Student progress tracking
🧠 Long-term conversation memory
🌐 Multilingual tutoring
📝 Automatic quiz generation
🎯 Adaptive difficulty
🔎 Source citations
📱 Mobile application
🔊 Advanced real-time voice interaction
👨‍🏫 Subject-specific AI tutors
🌟 Vision

Our vision is to make learning feel less like interacting with software and more like having a personal tutor available whenever you need one.

VoxTutor — Learn by talking. 🎙️🧠

👥 Team
HOTFIXERS

Built for StarForge Hackathon 2026 — VoxForge Track