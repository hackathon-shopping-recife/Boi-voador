from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .OxCrawler import *
def decodeNfce(link):
    # TODO: Put here the functions to use crawler
    ox = OxCrawler(link)
    return {
        'cnpj': ox.get_cnpj(), 
        'emission_date': ox.get_emission_date(),
        'values': ox.get_purchase_value(),
        'total_value': ox.get_items_total_amount(),
        'descriptions': ox.get_items_description(),
    }

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