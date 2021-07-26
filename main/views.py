from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Neighbourhood
# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

def hoods(request):
    all_hoods = Neighbourhood.objects.all()

    params = {
        'all_hoods': all_hoods
    }
    return render(request, 'all_hoods.html', params)