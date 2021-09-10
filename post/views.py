from django.http.response import JsonResponse
from post.forms import PostForm
from post.models import Post
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,View,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse_lazy
from .forms import PostForm
from django.core import paginator
from .permissions import PostAccessMixin,PostOwnerTest
from django.utils.translation import gettext_lazy as __
# Create your views here. 



class PostListView(LoginRequiredMixin,ListView):
    model=Post
    login_url = reverse_lazy('users:login')
    template_name="post/index.html"
    context_object_name = "posts_list"
    paginate_by=3
    
    def get_queryset(self):
        return super().get_queryset().order_by('-createdAt')


    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data['text'] = __('hello')
        return data




class PostDetailView(DetailView):
    template_name="post/show.html"
    context_object_name = "post_obj"

    def get_queryset(self):
        return Post.objects.all()


class PostUpdateView(PostAccessMixin,PostOwnerTest,UpdateView):
    template_name="post/edit.html"
    context_object_name = "post_obj"
    form_class = PostForm
    permission_required='post.change_post'
    login_url=reverse_lazy('users:login')

    def get_success_url(self):
        return reverse_lazy('post:index')

    def get_queryset(self):
        return Post.objects.all()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
        


class PostCreateView(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('users:login')
    redirect_field_name = 'next'
    template_name="post/create.html"
    form_class = PostForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse_lazy('post:index')



class AddLike(View):

    def post(self,request):
        if request.method == "POST":
            import json
            post_data = json.loads(request.body)
            post_id = post_data['post_id']

            post = Post.objects.get(id=post_id)
            if(request.user in post.likes.all()):
                post.likes.remove(request.user)
                return JsonResponse({'detail':'like removed'})    

            else :
                post.likes.add(request.user)

                return JsonResponse({'detail':'like added'})    


    
