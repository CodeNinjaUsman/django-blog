from django.shortcuts import render,HttpResponse
from .models import Blog
# Create your views here.
def index(request):
	a=Blog.objects.all()
	return render(request, 'index.html',{"blogs":a})
