# Importing TextBlob to help the chatbot understand language nuances.
from textblob import TextBlob # type: ignore
intents = {
    "hours":{
        "keywords":["hours","open","close"],
        "response": "We are open from 9 AM to 5 PM, Monday to Friday."
    },
    "return":{
        "keywords":["refund", "money back", "return"],
        "response":"I'd be happy to help you with the return process. Let me transfer you to a live agent."
    }
}

def get_response(message):
    message = message.lower()

    for intent in intents.values():  
        if any(word in message for word in intent["keywords"]):
            return intent["response"]
    # Analyzing the sentiment of the user's message.
    sentiment = TextBlob(message).sentiment.polarity

    return ("That's so great to hear!" if sentiment > 0 else "I'm so sorry to hear that. How can I help?" if sentiment < 0 else "I see. Can you tell me more about that?")

# Defining the ChatBot class for interaction.
def chat():
    print("Chatbot: Hi, How can I help you today")

    while(user_message := input("You: ").strip().lower()) not in ['exit', 'quit', 'bye']:
        print(f"\nChatbot: {get_response(user_message)}")
            
          
if __name__ == "__main__":
    # Creating the chatbot and starting the chat loop.
    chat()
