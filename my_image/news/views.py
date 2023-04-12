from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView



class HomePageView(ListView):
    model = Post
    template_name = 'news/post_list.html'

#def post_list(request):
#    post = Post.objects.all()
#    rol = {'post': post}
#    return render(request, 'news/post_list.html', rol)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'news/post_detail.html', {'post': post})