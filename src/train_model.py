from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

def train_model(data):
    tfidf = TfidfVectorizer(max_features=5000)
    X = tfidf.fit_transform(data['cleaned_text']).toarray()
    y = data['sentiment']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Save model
    joblib.dump(model, '../models/logistic_regression_model.pkl')
    return model, X_test, y_test
