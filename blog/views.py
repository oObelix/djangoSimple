import os
from django.conf import settings
from django.db.models import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
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


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request=request,
                  template_name=os.path.join(
                      settings.BASE_DIR,
                      "blog", "templates", "blog", "post_edit.html"
                  ),
                  context={'form': form}
                  )


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request=request,
                  template_name=os.path.join(
                      settings.BASE_DIR,
                      "blog", "templates", "blog", "post_edit.html"
                  ),
                  context={'form': form}
                  )
