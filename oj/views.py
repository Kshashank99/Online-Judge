from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from api import serializers
from .serializers import OjSerializer
# from .models import Note
from .utils import getQuesionList, getProblemDetail,ProblemSubmit
from .models import Question, solution,testcase

@api_view(['GET', 'POST'])
def getProblems(request):
    if request.method == 'GET':
        return getQuesionList(request)    

@api_view(['GET','POST'])
def getProbDetail(request, pk):
    if request.method == 'GET':
        return getProblemDetail(request, pk)
    if request.method == 'POST':
        return ProblemSubmit(request,pk)         