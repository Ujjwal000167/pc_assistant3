# **ro A.I. - Personal Virtual Assistant**

**ro A.I.** is a voice-controlled personal assistant built with **OpenAI's GPT-3** model, capable of performing a variety of tasks like answering questions, opening websites, playing music, and more. It interacts with users through voice commands and provides responses using **text-to-speech**. This assistant aims to enhance productivity and offer a seamless, hands-free experience for the user.

---

## **Motive Behind the Project**

The **ro A.I.** project was created to build a personalized virtual assistant that can be controlled via voice. The assistant is intended to:
- **Automate Tasks**: Open websites, play music, and retrieve information without needing manual input.
- **Enhance Productivity**: Provide real-time responses to queries about the time, open applications, and facilitate other tasks.
- **Integrate AI**: Leverage OpenAI’s GPT-3 to offer human-like responses, enabling dynamic and intelligent interactions with users.

---

## **Technologies Used**

1. **Python**: The core programming language used to build the assistant.
2. **OpenAI API**:
   - **GPT-3 Model** (`text-davinci-003`) for generating responses to user queries.
   - The model allows the assistant to perform tasks such as answering questions and chatting naturally with users.
3. **SpeechRecognition**:
   - This library is used to capture voice input from the user via the microphone.
4. **Pyttsx3** (Windows version of text-to-speech):
   - Provides voice-based feedback using the system’s built-in speech synthesis engine.
5. **Webbrowser**:
   - Used to open websites based on user requests.
6. **Datetime**:
   - Retrieves the current time and reports it back to the user.
7. **OS**:
   - Used to interact with the file system (e.g., playing music files, opening apps).
8. **Scikit-learn**:
   - A powerful library for machine learning in Python.
   - Modules Used:
   - CountVectorizer : Converts text data (user queries) into numerical vectors, enabling the model to process and classify the data.
   - MultinomialNB : A Naive Bayes classification algorithm, efficient for text-based classification tasks like intent detection.
9. **Pickle**:
   - A Python module used to save and load the trained model and the vectorizer.     

---

## **Features**

- **Voice Recognition**: Recognizes and processes voice commands like “Open YouTube,” “Play music,” etc.
- **Web Automation**: Opens popular websites like **YouTube**, **Google**, and **Wikipedia**.
- **Text-to-Speech**: Responds to queries using voice feedback.
- **Time Reporting**: Tells the current time.
- **AI Integration**: Uses OpenAI's GPT-3 to respond to user queries with intelligent, context-based answers.
- **Application Launching**: Opens applications like **FaceTime** or **Password Manager** based on voice commands.
- **Music Playback**: Plays a predefined music file.

---

## **How to Set Up ro A.I.**

### **Step 1: Install Python 3.10 or Above**

Make sure **Python 3.10** or higher is installed on your machine. If not, you can download it from [Python's official website](https://www.python.org/downloads/release/python-3100/).

### **Step 2: Clone or Download the Project**

1. Clone the repository (if using version control):
   ```bash
   git clone https://github.com/yourusername/ro-ai.git

2. install the required libraries:
    ```bash
    pip install openai speechrecognition pyttsx3 pyaudio numpy
    pip install scikit-learn

3. Generate an API Key:
   -Go to OpenAI's API key page and create a new API key.
   -Add the API Key to config.py: Create config.py and add your key:
    ```bash
   apikey = "your-openai-api-key-here"

4. Run the Program :
    ```bash
    python main.py

---

## **Future Customizations and Add-ons**

Here are some ideas to expand and improve the PC Assistant project:

1. **Add More Commands**:  
   - Include more intents like checking the weather, sending emails, or setting alarms.  
   - Example: "What's the weather?" → Fetch weather data using APIs like OpenWeatherMap.

2. **Smart Device Integration**:  
   - Control smart home devices like lights or speakers using APIs like Philips Hue or Google Home.  
   - Example: "Turn off the lights."

3. **Sentiment Analysis**:  
   - Add sentiment analysis to respond to user emotions.  
   - Example: If the user seems sad, offer encouraging responses.  

4. **Multi-language Support**:  
   - Extend the assistant to support multiple languages using libraries like Google Translate API.  
   - Example: Recognize and respond in French or Spanish.  

5. **Voice Command Execution**:  
   - Train a custom voice model to recognize specific keywords for quick actions.  

6. **Custom Notifications**:  
   - Add reminders or calendar integration to notify users of important events.  

These features will make the assistant more versatile, user-friendly, and engaging!
