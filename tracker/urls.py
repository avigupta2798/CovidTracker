from django.urls import path
from tracker import views

urlpatterns = [
    path('', views.track_covid_data, name='tracker')
]