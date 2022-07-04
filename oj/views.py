from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from .serializers import OjSerializer 

from .models import Question
from rest_framework import viewsets

def index(request):
    context = { }
    return render(request, 'index.html',context)

class Questionslist(viewsets.ModelViewSet):  
    serializer_class = OjSerializer   
    queryset = OjSerializer.objects.all()  
def problems(request):
    problems_list = Question.objects.all()
    context = {'problems_list': problems_list}   
    return render(request,'oj/problems.html',context)
# Create your views here.
# def problems(request):
#     	latest_problems_list = Question.objects.all()[:5]
# 	template = loader.get_template('onlinejudge/problems.html')
# 	context = {
# 		'latest_problems_list': latest_problems_list,
# 	}
# 	return HttpResponse(template.render(context, request))