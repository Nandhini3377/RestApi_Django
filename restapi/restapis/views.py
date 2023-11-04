from django.shortcuts import render
from .models import products
from .serializers import productSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET','POST'])
def product_list(request):

    # Get all products
    if request.method == 'GET':
        productlist = products.objects.all()
        serializer = productSerializer(productlist, many=True)
        return Response(serializer.data)
    
    # Create a new product
    elif request.method == 'POST':
        serializer = productSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])

def product_detail(request,id):
    try:
       prod=products.objects.get(pk=id)
    except products.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
           serializer=productSerializer(prod)
           return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = productSerializer(prod,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)