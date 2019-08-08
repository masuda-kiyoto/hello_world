from django.views import View
from django.shortcuts import render, redirect
import logging

logger = logging.getLogger(__name__)

# Create your views here.
class Test(View):

    fmt = "%(asctime)s %(levelname)s %(name)s :%(message)s"

    logging.basicConfig(level=logging.DEBUG, format=fmt)

    def get(self, request):

        test = None

        error = 3 + test

        return render(request, 'hello_world.html')
