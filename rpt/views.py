from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

import json

from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from .models import Book
from .serializers import BookSerializer




def index(request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28,
        "my_name": "package_name",
        "desc": "package_desc",
        "mask": "mutant"
    }
    file = open("package_info.json", "w", encoding="utf-8")
    my_data = json.dump(data, file, indent=2, ensure_ascii=False)
    # file.close()
    return HttpResponse(my_data)


# def index(request):
    
#     # do something with the your data
#     data = {
#         "name": "package_name",
#         "desc": "package_desc"
#     }

#     # just return a JsonResponse
#     return JsonResponse(data)


# def index(request):
#     data = {
#         # 'name': 'Vitor',
#         # 'location': 'Finland',
#         # 'is_active': True,
#         # 'count': 28
#     }
#     dump = json.dumps(data)
#     return HttpResponse(dump, content_type='application/json')


# def index(request):
#     objs = {
#         "name": "package_name",
#         "desc": "package_desc"
#     }
#     jsondata = serializers.serialize('json', objs)
#     return HttpResponse(jsondata, content_type='application/json')









class BookView(GenericViewSet,  # generic view functionality
                  ListModelMixin):  # handles GETs for many Companies

      serializer_class = BookSerializer
      queryset = Book.objects.all()
      
      
def safaricom_callback_url(request):
    context = {}
    return render(request, "rpt/safaricom.html", context)
