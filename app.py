import streamlit as st
import pickle

# Set up the page configuration (title and icon)
st.set_page_config(
    page_title="Tweet Sentiment Predictor",
    page_icon="🤖",  # You can use an emoji or a local file path for the icon
)

# Load the saved model and vectorizer
with open('Model/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('Model/vectorizer.pkl', 'rb') as vec_file:
    vectorizer = pickle.load(vec_file)

# Set up the Streamlit app layout
st.title("Tweet Sentiment Predictor")

st.write("Enter a tweet below to know its predicted sentiment:")

# User text input
user_input = st.text_area("Tweet text", "I'm so happy about the news!")

# Mapping the numeric prediction to sentiment labels
sentiment_mapping = {
    0: "Negative",
    1: "Neutral",
    2: "Positive"
}
# When the user clicks the 'Predict' button, process the input
if st.button("Predict"):
    # Transform the input text using the loaded TF-IDF vectorizer
    transformed_input = vectorizer.transform([user_input])

    # Use the model to predict the sentiment
    prediction = model.predict(transformed_input)

    # Map the numeric prediction to its corresponding sentiment
    predicted_sentiment = sentiment_mapping[prediction[0]]

    st.write("Predicted Sentiment:", predicted_sentiment)
