from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('project/<str:pk>/', views.projectPage, name='project'),
    path('add-project/', views.AddProject, name='add-project'),
    path('edit-project/<str:pk>/', views.EditProject, name='edit-project'),
    path('inbox/', views.inboxPage, name='inbox'),
    path('message/<str:pk>/', views.messagePage, name='message'),
    path('add-skill/', views.addSkill, name='skill-form'),
    path('add-endorsement/', views.addEndorsement, name='endorsement-form'),
    path('chart/', views.chartPage, name='chart'),
]
