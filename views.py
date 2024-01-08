# mysite/views.py
from django.shortcuts import render
from .models import Question, Choice

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'question_list.html', {'questions': questions})

def choice_list(request, question_id):
    choices = Choice.objects.filter(question_id=question_id)
    return render(request, 'choice_list.html', {'choices': choices})
