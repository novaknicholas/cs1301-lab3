# Lab 3: Chatbot page
#
# A chatbot built with Pydantic AI (see the Pydantic AI pages on Canvas).
# It should:
#   - use a Pydantic AI Agent with instructions that fit your project's theme (no tools yet)
#   - use Streamlit's chat elements: st.chat_message and st.chat_input
#   - remember the conversation (message_history, saved in st.session_state)
#   - use try/except so an error shows a message instead of crashing the page
#   - stay on theme, without using any API or external data
#
# Your Gemini API key goes in .streamlit/secrets.toml as GOOGLE_API_KEY.

import streamlit as st
from pydantic_ai import Agent
from pydantic_ai.models.fallback import FallbackModel

agent = Agent(
    FallbackModel(
        "google:gemini-3.5-flash-lite",
        "google:gemini-3.1-flash-lite",
        "google:gemini-3.8-flash"
    ),
    instructions=(
        "You are a friendly, upbeat assistant for Apple products. "
        "Only talk about Apple products and their specifications. "
        "Give short, simple, and easy to understand responses. "
        "You cannot look up live data, so answer from general knowledge and say when you're not sure. "
        "If the user asks about a topic unrelated to Apple topics, shift it back to Apple products or say you only help with Apple products in a friendly manner."
    ),
)

if "memory" not in st.session_state:
    st.session_state.memory = []

if "messages" not in st.session_state:
    st.session_state.messages = []

for role, message in st.session_state.messages:
    with st.chat_message(role):
        st.write(message)

prompt = st.chat_input("Ask about Apple products...")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)

    st.session_state.messages.append(("user", prompt))

    try: 
        with st.spinner("Thinking..."):
            result = agent.run_sync(
                prompt, message_history = st.session_state.memory
            )

        st.session_state.memory = result.all_messages()

        with st.chat_message("assistant"):
            st.write(result.output)

        st.session_state.messages.append(("assistant", result.output))

    except Exception:
        st.error("Sorry, something went wrong. Please try again.")
