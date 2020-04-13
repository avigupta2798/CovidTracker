from django.urls import path
from home import views

urlpatterns = [
    path('', views.get_covid_data, name='home')
]