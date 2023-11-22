from django.urls import path
from disneyapp import views

urlpatterns = [
    path("importdata",views.import_data_csv),
    path("sentimentHK",views.sentiment_HongKong),
    path("sentimentPS",views.sentiment_Paris),
    path("sentimentCL",views.sentiment_California)
]