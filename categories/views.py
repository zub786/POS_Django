from django.shortcuts import render
from categories.models import Category
# Create your views here.


def index(request):
    categories = Category.objects.all()
    return render(request, 'categories/index.html', {'categories': categories})