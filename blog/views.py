from django.shortcuts import render
# from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import PostForm
# Create your views here.
def blog(request):
    context = {
        'post':Post.objects.all(),
    }
    return render(request,'blog.html', context)

# class PostListView(ListView):
#     model = Post
#     template_name = 'blog/blog.html'
#     context_object_name = 'posts'
#     ordering = ['-date_posted']

# class PostDetailView(DetailView):
#     model = Post
# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = ['title','content']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
# class PostUpdateView(LoginRequiredMixin, UpdateView,  UserPassesTestMixin):
#     model = Post
#     fields = ['title','content']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False
# class PostDeleteView(LoginRequiredMixin, DeleteView,  UserPassesTestMixin):
#     model = Post
#     success_url = '/'
#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False
def create_post(request):
    if request.method == 'POST':
        form = PostForm()

    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})
