from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from backend.models import compra
from .OxCrawler import *

import json

def decodeNfce(link):
    ox = OxCrawler(link)
    return {
        'cnpj': ox.get_cnpj(), 
        'emission_date': ox.get_emission_date(),
        'qnt_values': sum(ox.get_items_total_amount()),
        'total_value': ox.get_total_value(),
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
        compras = compra.objects.filter(id_comprador=cpf)
        json_array = []
        for i in compras:
            json_array.append({
                'cpf_do_comprador': i.id_comprador,
                'cnpj': i.cnpj,
                'valor': i.valor,
                'qnt_itens': i.qnt_itens,
                'data_emissao': i.data_emissao
            })

        return JsonResponse(json_array, safe=False)

    def post(self, request):
        cpf = request.POST.get('cpf')
        link = request.POST.get('link')
        json = decodeNfce(link)
        buy = compra(
            id_comprador=cpf,
            cnpj=json.get('cnpj'),
            valor=int(float(json.get('total_value'))), # TODO: use just float
            qnt_itens=json.get('qnt_values'),
            data_emissao=json.get('emission_date'))
        buy.save()
        print(compra.objects.all())
        return JsonResponse(json)