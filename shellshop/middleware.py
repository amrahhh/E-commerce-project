from django.utils.deprecation import MiddlewareMixin
from django.core.exceptions import PermissionDenied
import time

class RequestLogMiddleware(MiddlewareMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def process_request(self, request):
        if request.method in ['GET']:
            # request.req_body = request.body
            request.start_time = time.time()
            with open('middle.txt', 'a') as f:
                f.write(f'{request} {request.start_time}')

    def process_response(self, request, response):
        request.start_time = time.time()
        with open('middle.txt', 'a') as f:
            f.write(f'{response} {request.start_time} \n')
        return response


class BlackListIPMiddleware(MiddlewareMixin):
    IP_BLACK_LIST = [
        '127.0.0.2'
    ]

    def process_view(self, request, *args, **kwargs):
        ip = request.META['REMOTE_ADDR']
        print('my ip',ip) 
        if ip in self.IP_BLACK_LIST:
            raise PermissionDenied()