# Tweet Sentiment Analysis

## Overview
This project is a machine learning workflow for sentiment analysis of tweets. It transforms text data into numerical representations and compares various classification models to identify the most effective method for sentiment classification.

## Features
- Data preprocessing (handling missing values and label encoding)
- Text vectorization using TF-IDF
- Comparison of multiple machine learning models:
  - Naive Bayes
  - Logistic Regression
  - Linear Support Vector Machine (SVM)
  - Random Forest
  - K-Nearest Neighbors (KNN)
- Evaluation of model performance using accuracy scores and confusion matrices

## Dataset
The dataset consists of tweets labeled with sentiment categories. Missing values are removed, and sentiment labels are encoded into numerical representations.

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
