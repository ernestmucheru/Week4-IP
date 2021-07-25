from django.shortcuts import render
from django.views.generic import (ListView,DetailView,CreateView)
from .models import Post

# Create your views here.
def blog(request):
    context = {
        'post':Post.objects.all(),
    }
    return render(request,'blog.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
class PostCreateView(CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)