from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200) # this looks similar to db migration/schema from rails
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # this is to define a foreign key related to question model
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


# python3 manage.py makemigrations polls -> run this to create the model/migration file
# python3 manage.py migrate -> this will do the migration
