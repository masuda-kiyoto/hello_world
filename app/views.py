from django.views import View
from django.shortcuts import render, redirect
import logging

# Create your views here.
class Test(View):

    logger = logging.getLogger(__name__)

    def get(self, request):
        logger.error(" Error Test ")
        return render(request, 'hello_world.html')
