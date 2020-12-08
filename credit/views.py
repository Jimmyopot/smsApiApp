from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import mixins
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from .models import CemanetEndpoint, CallbackUrl
from .serializers import CemanetEndpointSerializers
from .forms import CreateCemanetEndpointForm


class CemanetViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 Company
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin):  # handles GETs for many Companies

      serializer_class = CemanetEndpointSerializers
      queryset = CemanetEndpoint.objects.all()


# # API views
# @api_view(['GET'])
# def cemanet_list(request):
#     cemanet = CemanetEndpoint.objects.all()
#     serializer = CemanetEndpointSerializers(cemanet, many=True)
#     return Response(serializer.data)
    
    
# @api_view(['GET'])
# def cemanet_detail(request, pk):
#     cemanet = CemanetEndpoint.objects.get(id=pk)
#     serializer = CemanetEndpointSerializers(cemanet, many=False)
#     return Response(serializer.data)


# @api_view(['POST'])
# def cemanet_create(request):
#     serializer = CemanetEndpointSerializers(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
        
#     return Response(serializer.data)


# @api_view(['PUT'])
# def cemanet_update(request, pk):
#     cemanet = CemanetEndpoint.objects.get(id=pk)
#     serializer = CemanetEndpointSerializers(instance=cemanet, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
        
#     return Response(serializer.data)


# @api_view(['DELETE'])
# def cemanet_delete(request, pk):
#     cemanet = CemanetEndpoint.objects.get(id=pk)
#     cemanet.delete()
        
#     return Response('Item sucessfully deleted')

    
    
# form view
def create_cemanet_view(request):
    if request.method == 'POST':
        form = CreateCemanetEndpointForm(request.POST)
        if form.is_valid():
            api_key = form.cleaned_data['api_key']
            api_secret = form.cleaned_data['api_secret']
            unique_ref = form.cleaned_data['unique_ref']
            clientId = form.cleaned_data['clientId']
            # dlrEndpoint = form.cleaned_data['dlrEndpoint']
            productId = form.cleaned_data['productId']
            phone_no = form.cleaned_data['phone_no']
            message = form.cleaned_data['message']
            
            form.save()
            return HttpResponseRedirect('/safaricom_report/')

    else:
        form = CreateCemanetEndpointForm()

    context = {'form': form}
    return render(request, "credit/create.html", context)


def safaricom_report(request):
    context = {}
    return render(request, "credit/report.html", context)




