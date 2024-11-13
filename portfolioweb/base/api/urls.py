from django.urls import path
from . import views


urlpatterns = [
    path('', views.votingData, name='voting-data'),
    path('', views.WorldCountryData, name='country-data'),

]
