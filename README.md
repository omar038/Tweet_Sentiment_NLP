# Tweet Sentiment Analysis

## Overview
This project focuses on sentiment analysis of tweets using machine learning. It includes a workflow for data preprocessing, model training, evaluation, and the deployment of a web-based prediction app using Streamlit.
![WebApp](https://github.com/omar038/Tweet_Sentiment_NLP/blob/main/Gif/TweetSentimentPredictor.gif)

## Features
- **Data and Model Creation**:
  - Data preprocessing (handling missing values and label encoding)
  - Text vectorization using TF-IDF
  - Comparison of multiple machine learning models:
    - Naive Bayes
    - Logistic Regression
    - Linear Support Vector Machine (SVM)
    - Random Forest
    - K-Nearest Neighbors (KNN)
  - Evaluation of models using accuracy scores and confusion matrices
- **Web Application**:
  - User-friendly interface to input tweets for real-time sentiment prediction
  - Display of predicted sentiment (Positive, Neutral, or Negative)

## Dataset
The dataset consists of tweets with labeled sentiment categories. Missing values were removed, and sentiment labels encoded into numeric form.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tweet_sentiment.git

## Usage
Preprocess the dataset:

Drop missing values

Encode sentiment labels

Vectorize the text data using TF-IDF:

Convert tweets into numerical representations.

Train and evaluate machine learning models:

Compare accuracy scores of different models.

Visualize performance using confusion matrices.

## Results
All models tested achieved an accuracy of 100% on the test data, demonstrating effective sentiment classification.

## Technologies Used
Python

Scikit-learn

Matplotlib (for visualization)

## License
This project is licensed under the MIT License.
