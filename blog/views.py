import os
from django.conf import settings
from django.db.models import QuerySet
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone


def post_list(request):
    posts: QuerySet = Post.objects.filter(
        published_date__lte=timezone.now()
    ).order_by("published_date")
    return render(request=request,
                  template_name=os.path.join(
                      settings.BASE_DIR,
                      "blog", "templates", "blog", "post_list.html"
                  ),
                  context={
                      'posts': posts
                  })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request=request,
                  template_name=os.path.join(
                      settings.BASE_DIR,
                      "blog", "templates", "blog", "post_detail.html"
                  ),
                  context={'post': post})
