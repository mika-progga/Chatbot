import streamlit as st

# this is mandatory , first define the set_page_config then any other st.
st.set_page_config(page_title="AI Chatbot", layout="centered")

# tells streamlit to load only once and reuse it 
@st.cache_resource
def load_model():
    from transformers import pipeline
    return pipeline("text-generation", model="tiiuae/falcon-rw-1b")

# Load the chatbot model
chatbot = load_model()

# Title
st.title("🤖 Local Chatbot (Falcon RW 1B)")

# Chat history
if "history" not in st.session_state:
    st.session_state.history = [] #empty list keep track of previous questions

# User input
user_input = st.text_input("You:", key="input")

# Response generation
if user_input:
    response = chatbot(user_input, max_new_tokens=50)
    bot_reply = response[0]['generated_text'].replace(user_input, "").strip()
    

    # Save chat , both user and chatbot response will be daved to the chat history
    st.session_state.history.append(("🧑 You", user_input))
    st.session_state.history.append(("🤖 Bot", bot_reply))

# Show chat history
#f-string (formatted string literal) in Python
#st.session_state.history is a list of tuples where sender is who is speaking either user or bot
for sender, message in st.session_state.history:
    st.markdown(f"**{sender}:** {message}")
