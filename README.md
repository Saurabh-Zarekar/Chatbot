
Chatbot AI Project with Streamlit and Gemini API

This project implements an interactive chatbot using [Streamlit](https://streamlit.io/) as the frontend and Google’s [Gemini API](https://developers.generativeai.google) for natural language generation. It’s designed for easy deployment, with support for session management and customizable model parameters, offering a versatile AI-powered conversational interface.

 Table of Contents

- [Features](features)
- [Demo](demo)
- [Setup and Installation](setup-and-installation)
- [Configuration](configuration)
- [Usage](usage)
- [Customization](customization)
- [Troubleshooting](troubleshooting)
- [Contributing](contributing)
- [License](license)

 Features

- Real-time Chat Interface: Built with Streamlit for an easy-to-use, interactive chat experience.
- Generative AI Integration: Uses the Gemini API to generate conversational responses, customizable for various use cases.
- Session Management: Maintains chat history using Streamlit’s session state, allowing for contextual conversations.
- Error Handling: Provides clear error messages for API or connection issues, guiding users through troubleshooting.

 Demo

Here’s a quick demo of the application:

> Run the app locally to experience a real-time chatbot interface. You can engage in conversations, ask questions, and get responses from the AI model.

 Setup and Installation

Prerequisites

- Python 3.7 or higher
- [Streamlit](https://docs.streamlit.io/) installed
- `google-generativeai` library for interacting with the Gemini API

 Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Saurabh-Zarekar/chatbot-ai-gemini.git
    cd chatbot-ai-gemini
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the Gemini API key:
   Add your Gemini API key to Streamlit secrets (`.streamlit/secrets.toml`) or set it as an environment variable:
   ```plaintext
   [secrets]
   GEMINI_API_KEY="your_api_key_here"
   ```

4. Run the application:
    ```bash
    streamlit run app.py
    ```

 Configuration

In the `initialize_gemini` function, you can customize the Gemini API model settings:
- Temperature: Controls creativity (lower values make responses more deterministic).
- Top-p and Top-k: Controls sampling diversity.
- Max Output Tokens: Sets the maximum token limit for responses.

Example:
```python
generation_config={
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 50,
    "max_output_tokens": 1000,
}
```

 Usage

- Start a Chat Session: Open the app and type into the input field.
- Receive Responses: The bot responds to each message, maintaining the context of the conversation.
- Chat History: All user and bot messages are stored and displayed, allowing for a continuous conversation experience.

 Customization

- Model Parameters: Adjust the generation parameters in the configuration to control the response style.
- Styling: Modify Streamlit components or add custom CSS for UI changes.
- Session Management: Explore Streamlit’s session state further if you want more complex chat history handling.

 Troubleshooting

- API Key Missing: If the API key is missing, an error will appear. Check that the key is set in `.streamlit/secrets.toml` or as an environment variable.
- Connection Issues: If the app fails to connect to the Gemini API, ensure that your internet connection is stable and that the API key is valid.

 Contributing

Contributions are welcome! Here’s how to get started:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes and commit them (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Open a Pull Request

 License

This project is licensed under the MIT License. See `LICENSE` for details.

