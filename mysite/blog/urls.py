from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
    
]

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "blog/post_detail.html", {"post": post})


def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts})