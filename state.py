import os
import google.generativeai as genai
import reflex as rx

class TutorialState(rx.State):

    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]


    async def answer(self):
        # Our chatbot has some brains now!
        genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

        # Initialize the GenerativeModel with the desired model name
        model = genai.GenerativeModel('gemini-1.0-pro')

        # Generate content using the model
        response = model.generate_content(self.question)

        # Extract the text content of the response
        answer = response.text.strip()

        # Add to the answer as the chatbot responds.
        self.chat_history.append((self.question, answer))

        # Clear the question input.
        self.question = ""
        # Yield here to clear the frontend input before continuing.
        yield
