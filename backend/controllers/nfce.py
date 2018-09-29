from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class Nfce(View):

    # Hack to allow use POST without csrf field
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Nfce, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return HttpResponse('NFCE')
    def post(self, request):
        pass