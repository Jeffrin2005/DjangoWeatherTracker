from django.urls import path
from . import views

urlpatterns = [
  # Renders the index page
  path('',views.index,name='index')

]