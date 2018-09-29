from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

class Client(View):
    def get(self, request):
        return HttpResponse('Client bla')
    # Hack to allow use POST without csrf field
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Client, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        pass