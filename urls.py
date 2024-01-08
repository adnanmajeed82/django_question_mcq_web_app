# mysite/urls.py
from django.urls import path
from .views import question_list, choice_list
from django.contrib import admin

urlpatterns = [
    path('questions/', question_list, name='question_list'),
    path('choices/<int:question_id>/', choice_list, name='choice_list'),
    path('admin/', admin.site.urls),
]
