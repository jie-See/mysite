from django.shortcuts import render
from .models import BlogAtricles
# Create your views here.

def blog_title(request):
    blogs = BlogAtricles.objects.all()
    return render(request, "blog/titles.html", {"blogs": blogs})
