from django.shortcuts import render
from .models import PortFolio
# Create your views here.
def index(request):
    portfolios  = PortFolio.objects.all()
    data = {
        'portfolios' : portfolios
    }
    return render(request, 'Courses/index.html', data)
