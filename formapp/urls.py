from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_view, name='form'),
    path('show/', views.show_data, name='show_data'),
]
