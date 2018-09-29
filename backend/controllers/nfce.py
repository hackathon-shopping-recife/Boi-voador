from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

class Nfce(View):
    def get(self, request):
        return HttpResponse('NFCE')
    def post(self, request):
        pass