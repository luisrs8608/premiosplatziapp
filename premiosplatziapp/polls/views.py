from django.shortcuts import render
from django.http import HttpResponse
from importlib_metadata import re
from rest_framework import viewsets
from .models import Question
from .serializers import QuestionSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes


def index(request):
    return HttpResponse("Hello world")

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    context = {}

    def set_context(self, request):
        self.context.update({
            'request': request
        })

    def list(self, request):
        """
        List all code questions, or create a new question.
        """
        queryset = self.get_queryset()
        self.set_context(request)
        serializer = QuestionSerializer(queryset, many=True, context=self.context)
        return Response(serializer.data)

    def update(self, request, pk, partial=False):
        """
        Retrieve, update or delete a code question.
        """
        try:
            question = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method in ['PUT', 'PATCH']:
            self.set_context(request)
            serializer = QuestionSerializer(
                question, context=self.context, data=request.data, partial=partial
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # elif request.method == 'DELETE':
        #     question.delete()
        #     return Response(status=status.HTTP_204_NO_CONTENT)