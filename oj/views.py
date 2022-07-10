from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import Question,solution
from .our_forms import code_form, problem_form, testcase_form
from .code_validation1 import check_code

def display_problems(request):
    context={
        'probs': Question.objects.all()
    }
    return render (request, 'problem_page.html',context)

def problem_detail(request, prob_id):
    obj=get_object_or_404(Question, id = prob_id)
    if request.method == 'POST':
        form=code_form(request.POST)
        if(form.is_valid()):
            sub=form.save()
            sub.curr_problem=obj
            sub.save()
            check_code(sub)
        return redirect('past_submissions',prob_id)
    else:
        form=code_form()
        context = {
            'data': Question.objects.get(id=prob_id),
            'form': form,
        }
        # print(form.is_valid())
        # print(problem.objects.get(id=prob_id).name)
        # print(form.errors.as_data)
        template='detail_problem.html'
        return  render (request, template, context)

def submit(request,prob_id):
    obj=Question.objects.get(id=prob_id)
    qs=solution.objects.filter(curr_problem=obj)
    if(len(qs)==0):
        template='no_submission.html'
        return render(request,template)
    context= {
        'qs': qs
    }
    template='submission.html'
    return render(request,template,context)        

# from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponseRedirect, HttpResponse, Http404
# from django.urls import reverse
# from django.template import loader
# from django.shortcuts import render
# from django.http import HttpResponse
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# # from api import serializers
# from .serializers import OjSerializer
# # from .models import Note
# from .utils import getQuesionList, getProblemDetail,ProblemSubmit
# from .models import Question, solution,testcase

# @api_view(['GET', 'POST'])
# def getProblems(request):
#     if request.method == 'GET':
#         return getQuesionList(request)    

# @api_view(['GET','POST'])
# def getProbDetail(request, pk):
#     if request.method == 'GET':
#         return getProblemDetail(request, pk)
#     if request.method == 'POST':
#         return ProblemSubmit(request,pk)         