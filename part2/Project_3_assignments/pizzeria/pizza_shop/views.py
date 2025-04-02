from django.shortcuts import render

from .models import Pizza

def index(request):
    """The home page for the Pizza shop"""
    return render(request, 'pizza_shop/index.html')

def pizzas(request):
    """Show all pizzas"""
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas': pizzas}
    return render(request, 'pizza_shop/pizzas.html', context)

def pizza(request, pizza_id):
    """Show a single pizza and all its topppings"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('topping')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizza_shop/pizza.html', context)
