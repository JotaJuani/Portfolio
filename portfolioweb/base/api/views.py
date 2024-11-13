from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Question, Country
from django.db import models


@api_view(['GET'])
def votingData(request):
    questions = Question.objects.all()
    backend = Question.objects.filter(answer='Backend').count()
    frontend = Question.objects.filter(answer='Frontend').count()
    fullstack = Question.objects.filter(answer='Fullstack').count()
    recruiter = Question.objects.filter(answer='Recruiter').count()

    return Response({'backend': backend,
                     'frontend': frontend,
                     'fullstack': fullstack,
                     'recruiter': recruiter, })


@api_view(['GET'])
def WorldCountryData(request):
    country_counts = list(Country.objects.values(
        'answer').annotate(count=models.Count('answer')))
    unformated_data = {item['answer']: item['count'] for item in country_counts}
    data = [{"name": country, "value": count} for country, count in unformated_data.items()]
    print(data)
    return Response(data)
