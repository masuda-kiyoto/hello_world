from django.views import View
from django.shortcuts import render, redirect
from logging import getLogger

logger = getLogger(__name__)

# Create your views here.
class Test(View):
    def get(self, request):
        logger.debug("デバッグ")
        logger.info("インフォ")
        logger.warning("ワーニング")
        logger.error("エラー")
        logger.critical("クリティカル")
        return render(request, 'hello_world.html')
