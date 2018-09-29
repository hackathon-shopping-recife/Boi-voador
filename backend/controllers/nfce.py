from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

def decodeNfce(link):
    # TODO: Put here the functions to use crawler
    return {'hello': 'nfce', 'link': link}

class Nfce(View):

    # Hack to allow use POST without csrf field
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Nfce, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        date = request.GET.get('date')
        cpf = request.GET.get('cpf')
        return JsonResponse()

    def post(self, request):
        cpf = request.POST.get('cpf')
        link = request.POST.get('link')
        return JsonResponse(decodeNfce(link))