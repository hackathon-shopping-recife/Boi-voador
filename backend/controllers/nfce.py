from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from backend.models import compra, item
from .OxCrawler import *

def decodeNfce(link):
    ox = OxCrawler(link)
    return {
        'cnpj': ox.get_cnpj(), 
        'emission_date': ox.get_emission_date(),
        'qnt_values': sum(ox.get_items_total_amount()),
        'total_value': float(ox.get_total_value()),
        'descriptions': ox.get_items_description(),
        'purchase_values': ox.get_purchase_value()
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
            if (item.objects.filter(compra=i).exists()):
                print(item.objects.filter(compra=i))
                print(list(item.objects.filter(compra=i)))
            json_array.append({
                'id_da_compra': i.id,
                'cpf_do_comprador': i.id_comprador,
                'cnpj': i.cnpj,
                'valor': float(i.valor),
                'qnt_itens': i.qnt_itens,
                'data_emissao': i.data_emissao,
                'items': [{'valor':i.valor, 'descricao': i.descricao} for i in item.objects.filter(compra=i)]
            })

        return JsonResponse(json_array, safe=False)

    def post(self, request):
        cpf = request.POST.get('cpf')
        link = request.POST.get('link')
        if compra.objects.filter(url=link).exists():
            return JsonResponse({'error': 'link already used', 'code': 404 })
        json = decodeNfce(link)
        buy = compra(
            id_comprador=cpf,
            cnpj=json.get('cnpj'),
            valor=json.get('total_value'),
            qnt_itens=json.get('qnt_values'),
            url=link,
            data_emissao=json.get('emission_date'))
        buy.save()

        for desc, purc in zip(json.get('descriptions'), json.get('purchase_values')):
            it = item(descricao=desc, valor=purc, compra=buy)
            it.save()

        return JsonResponse(json)