from django.urls import path
from . import views
from .views import  votingData

urlpatterns = [path('api/', votingData, name='voting-data'),]
    