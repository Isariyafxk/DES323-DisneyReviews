from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import *

#  nltk - text sentiment analysis
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def import_data_csv(request):
    csv_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vS4EPpyFHzOACG9rfzqk3bJ0PbCawzX24IgYrYptGgi0cvDo4IH7frGmYuNBdLBzYuW0MHxv8EYoBDA/pub?output=csv'
    df = pd.read_csv(csv_url)
    data_sets = df[["Review_ID","Rating","Review_Text","Branch"]]
    sucesss = []
    errors = []
    for index, row in data_sets.iterrows():
        instance = DisneylandReview(
            review_id = int(row['Review_ID']),
            rating = int(row['Rating']),
            text = row['Review_Text'],
            branch = row['Branch'],
        )
        try:
            instance.save()
            sucesss.append(index)
        except:
            errors.append(index)
    return JsonResponse({"success_indexes":sucesss,"error_index":errors})

#text analysis function-> Negative(-1 - -0.25) Neutral(-0.25 - 0) Positive(+1)
nltk.download('vader_lexicon')

def sentiment(text):
    text_score = SentimentIntensityAnalyzer().polarity_scores(text)
    return text_score['compound']

def get_disney_data(request):
    review_texts =  DisneylandReview.objects.all().values()
    df = pd.DataFrame(review_texts)
    branch = df['branch']
    # hongkong_data = df[df['branch'] == 'Disneyland_HongKong']
    # hongkong_text = hongkong_data[['review_id','text','branch']]
    # print(hongkong_text)
    df['sentiment'] = df['text'].apply(sentiment)
    # print(df[['id', 'branch', 'text', 'sentiment']])
    df['sentiment_category'] = df['sentiment'].apply(lambda score: 'positive' if score > 0 else 'negative' if score < 0 else 'neutral')
    print( df['sentiment_category'])

def generate_catagories(request):
    categories = DisneylandReview.objects.filter(categories = categories)
    reviews = DisneylandReview.objects.all().values()
    df = pd.DataFrame(reviews)
    df['sentiment'] = df['text'].apply(sentiment)
    print(df['categories'])
    categories = df['sentiment'].apply(lambda score: 'positive' if score > 0 else 'negative' if score < 0 else 'neutral')
    print(df['categories'])
    categories.save()