from django.contrib import admin

from .models import Question

admin.site.register(Question) # this register the question model to be accessed via admin site
