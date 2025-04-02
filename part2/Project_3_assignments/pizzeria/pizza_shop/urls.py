"""Define url patterns for pizza shop"""


from django.urls import path
from . import views

app_name = 'pizza_shop'
urlpatterns = [
    # Home page 
    path('', views.index, name='index'),
    # Page that shows all the pizzas
    path('pizzas/', views.pizzas, name='pizzas'),
    # Detail page for a single pizza
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
    
]


