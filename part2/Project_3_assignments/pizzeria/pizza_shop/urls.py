"""Define url patterns for pizza shop"""


from django.urls import path
from . import views

app_name = 'pizza_shop'
urlpatterns = [
    # Home page 
    path('', views.index, name='index'),
]


