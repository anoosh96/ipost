from django.http.response import JsonResponse
from django.views.generic.detail import DetailView
from author.models import Author
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views import View
from django.contrib.auth.views import LoginView,LogoutView
from .forms import CreateUserForm,LoginUserForm
from django.urls import reverse_lazy
# Create your views here.


class UserRegisterView(CreateView):
    form_class = CreateUserForm
    template_name="author/register.html"
    success_url=reverse_lazy('post:index')


class UserLoginView(LoginView):
    template_name="author/login.html"
    form_class=LoginUserForm


class UserLogoutView(LogoutView):
    pass


class UserProfile(DetailView):
    template_name="author/show.html"
    model=Author
    context_object_name="user"
    

    def get_queryset(self):
        return super().get_queryset().prefetch_related('posts').order_by('posts__createdAt').all()


class UserRelation(View):

    def post(self,request):
        import json
        post_data = json.loads(request.body)
        follower_id = post_data['follower_id']
        following_id = post_data['following_id']
        req_type = post_data['req_type']

        user = Author.objects.get(id=following_id)
        
        if req_type=='add':
            request.user.following.create(following_id=user)
        
            return JsonResponse({'detail':'follow added'})

        else:
            request.user.following.filter(following_id=user).delete()
        
            return JsonResponse({'detail':'follow removed'})




      