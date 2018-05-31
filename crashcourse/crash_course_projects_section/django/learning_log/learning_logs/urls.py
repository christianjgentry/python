"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""Defines URL patterns for learning_logs"""
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),


#Show all topics.
path('topics/', views.topics, name='topics'),

#Detail page for a single topic.
path('topics/<int:topic_id>/', views.topic, name='topic'),

#Page for adding a new topic.
path('new_topic/', views.new_topic, name='new_topic'),

#Page for adding a new entry.
path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

]
