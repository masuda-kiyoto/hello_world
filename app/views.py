from django.views import View
from django.shortcuts import render, redirect
# import logging

# logger = logging.getLogger(__name__)

# Create your views here.
class Test(View):

    def get(self, request):
        # logger.debug('This is debug message.')
        # logger.info('This is info message.')
        # logger.warn('This is warning message.')
        # logger.error('エラーだよ！')
        # logger.critical('重大なエラーだよ！')
        return render(request, 'hello_world.html')
