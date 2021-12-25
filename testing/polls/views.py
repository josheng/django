from django.shortcuts import render, get_object_or_404 # shortcut for 404
from django.http import HttpResponse, Http404 # dont need if using render
from .models import Question # need to import the models
from django.template import loader # this tells django to look for the files in templates, not needed if using render


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html') # this tell django to use index.html
#     context = {
#         'latest_question_list': latest_question_list, # this maps template variable name to python object
#     }
#     return HttpResponse(template.render(context, request))


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context) # this uses render() to render the view
# Create your views here.

def test(request):
    return HttpResponse("<h1>Hello, world. You're at the polls test.</h1>") #looks like can take in html tags


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist") # return 404 if question does not exist
#     return render(request, 'polls/detail.html', {'question': question})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # either get object or return 404
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

#doc say can return a Http404 or a HttpResponse
