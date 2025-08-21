# Linkedin-post-generator
LinkedIn Post Generator

This project helps LinkedIn influencers create fresh posts that match their own writing style. By analyzing their past content, the tool learns their tone, style, and common topics, and then generates new posts that feel authentic and consistent.

<img src="resources/tool.jpg"/>
Example Use Case

Suppose Mohan is a LinkedIn influencer who regularly shares content. Instead of struggling to draft new posts from scratch, Mohan can upload his previous posts into this tool. The system will:

Identify topics, tone, and structure from past posts

Let Mohan choose a topic, preferred length, and language

Generate new posts that align with his established style

⚙️ How It Works (Architecture)
<img src="resources/architecture.jpg"/>

Stage 1: Analyze Past Posts

Extract key attributes such as topic, language, and length from the influencer’s past LinkedIn posts.

Stage 2: Generate New Posts

Based on the chosen topic, language, and length, the system uses a few-shot learning approach with relevant past posts to guide the LLM.

The generated post matches the influencer’s writing style.

🚀 Setup Instructions

Get an API Key

Create a Groq API key from: https://console.groq.com/keys

Add it to your .env file as:

GROQ_API_KEY=your_api_key_here


Install Dependencies

pip install -r requirements.txt


Run the Application

streamlit run main.py
