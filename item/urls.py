from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path("browse/", views.browse, name="browse"),
    path('detail/<int:pk>', views.detail,  name='detail'),
    path('edit/<int:pk>', views.edit,  name='edit'),
    path('delete/<int:pk>', views.delete,  name='delete'),
    path('new', views.new,  name='new'),
]
