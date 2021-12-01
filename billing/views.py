from re import I, T
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers, status

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer, subCategorySerializer, ItemsSerializer
from .models import Category, Subcategory, Items
# Create your views here.


@api_view(['GET'])
def view(request):
    category = request.query_params.get('category')
    subcategory = request.query_params.get('subcategory')
    item = request.query_params.get('item')
    if category == None and subcategory == None and item == None:
        items = Items.objects.all()
        serializer = ItemsSerializer(items, many=True)

    elif category:
        item = Items.objects.filter(subcategory__category__name=category)
        serializer = ItemsSerializer(item, many=True)
    elif subcategory:
        item = Items.objects.filter(subcategory__name=subcategory)
        serializer = ItemsSerializer(item, many=True)
    elif item:
        item = Items.objects.filter(name=item)
        serializer = ItemsSerializer(item, many=True)
    final_data = []
    for item in serializer.data:
        subcategory_obj = Subcategory.objects.get(pk=item['subcategory'])
        new_item = {}
        new_item['name'] = item['name']
        new_item['amount'] = item['amount']
        new_item['category'] = subcategory_obj.category.name
        new_item['subcategory'] = subcategory_obj.name
        final_data.append(new_item)
    return Response(final_data)


@api_view(['POST'])
def create(request):
    new_item = {}
    data = request.data
    subcategory = data['subcategory']
    sub_category_obj = Subcategory.objects.get(name=subcategory)
    new_item['name'] = data['name']
    new_item['amount'] = data['amount']
    new_item['subcategory'] = sub_category_obj.pk
    serializer = ItemsSerializer(data=new_item)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def update(request, item_name):
    data = request.data
    item = Items.objects.get(name=item_name)
    updated_item = {}
    updated_item['name'] = data['name']
    updated_item['amount'] = data['amount']
    updated_item['subcategory'] = item.pk
    serializer = ItemsSerializer(item, data=updated_item)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data['success'] = 'update successfull'
        return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete(request, item_name):
    item = Items.objects.get(name=item_name)
    item.delete()
    return Response('Item successfully deleted')
