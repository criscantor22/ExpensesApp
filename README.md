# ✈️ TravelAI Expense Assistant

AI-powered travel expense reporting and compliance validation platform built for the **TCS AI Friday Season 2 Hackathon**.

## Overview

TravelAI Expense Assistant helps corporate travelers automate the expense reporting process by uploading receipts and travel itineraries, generating expense reports, validating expenses against company policies, and providing AI-powered insights through a conversational assistant.

## Features

### 📄 Receipt Upload
- Upload multiple receipt files
- Supports JPG, JPEG, PNG, and PDF formats
- Receipt preview functionality

### 🛫 Travel Itinerary Upload
- Upload travel itineraries
- Supports PDF and CSV formats

### 📊 Expense Report Generation
- Automatic expense report creation
- Expense categorization
- Total expense calculation
- Downloadable CSV reports

### ⚠️ Policy Compliance Validation
- Configurable meal expense limits
- Configurable hotel expense limits
- Automatic policy violation detection
- Compliance scoring

### 🤖 Expense Copilot
- Natural language interaction
- AI-powered expense analysis
- Policy compliance explanations
- Expense insights and recommendations

## Technology Stack

- Python
- Streamlit
- Pandas
- OpenAI API
- Pillow (PIL)
- Python Dotenv

## Project Structure

ExpensesApp/

├── app.py

├── requirements.txt

├── README.md

├── data/

├── models/

├── services/

└── tests/

## Installation

### Clone the Repository

##bash
git clone https://github.com/criscantor22/ExpensesApp.git
cd ExpensesApp

##install dependencies
pip install -r requirements.txt

##config the env file
OPENAI_API_KEY=your_api_key_here

##run the app
python -m streamlit run app.py

https://chatgpt.com/share/6a22fddc-b368-83e8-b705-56b038f6168f
