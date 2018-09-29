from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

class Client(View):
    def get(self, request):
        return HttpResponse('Client bla')
    def post(self, request):
        pass