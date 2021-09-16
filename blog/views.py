from django.shortcuts import render
from django.views import View

from .models import Blog


# Create your views here.


class blogView(View):
	@staticmethod
	def get(request, blog_pk):
		blog = Blog.objects.get(id=blog_pk)
		context = {
			'blog': blog
		}
		return render(request, 'blog/blog.html', context)
