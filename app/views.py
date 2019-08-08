from django.views import View
from django.shortcuts import render, redirect
import logging
from applicationinsights.logging import enable

enable('095f40cf-8be3-416f-8d93-c12b17d178b2')

logger = logging.getLogger(__name__)

fmt = "%(name)s :%(message)s"

logging.basicConfig(level=logging.DEBUG, format=fmt)

# Create your views here.
class Test(View):
    def get(self, request):
        logger.error(" Error Test ")
        return render(request, 'hello_world.html')
