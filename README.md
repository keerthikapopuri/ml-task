# Price Negotiation Chatbot

## Overview

This project implements a price negotiation chatbot designed to interact with customers and negotiate prices for products. The chatbot utilizes user inputs to adjust its offers based on the customer's proposed price and their politeness, providing an engaging and dynamic experience.

## Features

- **Initial and Minimum Pricing**: The bot starts with a predefined initial price and a minimum acceptable price for negotiation.
- **Price Negotiation Logic**: The bot evaluates user proposals and generates counter-offers based on specified rules.
- **Politeness Detection**: The chatbot uses simple sentiment analysis to determine if the customer is polite, influencing its response and negotiation strategy.
- **Conversational AI Integration**: The bot simulates responses using a conversational AI model (Gemini) to provide natural and engaging replies.

## Getting Started

### Prerequisites

- Python 3.x
- Required libraries:
  - `regex` for regular expression matching
  - An AI model or API (like Gemini) for generating conversational responses

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install necessary packages:
   ```bash
   pip install regex
   ```

### Usage

1. Open your terminal or command prompt.
2. Navigate to the project directory.
3. Run the chatbot:
   ```bash
   python chatbot.py
   ```
4. Follow the prompts to interact with the chatbot.

### Example Interaction

```
Chatbot: Hello! Let's negotiate a price for the product.
Chatbot: The starting price is 1000 USD.
Customer: Can I get it for 800 please?
Chatbot: I understand you're looking for a great deal, and I appreciate your interest in our product. While your target price of $700 is a bit lower than we can offer, I'd be happy to propose a price of $850.  This price point allows us to continue providing you with the quality and performance you expect, while also making this a very competitive deal. 

```

## Code Structure

- `initial_price`: Sets the starting price for negotiations.
- `min_price`: Defines the minimum price the chatbot can offer.
- `negotiate_price(user_price)`: Contains the logic for negotiating prices based on the user's input.
- `chat_response(user_price, negotiation_price, polite)`: Generates a response from the conversational AI model, adjusting the offer based on the user's politeness.
- `sentiment_analysis(user_message)`: Analyzes the user's message for politeness indicators.
- `main()`: The main loop that runs the chatbot, handling user input and responses.

