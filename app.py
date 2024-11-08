import streamlit as st
import google.generativeai as genai
import os

# Initialize Gemini API key and model
def initialize_gemini():
    try:
        api_key = st.secrets["GEMINI_API_KEY"] if "GEMINI_API_KEY" in st.secrets else os.getenv("GEMINI_API_KEY")
        if not api_key:
            st.error("Gemini API key is missing. Please add it to secrets or environment variables.")
            return None
        genai.configure(api_key=api_key)
        return genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config={
                "temperature": 0.7,
                "top_p": 0.95,
                "top_k": 50,
                "max_output_tokens": 1000,
            },
        )
    except Exception as e:
        st.error(f"Failed to initialize Gemini API client: {e}")
        return None

# Function to interact with Gemini chatbot
def chat_with_gemini(model, input_query):
    try:
        # Start a new chat session
        chat_session = model.start_chat(history=[])
        # Send the message and get a response
        response = chat_session.send_message(input_query)
        # Return the generated response
        return response.text.strip()
    except Exception as e:
        st.error(f"Error during chat response generation: {e}")
        return "I'm sorry, but I'm having trouble processing your request."

# Streamlit app UI
def main():
    st.title("Chatbot AI Project")
    st.write("Welcome to the chatbot! Ask me anything.")

    # Initialize model
    model = initialize_gemini()
    if model is None:
        return  # Stop app execution if the model fails to initialize

    # Initialize session state for chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("What's on your mind?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = chat_with_gemini(model, prompt)
                st.markdown(response)

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
