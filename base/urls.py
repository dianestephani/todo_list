# 2. Importing a path function to create URL patterns.
from django.urls import path 

# 3. Doing a mass import of all views.
from . import views

# 4. Creating a URL pattern that will be a list.

urlpatterns = [
    path('', views.taskList, name='tasks'),
]