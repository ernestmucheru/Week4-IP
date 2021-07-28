from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import NeighbourHood, Business
from .forms import NeighbourHoodForm, UpdateProfileForm, BusinessForm
from django.contrib.auth.models import User
from blog.models import Post
from authy.models import Profile

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

def hoods(request):
    all_hoods = NeighbourHood.objects.all()
    all_hoods = all_hoods[::-1]
    params = {
        'all_hoods': all_hoods,
    }
    return render(request, 'all_hoods.html', params)

def hood_members(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    members = Profile.objects.filter(neighbourhood=hood)
    return render(request, 'members.html', {'members': members})

def create_hood(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('hood')
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

@login_required(login_url='/login')
def single_hood(request,id):
    hood = NeighbourHood.objects.get(id=id)
    businesses = Business.objects.filter(neighbourhood=hood)
    posts = Post.objects.filter(hood=hood)
    user= Profile.objects.get(user=request.user)
    member = False

    
    if (user.neighbourhood == None):
        member = False
    elif(user.neighbourhood == hood):
        member = True
   
    context = {
        "hood":hood,
        'businesses':businesses,
        'posts':posts,
        'member':member,
        
    }
    return render(request,'single_hood.html',context)

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

def search_business(request):
    if request.method == 'POST':
        name = request.POST.get("name",None)
        if name:
            results = Business.objects.filter(business_name__contains=name)
            return render(request, 'business/business_search.html', {"results":results})
        else:
            message = "You haven't searched for any image category"
    return render(request, 'results.html')

    #     results = Business.objects.filter(name__icontains=name).all()
    #     print(results)
    #     message = f'name'
    #     params = {
    #         'results': results,
    #         'message': message
    #     }
    #     return render(request, 'results.html', params)
    # else:
    #     message = "You haven't searched for any image category"
    # return render(request, "results.html")