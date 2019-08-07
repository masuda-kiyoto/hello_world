from django.views import View
from django.shortcuts import render, redirect
import logging
from applicationinsights.logging import enable

enable('0b6874ae-6834-4e5b-a4de-b314b1297153')

logger = logging.getLogger(__name__)

fmt = "%(asctime)s %(levelname)s %(name)s :%(message)s"

logging.basicConfig(level=logging.DEBUG, format=fmt)

# Create your views here.
class Test(View):
    def get(self, request):
        logger.warning("ワーニング")
        return render(request, 'hello_world.html')
