import matplotlib.pyplot as plt
import pandas as pd

def visualize_sentiment(data):
    sentiment_counts = data['sentiment'].value_counts()
    plt.bar(sentiment_counts.index, sentiment_counts.values)
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.savefig('../results/sentiment_distribution.png')
    plt.show()
