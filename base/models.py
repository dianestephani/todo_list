from django.db import models

# Django has built-in tables, one of which will be for users.
from django.contrib.auth.models import User

# Create your models here. These are how database tables are built in Django. These are classes that represent a table...the
# class is the table, and the attributes are the model columns. 

# This class is the model of what each task will look like.
# Any time this file is changed, we need to re-run our migrations to update the database.


class Task(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
     

    # This sends completed items to the bottom of the list.
    class Meta: 
        ordering = ['complete']




# 1. On_delete = What do we do with a task if the user gets deleted? Cascade sets us up so if the user gets deleted, so do 
# all the children tasks. If we did SET_NULL instead of Cascade, we could delete the user but the items would remain.
# Null allows some items to have missing information, Blank allows us to have blank spaces in the table.

# 2. We've set the character field for the title: max of 200 characters.

# 3. In description we've set a text field, which hosts longer text than a character field.

# 4. Boolean field, true or false. By setting the default to false, any new items we add will appear as to-do rather than complete.

# 5. Auto Now Add will automatically create a time stamp when an item is created.

# Left off at 13:31




