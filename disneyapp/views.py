from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import *

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

def get_disney_data(request):
    comments =  DisneylandReview.objects.all().values()
    df = pd.DataFrame(comments)
    branch = df['branch']
    hongkong_data = df[df['branch'] == 'Disneyland_HongKong']
    hongkong_text = hongkong_data[['review_id','text']]
    print(hongkong_text)

   