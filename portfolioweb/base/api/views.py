from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Question
from .serializers import QuestionSerializer


@api_view(['GET'])
def votingData(request):
    questions = Question.objects.all()
    backend = Question.objects.filter(answer='Backend').count()
    frontend = Question.objects.filter(answer='Frontend').count()
    fullstack = Question.objects.filter(answer='Fullstack').count()

    print(f"Backend: {backend}, Frontend: {frontend}, Fullstack: {fullstack}")

    return JsonResponse({'backend': backend,
                         'frontend': frontend,
                         'fullstack': fullstack, })
