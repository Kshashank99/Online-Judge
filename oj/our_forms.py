# from .our_forms import code_form, problem_form, testcase_form

from django import forms
from .models import solution, Question, testcase

class code_form(forms.ModelForm):
    code = forms.CharField(widget = forms.Textarea)
    class  Meta:
        model = solution
        fields = ['code']

class problem_form(forms.ModelForm):
    name = forms.CharField()
    statement = forms.CharField(widget = forms.Textarea)
    difficulty = forms.CharField()
    class Meta:
        model = Question
        fields = ['name', 'statement', 'difficulty']

class testcase_form(forms.ModelForm):
    input = forms.CharField(widget = forms.Textarea)
    output = forms.CharField(widget = forms.Textarea)
    class Meta:
        model = testcase
        fields = ['input', 'output']
