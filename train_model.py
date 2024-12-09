from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle


queries = [
  
    "open youtube",
    "play music",
    "open google",
    "open facebook",
    "open twitter",
    "open vscode",
    "start notepad",
    "start calculator",
    "open file explorer",
    
    
    "create folder project",
    "create folder work/documents",
    "create folder my files/subfolder",
    "create file notes.txt",
    "create file report.docx",
    "create file hello_world.py",
    "create file resume.pdf in documents",
    
    
    "delete folder old_folder",
    "delete file report.docx",
    "rename file notes.txt to new_notes.txt",
    "move file report.docx to my documents",
    "copy file notes.txt to backup folder",
    
    
    "exit the program",
    "goodbye",
    "shut down assistant"
]

intents = [
   
    "open_website", 
    "open_website",
    "open_website",
    "open_website",
    "open_website",
    "open_application",  
    "open_application",
    "open_application",
    "open_application",
    "create_folder", 
    "create_folder",
    "create_folder",
    "create_file", 
    "create_file",
    "create_file",
    "create_file",
    "delete_folder", 
    "delete_file",
    "rename_file", 
    "move_file", 
    "copy_file",  
    "exit" 
]

# Vectorize the queries
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(queries)

# Train the Naive Bayes model
model = MultinomialNB()
model.fit(X, intents)

# Save the model and vectorizer using pickle
with open("intent_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Model and vectorizer saved successfully!")
