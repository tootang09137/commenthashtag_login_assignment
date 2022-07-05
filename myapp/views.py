from django.shortcuts import render, redirect
from .forms import BlogForm
from django.utils import timezone
from .models import Blog

# Create your views here.

def main(request):
    return render(request, 'main.html')

def write(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('main')
    else:
        form = BlogForm
        return render(request, 'write.html', {'form':form})

def read(request):
    blogs = Blog.objects
    return render(request, 'read.html', {'blogs':blogs})