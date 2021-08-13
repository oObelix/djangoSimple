import os

from django.conf import settings
from django.shortcuts import render


def post_list(request):
    return render(request=request,
                  template_name=
                  os.path.join(settings.BASE_DIR,
                               "blog/templates/blog/post_list.html"),
                  context={})
