from django.views import View
from django.shortcuts import render, redirect
import logging

logger = logging.getLogger('testapp')

# Create your views here.
class Test(View):

    fmt = "%(asctime)s %(levelname)s %(name)s :%(message)s"

    logging.basicConfig(level=logging.DEBUG, format=fmt)

    def get(self, request):
        logger.warning("Error Test")
        return render(request, 'hello_world.html')
