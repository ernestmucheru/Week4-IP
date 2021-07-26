from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import NeighbourHood, Business
from .forms import NeighbourHoodForm, UpdateProfileForm
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

def hoods(request):
    all_hoods = NeighbourHood.objects.all()

    params = {
        'all_hoods': all_hoods,
    }
    return render(request, 'all_hoods.html', params)


def create_hood(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
    else:
        form = NeighbourHoodForm()
    return render(request, 'newhood.html', {'form': form})


def join_hood(request, id):
    neighbourhood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('hood')

def leave_hood(request, id):
    hood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('hood')

def single_hood(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    business = Business.objects.filter(neighbourhood=hood)
    print(business)
    params = {
        'hood': hood,
        'business': business
    }
    return render(request, 'single_hood.html', params)


def profile(request, username):
    return render(request, 'profile.html')


def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'editprofile.html', {'form': form})