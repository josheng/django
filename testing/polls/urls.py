from django.urls import path

from . import views

app_name = 'polls' # this added namespace so django wont be confused if there is a view with same name but diff app
urlpatterns = [
    # path(
    #     '', views.index, name='index'
    # ),  # assuming this is ref to views file with index method, first arg is route
    # path(
    #     'test', views.test, name='test'
    # ),  # have to define a route name, name arg is probably like rails route name
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'), # kind of like rails routes referencing to ID
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    #
    # refactoring, using generic views
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), # generic views expect the primary key value to be called pk instead of question_id
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
