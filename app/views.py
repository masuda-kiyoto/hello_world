from django.views import View
from django.shortcuts import render, redirect
import logging

logger = logging.getLogger(__name__)

# Create your views here.
class Test(View):
    def get(self, request):
        logger.warning("ワーニング")
        return render(request, 'hello_world.html')
