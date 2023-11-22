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

def classify_sentiment(score):
    if score and score > 0:
        return 'positive'
    elif score and score < 0:
        return 'negative'
    else:
        return 'neutral'

def calculate_sentiment_percentage(df):
    total_count = len(df)
    positive_percentage = (df[df['sentiment_category'] == 'positive'].shape[0] / total_count) * 100
    neutral_percentage = (df[df['sentiment_category'] == 'neutral'].shape[0] / total_count) * 100
    negative_percentage = (df[df['sentiment_category'] == 'negative'].shape[0] / total_count) * 100
    return positive_percentage, neutral_percentage, negative_percentage

def sentiment_HongKong(request):
    reviews_hongkong = DisneylandReview.objects.filter(branch='Disneyland_HongKong')
    df_hongkong = pd.DataFrame(list(reviews_hongkong.values()))

    df_hongkong['sentiment'] = df_hongkong['text'].apply(sentiment)
    df_hongkong['sentiment_category'] = df_hongkong['sentiment'].apply(classify_sentiment)
    positive_percentage, neutral_percentage, negative_percentage = calculate_sentiment_percentage(df_hongkong)
    print(df_hongkong)
    # print(df_hongkong[['review_id','text']])
    print("Branch: Hong Kong")
    print(f"Positive Percentage: {positive_percentage}%")
    print(f"Neutral Percentage: {neutral_percentage}%")
    print(f"Negative Percentage: {negative_percentage}%")
    
    context = {
        'branch': 'Hong Kong',
        'positive_percentage': positive_percentage,
        'neutral_percentage': neutral_percentage,
        'negative_percentage': negative_percentage,
    }
    return render(request, 'places.html', context)

def sentiment_Paris(request):
    reviews_paris = DisneylandReview.objects.filter(branch='Disneyland_Paris')
    df_paris = pd.DataFrame(list(reviews_paris.values()))

    df_paris['sentiment'] = df_paris['text'].apply(sentiment)
    df_paris['sentiment_category'] = df_paris['sentiment'].apply(classify_sentiment)
    positive_percentage, neutral_percentage, negative_percentage = calculate_sentiment_percentage(df_paris)
    print(df_paris)
    # print(df_hongkong[['review_id','text']])
    print("Branch: Paris")
    print(f"Positive Percentage: {positive_percentage}%")
    print(f"Neutral Percentage: {neutral_percentage}%")
    print(f"Negative Percentage: {negative_percentage}%")
    
    context = {
        'branch': 'Paris',
        'positive_percentage': positive_percentage,
        'neutral_percentage': neutral_percentage,
        'negative_percentage': negative_percentage,
    }
    return render(request, 'places.html', context)

def sentiment_California(request):
    reviews_california = DisneylandReview.objects.filter(branch='Disneyland_California')
    df_california = pd.DataFrame(list(reviews_california.values()))

    df_california['sentiment'] = df_california['text'].apply(sentiment)
    df_california['sentiment_category'] = df_california['sentiment'].apply(classify_sentiment)
    positive_percentage, neutral_percentage, negative_percentage = calculate_sentiment_percentage(df_california)
    print(df_california)
    # print(df_hongkong[['review_id','text']])
    print("Branch: California")
    print(f"Positive Percentage: {positive_percentage}%")
    print(f"Neutral Percentage: {neutral_percentage}%")
    print(f"Negative Percentage: {negative_percentage}%")
    
    context = {
        'branch': 'California',
        'positive_percentage': positive_percentage,
        'neutral_percentage': neutral_percentage,
        'negative_percentage': negative_percentage,
    }
    return render(request, 'places.html', context)
   