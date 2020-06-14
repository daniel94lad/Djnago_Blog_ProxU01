from django.contrib.auth.decorators import  login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView , CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Forms
from posts.form import PostForm

# Models
from posts.models import Post



class PostsFeedView(LoginRequiredMixin,ListView):
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created')
    paginate_by = 30
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin,DetailView):
    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

class CreatePostView(LoginRequiredMixin,CreateView):
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context

# @login_required
# def create_post(request):
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('posts:list')
#     else:
#         form = PostForm()
    
#     context = {
#         'form':form,
#         'user': request.user,
#         'profile': request.user.profile,

#     }
#     return render(request,'posts/new.html',context)