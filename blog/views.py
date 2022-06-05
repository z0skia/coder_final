from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')
    
def dash(request):
    posts = Post.objects.filter
    return render(request, 'blog/dash.html', {'posts':posts})
    #.objects.filter(published_date=timezone.now()).order_by('published_date')