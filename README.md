# WhatsApp Customer Support Bot for Airbnb FAQ

This project is a WhatsApp customer support bot designed to handle frequently asked questions (FAQs) related to Airbnb. The bot leverages advanced AI models and natural language processing to provide accurate and helpful responses to user queries.

## Key Features

- **RAG (Retrieval-Augmented Generation)**: Combines retrieval-based and generation-based methods to improve the accuracy and relevance of responses.
- **Llama2 and OpenAI Integration**: Utilizes Llama2 from Ollama and OpenAI models for generating and embedding responses.
- **Ollama and OpenAI Embeddings**: Employs embeddings from both Ollama and OpenAI to enhance the bot's understanding of user queries.
- **LangChain Framework**: Utilizes LangChain, a framework for building applications with LLMs, to streamline the development process.
- **WhatsApp API Integration**: Connects to WhatsApp using the WhatsApp API, allowing users to interact with the bot through their WhatsApp accounts.
- **Flask Web Framework**: Uses Flask to handle the web framework and navigate between different components of the application.

## Setup and Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/light-y44/Whatsapp_customer_support_bot.git
   cd Whatsapp_customer_support_bot
2. **Create and activate a virtual environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
4. **Set up environment variables:**
- **Create a .env file in the root directory.**
- **Add your API keys and other configuration settings to the .env file.**

# Usage
To interact with the bot, simply send a message to the WhatsApp number associated with the bot. The bot will respond with relevant answers to your Airbnb-related queries.

# License 
This project is licensed under the MIT License. See the LICENSE file for more details.

# Acknowledgements
This project is based on code from Datalumina B.V. with modifications and additional content added by Devansh Gupta.


