from django.shortcuts import render,redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import HttpResponse
from .models import Blog
from .forms import BlogForm




def indexl(request):
	#return HttpResponse("hello world")
	# myname="CHANDRU"
	# numbers=[1,2,3,4,5]
	# data= Blog.objects.all()
	
	#{'key':value}context value -dinamic value
 # --------------------------------------------------------Pagination code-----------------------
	var = Blog.objects.all()
	paginator = Paginator(var,2)
	page = request.GET.get('page')
	try:
		p = paginator.page(page)
	except PageNotAnInteger:
		p = paginator.page(1)
	except EmptyPage:
		p = paginator.page(paginator.num_pages)


	return render(request,'second.html',{'var':p})
	


def postblog(request):
	form = BlogForm(request.POST)
	if form.is_valid():
		post = form.save(commit=False)
		post.published="2018-01-01" #timezone.now
		post.save()
		return redirect('/blogging/')
	return render(request,'postblog.html',{'form':form})