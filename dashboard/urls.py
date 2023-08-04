from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', view=views.index, name='index'),
    path('category/<str:c>', view=views.index, name='index'),
]

