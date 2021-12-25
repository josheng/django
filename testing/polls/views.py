from django.shortcuts import render
from django.http import HttpResponse
from .models import Question # need to import the models
from django.template import loader # this tells django to look for the files in templates


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html') # this tell django to use index.html
    context = {
        'latest_question_list': latest_question_list, # this maps template variable name to python object
    }
    return HttpResponse(template.render(context, request))
# Create your views here.

def test(request):
    return HttpResponse("<h1>Hello, world. You're at the polls test.</h1>") #looks like can take in html tags


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

#doc say can return a Http404 or a HttpResponse
