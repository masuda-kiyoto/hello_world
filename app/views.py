from django.views import View
from django.shortcuts import render, redirect
import logging

logger = logging.getLogger(__name__)

# Create your views here.
class Test(View):

    fmt = "%(asctime)s %(levelname)s %(name)s :%(message)s"

    logging.basicConfig(level=logging.DEBUG, format=fmt)

    def get(self, request):
        logger.debug('This is debug message.')
        logger.info('This is info message.')
        logger.warn('This is warning message.')
        logger.error('This is error message.')
        logger.critical('This is critical message.')
        return render(request, 'hello_world.html')
