from django.views import View
from django.shortcuts import render, redirect
import logging

# Create your views here.
class Test(View):

    def get(self, request):
        logger = logging.getLogger(__name__)
        logger.error(" Error Test ")
        return render(request, 'hello_world.html')
