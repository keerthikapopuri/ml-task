import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from IPython.display import Markdown
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_vertexai import ChatVertexAI, HarmBlockThreshold, HarmCategory
from vertexai.generative_models import Content, GenerativeModel, Part

# Configure the API with the provided API key
apikey = "AIzaSyDL3prPAuMrAMakO4YhJrq_vX6i5AdIeruf"
genai.configure(api_key=apikey)
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])
import regex as re

# Initial price set by the bot
initial_price = 1000  # Example price in USD
min_price = 600  # Minimum acceptable price for negotiation

def negotiate_price(user_price):
    global initial_price, min_price
    if user_price >= initial_price:
        return "Deal accepted"
    elif user_price >= min_price - 200:
        counter_offer = (user_price + initial_price) // 2
        initial_price = counter_offer
        return counter_offer
    else:
        return 600

def chat_response(user_price, negotiation_price, polite):
    """Get response from the Gemini model"""
    if polite:
      conversation = model.generate_content(f"The manufacturer hired you for negoitation of his business. Customer asked for {user_price} and the base price is 1000 USD and the minimum price the manufacturer can give it to is 500. The user is polite so you can give discount on the negoitation price a bit. Write imperatively a reply to the user offering {negotiation_price}. Do not mention about internal functions we are using to calculate. just reply as a chatbot")
    else:
      conversation = model.generate_content(f"The manufacturer hired you for negoitation of his business. Customer asked for {user_price} and the base price is 1000 USD and the minimum price the manufacturer can give it to is 500. Write imperatively a reply to the user offering {negotiation_price}. Do not mention about internal functions we are using to calculate. just reply as a chatbot")
    return conversation

def sentiment_analysis(user_message):
    """Simple sentiment analysis"""
    if "please" in user_message.lower() or "kindly" in user_message.lower():
        return True  # The customer seems polite
    return False  # Not polite

def main():
    """Main chatbot loop"""
    print("Chatbot: Hello! Let's negotiate a price for the product.")
    print(f"Chatbot: The starting price is {initial_price} USD.")
    
    while True:
        # Get user input
        user_message = input("Customer: ")
        
        # Extract user price proposal
        try:
            match = re.search(r'\d+', user_message)  # Find the first integer in the message
            user_price = int(match.group())
        except (ValueError, AttributeError):
            user_price = initial_price  # Use default if no price mentioned
        
        # Determine if the user's message is polite
        is_polite = sentiment_analysis(user_message)

        # Get negotiation result based on user's price
        negotiation = negotiate_price(user_price)
        if negotiation == "Deal accepted":
            print("Chatbot: Thank you for shopping with us.")
            break
        
        # Get a conversation response from the Gemini AI model
        ai_response = chat_response(user_price, negotiation, is_polite)
        print(ai_response.text)

if __name__ == "__main__":
    main()



