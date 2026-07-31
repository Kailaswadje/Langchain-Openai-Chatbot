# 🦜🔗 LangChain OpenAI Chatbot

A lightweight conversational AI web app built with **LangChain**, **OpenAI**, and **Streamlit**. Enter your OpenAI API key, type a question, and get an instant LLM-powered response — all through a clean browser interface with zero backend setup.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?logo=langchain&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-LLM-412991?logo=openai&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Overview

This project demonstrates how to integrate a Large Language Model (LLM) into an interactive web application using the modern GenAI stack:

- **LangChain** handles the LLM abstraction and invocation
- **OpenAI** provides the underlying language model (`temperature=0.8` for creative, varied responses)
- **Streamlit** powers the UI — form input, sidebar API key entry, and response display

The app validates the API key format before making any calls and keeps the key secure using a password-masked input field, so it is never hardcoded or exposed in the source code.

---

## ✨ Features

- 🔐 **Secure API key handling** — key is entered via a masked sidebar input, never stored in code
- ✅ **Key validation** — warns the user if the key doesn't match the expected `sk-` format
- 💬 **Simple Q&A interface** — type any question into the form and submit
- ⚡ **Instant responses** — LangChain invokes the OpenAI LLM and renders the answer inline
- 🎨 **Clean UI** — built entirely with Streamlit, no HTML/CSS/JS required

---

## 🏗️ How It Works

```
User enters API key (sidebar) ──► Key format validated (sk-...)
        │
User types a question ──► Streamlit form submission
        │
        ▼
LangChain OpenAI wrapper (temperature = 0.8)
        │
        ▼
llm.invoke(input_text) ──► Response displayed via st.info()
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- An [OpenAI API key](https://platform.openai.com/api-keys)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Kailaswadje/Langchain-Openai-Chatbot.git
   cd Langchain-Openai-Chatbot
   ```

2. **(Recommended) Create a virtual environment**

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**

   ```bash
   streamlit run GenAI_06_Openai_langchain.py
   ```

5. Open the local URL shown in your terminal (usually `http://localhost:8501`), paste your OpenAI API key in the sidebar, and start asking questions.

---

## 🧰 Tech Stack

| Component | Purpose |
|---|---|
| [Streamlit](https://streamlit.io/) | Web UI — forms, sidebar, response display |
| [LangChain](https://www.langchain.com/) (`langchain-openai`) | LLM orchestration and invocation |
| [OpenAI](https://openai.com/) | Underlying language model |
| Python | Core language |

---

## 📂 Project Structure

```
Langchain-Openai-Chatbot/
├── GenAI_06_Openai_langchain.py   # Main Streamlit application
├── requirements.txt               # Project dependencies
├── .gitignore                     # Ignored files (env, cache, etc.)
└── README.md                      # Project documentation
```

---

## 🔮 Future Improvements

- [ ] Add conversation memory (`ConversationBufferMemory`) for multi-turn chat
- [ ] Switch to `ChatOpenAI` with streaming responses
- [ ] Add model selection dropdown (GPT-4o, GPT-4o-mini, etc.)
- [ ] Add temperature/max-tokens controls in the sidebar
- [ ] Deploy to Streamlit Community Cloud

---

## 🔒 Security Note

Your OpenAI API key is entered at runtime through a password-masked field and is **never** stored, logged, or committed to the repository. Never hardcode API keys in source files.

---

## 👤 Author

**Kailas Wadje**
MSc Data Science & AI, University of Liverpool

- GitHub: [@Kailaswadje](https://github.com/Kailaswadje)
- LinkedIn: [linkedin.com/in/kwadaje](https://www.linkedin.com/in/kwadaje/)

---

## 📄 License

This project is licensed under the MIT License — feel free to use, modify, and share.

---

⭐ If you found this project helpful, consider giving it a star!
