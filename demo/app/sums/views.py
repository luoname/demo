from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
import json
import datetime
import re


class SUMAddView(View):
    def post(self, request):
        json_dict = json.loads(request.body)
        value_arrey = json_dict.get("value_array")

        sums = 0
        for i in value_arrey:
            sums += i["value"]
        sumadd = sums

        return JsonResponse({"result": sumadd})


class GetDateView(View):
    def get(self, request):
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        date = datetime.date.today()

        return JsonResponse({"date": date})



