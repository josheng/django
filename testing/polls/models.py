import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200) # this looks similar to db migration/schema from rails
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text # this returns the question text when u query the db API instead of just class

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now # replace btm line so it does not return true for future date
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1) # this is a custom method


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # this is to define a foreign key related to question model
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# python3 manage.py makemigrations polls -> run this to create the model/migration file
# python3 manage.py migrate -> this will do the migration
