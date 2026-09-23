import streamlit as st
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

st.set_page_config(page_title="Mood AI Chatbot", page_icon="🤖", layout="centered")

MODES = {
    "Angry 😡": "You are an angry AI agent. You respond aggressively and impatiently.",
    "Funny 😂": "You are funny AI agent. You respond with humor and jokes.",
    "Sad 😢": "You are sad AI agent. You will always respond in a sad way.",
}


@st.cache_resource
def get_model():
    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.1-8B-Instruct",
        task="text-generation",
        temperature=0.7,
        max_new_tokens=100,
    )
    return ChatHuggingFace(llm=llm)


model = get_model()

st.title("🤖 Mood-Based AI Chatbot")
st.caption("A simple LangChain + HuggingFace chatbot with switchable personalities.")

# --- Mode selection (sidebar) ---
with st.sidebar:
    st.header("Choose your AI mode")
    selected_label = st.radio("Pick a personality:", list(MODES.keys()), index=0)
    mode = MODES[selected_label]

    if st.button("🔄 Reset Chat", use_container_width=True):
        st.session_state.messages = [SystemMessage(content=mode)]
        st.rerun()

# --- Session state init / mode change handling ---
if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content=mode)]
    st.session_state.active_mode_label = selected_label

# If user switches mode mid-conversation, restart with the new system prompt
if st.session_state.get("active_mode_label") != selected_label:
    st.session_state.messages = [SystemMessage(content=mode)]
    st.session_state.active_mode_label = selected_label
    st.rerun()

# --- Render chat history (skip the SystemMessage) ---
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# --- Chat input ---
prompt = st.chat_input("You : ")
if prompt:
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.invoke(st.session_state.messages)
        st.markdown(response.content)

    st.session_state.messages.append(AIMessage(content=response.content))