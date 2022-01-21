from django.db import models

# Django has built-in tables, one of which will be for users.
from django.contrib.auth.models import User

# Create your models here. These are how database tables are built in Django. These are classes that represent a table...the
# class is the table, and the attributes are the model columns. 

# This class is the model of what each task will look like.
class Task(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = 
    complete = 
    create = 
     
# 1. On_delete = What do we do with a task if the user gets deleted? Cascade sets us up so if the user gets deleted, so do 
# all the children tasks. If we did SET_NULL instead of Cascade, we could delete the user but the items would remain.
# Null allows some items to have missing information, Blank allows us to have blank spaces in the table.

# 2. We've set the character field for the title: max of 200 characters, same deal with null and blank.




