from django.views import View
from django.shortcuts import render, redirect
import mysql.connector
# import logging

# logger = logging.getLogger(__name__)

# Create your views here.
class Test(View):

    def get(self, request):

        connect = mysql.connector.connect(
            database='test_table',
            user="masuda@employee-ledger",
            charset='utf8'
        )

        cur = connect.cursor(dictionary=True)

        connect.commit()
        cur.execute('SELECT * FROM test_table ')
        rows = cur.fetchall()
        cur.close()
        connect.close()

        # logger.debug('This is debug message.')
        # logger.info('This is info message.')
        # logger.warn('This is warning message.')
        # logger.error('エラーだよ！')
        # logger.critimancal('重大なエラーだよ！')
        return render(request, 'hello_world.html', context={
            'data': rows
        })
