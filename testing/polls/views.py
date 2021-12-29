from django.shortcuts import render, get_object_or_404 # shortcut for 404
from django.http import HttpResponse, HttpResponseRedirect  # dont need if using render
from .models import Choice, Question # need to import the models
# from django.template import loader # this tells django to look for the files in templates, not needed if using render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html') # this tell django to use index.html
#     context = {
#         'latest_question_list': latest_question_list, # this maps template variable name to python object
#     }
#     return HttpResponse(template.render(context, request))


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context) # this uses render() to render the view
# Create your views here.

def test(request):
    return HttpResponse("<h1>Hello, world. You're at the polls test.</h1>") #looks like can take in html tags


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist") # return 404 if question does not exist
#     return render(request, 'polls/detail.html', {'question': question})


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id) # either get object or return 404
#     return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

#doc say can return a Http404 or a HttpResponse

# changed index, details and results to generic views

class IndexView(generic.ListView):
    template_name = 'polls/index.html'  #specify which template to use, else it defaults to appname/modelname_list.html
    context_object_name = 'latest_question_list' # tell the view to set the context variable as latest_question_list so the template can render this

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Question.objects.order_by('-pub_date')[:5]

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question # tells the generic views to act upon this model
    template_name = 'polls/detail.html' #specify which template to use, else it defaults to appname/modelname_detail.html
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question  # tells the generic views to act upon this model
    template_name = 'polls/results.html'  #specify which template to use, else it defaults to appname/modelname_detail.html
