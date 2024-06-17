from django.shortcuts import render

# Create your views here.
def index(request):
    params = {}
    return render(request, 'home/index.html')
def product(request):
    params = {}
    return  render(request, 'home/product.html')