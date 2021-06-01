from django.shortcuts import render

# Create your views here.
from django.views import View


class HomePageView(View):
	def get(self, request):
		return render(request, 'main/index.html')
