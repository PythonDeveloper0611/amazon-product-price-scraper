# AI-Powered Personal Assistant

## Overview
This project is an AI-powered personal assistant that can manage your calendar, answer questions, and perform various tasks using natural language processing. The assistant uses OpenAI GPT for understanding and generating responses and integrates with Google Calendar API for scheduling events.

## Features
- Natural language processing using OpenAI GPT
- Calendar management with Google Calendar API
- Web interface for interacting with the assistant

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai_personal_assistant.git
   cd ai_personal_assistant
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Set up OpenAI API key:
   - Sign up for OpenAI API and get your API key.
   - Create a `.env` file and add your API key:
     ```
     OPENAI_API_KEY=your-openai-api-key
     ```

4. Set up Google Calendar API:
   - Enable the Google Calendar API in the Google Cloud Console.
   - Download the `credentials.json` file and place it in the project directory.

5. Run the application:
   ```bash
   flask run
   ```

## Usage
- Open your browser and go to `http://127.0.0.1:5000`.
- Ask questions and manage your calendar through the web interface.

## License
This project is licensed under the MIT License.