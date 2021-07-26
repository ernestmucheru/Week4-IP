from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import NeighbourHood
from .forms import NeighbourHoodForm
# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

def hoods(request):
    all_hoods = NeighbourHood.objects.all()

    params = {
        'all_hoods': all_hoods
    }
    return render(request, 'all_hoods.html', params)
def create_hood(request):
    form = NeighbourHoodForm()
    return render(request, 'newhood.html', {'form': form})

def join_hood(request, id):
    neighbourhood = get_object_or_404(NeighbourHood, id=id)
    request.user.neighbourhood = neighbourhood
    request.user.save()
    return redirect('hood')