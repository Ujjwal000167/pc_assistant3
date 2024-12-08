import openai
import pickle
import webbrowser
import os
import datetime
import pyttsx3
import speech_recognition as sr
from config import apikey

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

# Load the trained model and vectorizer
with open("intent_model.pkl", "rb") as f:
    intent_model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Function to classify intent
def classify_intent(query):
    X = vectorizer.transform([query])
    intent = intent_model.predict(X)[0]
    return intent

# Function to speak text
def say(text):
    engine.say(text)
    engine.runAndWait()

# Function to take voice input
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query.lower()
        except Exception as e:
            print("Error:", e)
            return "Some error occurred."

# Function to open a website based on user query
def open_website(query):
    # Dictionary of popular websites
    websites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "wikipedia": "https://www.wikipedia.org",
        "facebook": "https://www.facebook.com",
        "twitter": "https://www.twitter.com",
        "instagram": "https://www.instagram.com",
        "github": "https://www.github.com",
        "linkedin": "https://www.linkedin.com"
    }

    # Check if the query contains a known website
    for website in websites:
        if website in query:
            webbrowser.open(websites[website])
            return True  # Successfully opened the website

    return False  # No known website found in query

# Function to search for a website based on user query
def search_web(query):
    # Remove the word 'search' or 'find' and perform a web search using Google
    search_query = query.replace("search", "").replace("find", "").strip()
    
    # Use webbrowser to open Google search results for the query
    search_url = f"https://www.google.com/search?q={search_query}"
    webbrowser.open(search_url)

# Main Function
if __name__ == "__main__":
    openai.api_key = apikey
    print("Welcome to PC Assistant!")
    say("Welcome to PC Assistant!")

    while True:
        query = take_command()

        if not query or "error" in query:
            continue

        intent = classify_intent(query)

        if intent == "open_website":
            if open_website(query):  # Try opening a website
                say("Opening the website...")
            else:
                say("Sorry, I couldn't find that website.")

        elif "search" in query or "find" in query:
            say("Searching the web...")
            search_web(query)  # Perform dynamic search

        elif intent == "play_music":
            say("Playing music...")
            music_path = "path/to/your/music.mp3"  # Update this path with your music file location
            os.system(f"start {music_path}")

        elif intent == "get_time":
            now = datetime.datetime.now().strftime("%H:%M")
            say(f"The time is {now}")

        elif intent == "exit":
            say("Goodbye!")
            break

        else:
            say("I didn't understand that. Let me try using AI.")
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=query,
                max_tokens=50
            )
            say(response["choices"][0]["text"].strip())


