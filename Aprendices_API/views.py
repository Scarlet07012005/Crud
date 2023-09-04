from typing import Any
from django import http
from django.http.response import JsonResponse
from django.views import View
from .models import Aprendices
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class AprendicesView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kvargs):
        return super().dispatch(request, *args, **kvargs)
    
    def get(self, request, id = 0):
        if(id > 0):
            aprendices = list(Aprendices.objects.filter(id=id).values())
            if len(aprendices) > 0:
                aprendiz = aprendices[0]
                datos = {'message': 'Sucess', 'aprendices': aprendiz}
            else:
                datos = {'message': 'Aprendiz not found...'}
        else:
            aprendices = list(Aprendices.objects.values())
            if len(aprendices) > 0:
                datos = {'message': 'Sucess', 'aprendices': aprendices}
            else: 
                datos = {'message': 'Aprendiz not found...'}
        
        return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        Aprendices.objects.create(name=jd['name'], lastname=jd['lastname'], year=jd['year'], documento=jd['documento'], typeDocumento=jd['typeDocumento'], ficha=jd['ficha'])
        datos = {'message': 'Sucess'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        aprendiz = list(Aprendices.objects.filter(id=id).values())
        if (len(aprendiz) > 0):
            aprendiz = Aprendices.objects.get(id=id)
            aprendiz.name = jd['name']
            aprendiz.lastname = jd['lastname']
            aprendiz.year = jd['year']
            aprendiz.documento = jd['documento']
            aprendiz.typeDocumento = jd['typeDocumento']
            aprendiz.ficha = jd['ficha']
            aprendiz.save()
            print(aprendiz)
            datos = {'message': 'Sucess'}
        else:
            datos = {'message': 'Aprendiz not found...'}

        return JsonResponse(datos)

    def delete(self, request, id):
        aprendiz = list(Aprendices.objects.filter(id=id).values())
        if len(aprendiz) > 0:
            Aprendices.objects.filter(id=id).delete()
            datos = {'message': 'Sucess'}
        else:
            datos = {'message': 'Aprendiz not found...'}

        return JsonResponse(datos)
