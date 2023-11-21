from django.urls import path
from disneyapp import views

urlpatterns = [
    path("importdata",views.import_data_csv),
    path("alldata",views.get_disney_data),
]