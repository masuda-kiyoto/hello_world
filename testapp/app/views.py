from django.views import View
from django.shortcuts import render, redirect

# Create your views here.
class Test(View):
    def get(self, request):
        return render(request, 'hello_world.html')
