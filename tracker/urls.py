from django.urls import path
from tracker import views

urlpatterns = [
    path('tracker/', views.track_covid_data, name='tracker')
]