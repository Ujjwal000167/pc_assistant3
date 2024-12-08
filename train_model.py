from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Training Data
queries = [
    "open youtube",
    "play music",
    "what time is it",
    "exit the program"
]
intents = [
    "open_website",
    "play_music",
    "get_time",
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
