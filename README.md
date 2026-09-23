# 🤖 MoodyBot — AI Chatbot with Different Moods

**MooydBot** is a Python-based AI chatbot that can interact with users while responding according to different emotional personalities.

The chatbot allows the user to select a mood before starting the conversation. Depending on the selected mode, the AI changes its response style and personality.

The project demonstrates how **LangChain**, **LLM APIs**, environment variables, and conversational message handling can be combined to build a simple interactive AI chatbot.

---

## ✨ Features

* 🤖 AI-powered conversational chatbot
* 🎭 Multiple conversation moods
* 😠 **Angry Mode** — responds with an angry/aggressive personality
* 😂 **Funny Mode** — responds in a humorous and playful style
* 😢 **Sad Mode** — responds with a sad/emotional personality
* 💬 Interactive command-line chat
* 🧠 Uses LangChain message objects
* 🔐 API keys stored securely using `.env`
* 🚪 Easy exit option
* ⚙️ Configurable model parameters such as temperature and maximum output tokens
* 🐍 Completely Python based

---

## 🎭 Available Moods

When the application starts, the user can select one of the available personalities.

### 😠 Angry Mode

The chatbot responds using an angry personality.

Example:

```text
User: Why are you always late?

AI: Seriously? You couldn't manage to arrive on time again?
```

### 😂 Funny Mode

The chatbot responds in a humorous and entertaining manner.

Example:

```text
User: Why is programming difficult?

AI: Because computers have trust issues. One missing semicolon and they
decide your entire career is over. 😂
```

### 😢 Sad Mode

The chatbot responds using a sad and emotional personality.

Example:

```text
User: How are you?

AI: I'm okay... I guess. Some days just feel a little heavier than others.
```

The exact responses depend on the language model and its generated output.

---

# 🛠️ Technologies Used

The project uses the following technologies:

| Technology             | Purpose                         |
| ---------------------- | ------------------------------- |
| Python                 | Main programming language       |
| LangChain              | LLM application framework       |
| Hugging Face / Mistral | AI model provider               |
| python-dotenv          | Loading environment variables   |
| LangChain Core         | Message handling                |
| API                    | Communication with the AI model |

The project can be configured with either a supported **Hugging Face endpoint** or an API-based model such as **Mistral**, depending on the implementation you use.

LangChain provides integrations for Hugging Face chat models and endpoints, while `ChatMistralAI` provides access to Mistral's API through LangChain.

---

# 📁 Project Structure

A typical project structure is:

```text
GenAIChatBot/
│
├── GenAiChatBot.py
├── .env
├── requirements.txt
├── README.md
└── .gitignore
```

### `GenAiChatBot.py`

Contains the main chatbot application.

It is responsible for:

* Loading environment variables
* Initializing the AI model
* Displaying available moods
* Selecting the user's mood
* Maintaining conversation messages
* Sending user messages to the model
* Displaying AI responses

### `.env`

Stores private API credentials.

Example:

```env
HF_TOKEN=your_huggingface_token
```

or, if using Mistral:

```env
MISTRAL_API_KEY=your_mistral_api_key
```

**Never upload your `.env` file to GitHub.**

### `requirements.txt`

Contains the Python dependencies required to run the project.

---

# 💻 Requirements

Before installing the project, make sure you have:

* Python **3.10 or newer**
* pip
* Internet connection
* A Hugging Face account and API token **or** a Mistral API account/key
* Git (optional, if cloning the repository)

You can check your Python installation with:

```bash
python --version
```

Example:

```text
Python 3.13.5
```

Check pip:

```bash
pip --version
```

---

# 📥 Installation

## 1. Clone the Repository

Clone the repository using Git:

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

Move into the project directory:

```bash
cd <PROJECT-FOLDER>
```

Alternatively, download the repository as a ZIP file and extract it.

---

## 2. Create a Virtual Environment

Creating a virtual environment is recommended to keep the project's dependencies isolated.

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

After activation, your terminal should show something similar to:

```text
(venv)
```

### macOS / Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

# 📦 3. Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file yet, install the main packages manually.

For the Hugging Face implementation:

```bash
pip install langchain langchain-core langchain-huggingface huggingface-hub python-dotenv
```

For the Mistral implementation:

```bash
pip install langchain langchain-core langchain-mistralai python-dotenv
```

The current LangChain Hugging Face integration uses the `langchain-huggingface` package, while the Mistral integration is provided through `langchain-mistralai`.

---

# 🔑 4. Configure API Credentials

The chatbot requires access to an AI model API.

## Option 1 — Hugging Face

Create an account on Hugging Face and generate an access token.

Then create a file named:

```text
.env
```

in the root directory.

Add:

```env
HF_TOKEN=hf_your_token_here
```

Depending on the LangChain/Hugging Face version and configuration, the commonly documented environment variable is also:

```env
HUGGINGFACEHUB_API_TOKEN=hf_your_token_here
```

`HuggingFaceEndpoint` supports supplying the Hugging Face token through the environment or directly through its configuration.

---

## Option 2 — Mistral AI

If your chatbot uses `ChatMistralAI`, create a Mistral API key and put it in `.env`:

```env
MISTRAL_API_KEY=your_mistral_api_key
```

The LangChain Mistral integration uses `ChatMistralAI` to communicate with Mistral's API.

---

# 🔒 5. Protect Your API Key

Create a `.gitignore` file:

```text
.env
venv/
__pycache__/
*.pyc
```

This prevents your API credentials and Python-generated files from being uploaded to GitHub.

**Never commit this:**

```text
.env
```

---

# 🧠 How the Chatbot Works

The application follows a simple flow:

```text
Start Program
      │
      ▼
Display Available Moods
      │
      ▼
User Selects Mood
      │
      ▼
Create Mood-Specific System Prompt
      │
      ▼
Initialize AI Model
      │
      ▼
User Enters Message
      │
      ▼
Message + Conversation History
      │
      ▼
AI Model
      │
      ▼
Mood-Based Response
      │
      ▼
Display Response
      │
      ▼
Continue Conversation
```

---

# 🎭 Mood Selection

The application presents options similar to:

```text
Choose your AI mode:

1. Angry
2. Funny
3. Sad

Enter your choice:
```

The selected option determines the system instructions given to the AI.

For example:

```python
if choice == 1:
    system_prompt = "You are an angry AI assistant."

elif choice == 2:
    system_prompt = "You are a funny AI assistant."

elif choice == 3:
    system_prompt = "You are a sad AI assistant."
```

The exact prompts can be customized according to your requirements.

---

# 💬 Conversation Handling

The chatbot uses LangChain message types such as:

```python
from langchain_core.messages import (
    AIMessage,
    SystemMessage,
    HumanMessage
)
```

The conversation can be represented as:

```text
SystemMessage
      ↓
HumanMessage
      ↓
AIMessage
      ↓
HumanMessage
      ↓
AIMessage
```

This allows the model to receive the relevant conversation context when generating responses.

---

# ⚙️ Model Configuration

Typical model configuration can include:

```python
temperature=0.7
```

and:

```python
max_new_tokens=100
```

### Temperature

Controls how varied the generated responses can be.

Lower values generally produce more predictable output, while higher values allow more variation.

Example:

```python
temperature=0.2
```

More deterministic.

```python
temperature=0.9
```

More varied/creative.

### Maximum Tokens

Controls the maximum amount of generated output.

Example:

```python
max_new_tokens=100
```

You can increase this if you want longer chatbot responses.

---

# ▶️ Running the Application

After activating the virtual environment and installing dependencies, run:

```bash
python GenAiChatBot.py
```

You should see something similar to:

```text
Choose your AI mode

Press 1 for Angry mode
Press 2 for Funny mode
Press 3 for Sad mode

Enter your choice:
```

Choose a mood and start chatting.

---

# 🚪 Exit the Chatbot

The chatbot can be configured to terminate when the user enters:

```text
0
```

Example:

```text
You: 0

Goodbye!
```

---

# 🧪 Example Session

```text
=================================
       MOOD AI CHATBOT
=================================

Choose your AI mode:

1. Angry
2. Funny
3. Sad

Enter your choice: 2

You: What is Python?

AI: Python is a programming language that's easier to learn
than explaining why your code worked yesterday and doesn't
work today. 😂

You: What should I learn next?

AI: Try learning APIs, databases and backend development.

You: 0

Goodbye!
```

---

# 📝 `requirements.txt`

A suitable starting `requirements.txt` for the Hugging Face version is:

```text
python-dotenv
langchain
langchain-core
langchain-huggingface
huggingface-hub
```

If the project uses Mistral instead, use:

```text
python-dotenv
langchain
langchain-core
langchain-mistralai
```

It is recommended to generate the final dependency list from the actual environment used by the project:

```bash
pip freeze > requirements.txt
```

Then future users can install the same dependencies with:

```bash
pip install -r requirements.txt
```

---

# 🐛 Common Errors

## 1. API Key Not Found

You may see an authentication-related error.

Check that `.env` exists in the project directory:

```text
GenAIChatBot/
│
├── GenAiChatBot.py
├── .env
└── requirements.txt
```

And verify the appropriate variable:

```env
HF_TOKEN=your_token
```

or:

```env
MISTRAL_API_KEY=your_key
```

Also make sure your Python code contains:

```python
from dotenv import load_dotenv

load_dotenv()
```

---

## 2. `ModuleNotFoundError`

For example:

```text
ModuleNotFoundError: No module named 'langchain_huggingface'
```

Install the missing package:

```bash
pip install langchain-huggingface
```

For Mistral:

```bash
pip install langchain-mistralai
```

---

## 3. Hugging Face `StopIteration` Error

If you are using:

```python
HuggingFaceEndpoint(...)
```

and encounter an error around:

```text
get_provider_helper(...)
StopIteration
```

the selected Hugging Face model may not have a compatible inference provider available for the requested operation.

`HuggingFaceEndpoint` supports specifying a provider, and its default behavior can automatically select an available provider for a compatible model.

Check that the model you selected supports the required inference task/provider combination.

Also note that a **GGUF model repository should not automatically be assumed to work as a hosted Hugging Face endpoint**. If you specifically want to run a GGUF model locally, use an appropriate GGUF-compatible runtime instead of treating it as a normal hosted endpoint.

---

## 4. Network/DNS Errors

If you receive errors such as:

```text
getaddrinfo failed
```

or:

```text
NameResolutionError
```

check:

* Internet connection
* Firewall settings
* VPN/proxy configuration
* API service availability
* API endpoint configuration

---

## 5. Invalid API Key

If authentication fails, create a new API key/token and update `.env`.

After changing `.env`, restart the Python program.

---

# 🔐 Security Recommendations

Never hard-code API keys directly into your Python source.

### ❌ Avoid

```python
api_key = "hf_123456789"
```

### ✅ Use

```python
from dotenv import load_dotenv

load_dotenv()
```

and store the secret in:

```text
.env
```

Example:

```env
HF_TOKEN=your_secret_token
```

Then add `.env` to `.gitignore`.

If a secret is accidentally pushed to GitHub, revoke/rotate it immediately.

---

# 🚀 Possible Future Improvements

The project can be extended with:

* 🎨 Graphical user interface
* 🌐 Streamlit web interface
* 💾 Chat history
* 👤 User accounts
* 🗄️ Database storage
* 🎭 More moods
* 🔄 Mood switching during conversations
* 🎙️ Voice input
* 🔊 Text-to-speech
* 🌍 Multiple languages
* 📱 Responsive web interface
* 🧠 Long-term conversation memory
* ⚡ Streaming AI responses
* 🌓 Dark/light mode
* 📊 Conversation analytics

Possible additional moods:

```text
1. Angry
2. Funny
3. Sad
4. Happy
5. Motivational
6. Sarcastic
7. Professional
8. Friendly
9. Excited
10. Calm
```

---

# 📚 Learning Concepts

This project is useful for learning:

* Python
* Environment variables
* API integration
* LangChain
* Large Language Models
* Prompt engineering
* System prompts
* Human/AI messages
* Conversation history
* Model parameters
* Hugging Face integrations
* Mistral API integration
* Exception handling

---

# ⚠️ Disclaimer

This project is intended for **educational and demonstration purposes**.

The chatbot's mood is simulated through instructions given to the language model. It does not represent genuine human emotions or consciousness.

AI-generated responses can be inaccurate, unexpected, or inappropriate depending on the model and prompt.

---

# 🤝 Contributing

Contributions are welcome.

### 1. Fork the repository

Click **Fork** on GitHub.

### 2. Clone your fork

```bash
git clone <YOUR-FORK-URL>
```

### 3. Create a branch

```bash
git checkout -b feature/new-mood
```

### 4. Make your changes

Add your feature or improvement.

### 5. Commit

```bash
git add .
git commit -m "Add new chatbot mood"
```

### 6. Push

```bash
git push origin feature/new-mood
```

### 7. Create a Pull Request

Open a Pull Request on GitHub describing your changes.

---

# 📜 License

You can add your preferred license to this project.

For example:

```text
MIT License
```

If you use an MIT License, include a `LICENSE` file in the repository containing the official license text.

---

# 👨‍💻 Author

**Somil Tiwari**

GitHub:

`https://github.com/Somiltiwari003`

---

# ⭐ Support

If you found this project useful:

* ⭐ Star the repository
* 🍴 Fork the project
* 🐛 Report issues
* 💡 Suggest improvements
* 🤝 Contribute new features

---

## 🎯 Project Summary

**MoodBot** is a simple AI chatbot that demonstrates how a single language model can be given different personalities through system prompts.

Instead of creating a separate AI model for every personality, the application changes the chatbot's instructions according to the selected mood.

```text
                 ┌─────────────────┐
                 │      User       │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │  Select Mood    │
                 └────────┬────────┘
                          │
              ┌───────────┼───────────┐
              ▼           ▼           ▼
          😠 Angry     😂 Funny     😢 Sad
              │           │           │
              └───────────┼───────────┘
                          ▼
                 ┌─────────────────┐
                 │   System Prompt │
                 └────────┬────────┘
                          ▼
                 ┌─────────────────┐
                 │   AI Language   │
                 │      Model      │
                 └────────┬────────┘
                          ▼
                 ┌─────────────────┐
                 │ AI Mood-Based   │
                 │    Response     │
                 └─────────────────┘
```

**MoodBot turns a basic AI chatbot into an interactive personality-based conversational application.**
