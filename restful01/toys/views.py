from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from toys.models import Toy
from toys.serializers import ToySerializer

# Create your views here.
"""

@csrf_exempt
def toy_list(request):
    if request.method == 'GET':
        toys = Toy.objects.all()
        toys_serializer = ToySerializer(toys, many=True)
        return JsonResponse(toys_serializer.data, safe=False)
    elif request.method == 'POST':
        toy_data = JSONParser().parse(request)
        toys_serializer = ToySerializer(data=toy_data)
        if toys_serializer.is_valid():
            toys_serializer.save()
            return JsonResponse(toys_serializer.data,
                                status=status.HTTP_201_CREATED,
                                safe=False)
        return JsonResponse(toys_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST,
                            safe=False)


@csrf_exempt
def toy_detail(request, pk):
    try:
        toy = Toy.objects.get(pk=pk)
    except Toy.DoesNotExist as err:
        return HttpResponse(err, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        toy_serializer = ToySerializer(toy)
        return JsonResponse(toy_serializer.data, safe=False)
    elif request.method == 'PUT':
        toy_data = JSONParser().parse(request)
        toy_serializer = ToySerializer(toy, data=toy_data)
        if toy_serializer.is_valid():
            toy_serializer.save()
            return JsonResponse(toy_serializer.data)
        return JsonResponse(toy_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST,
                            safe=False)
    elif request.method == 'DELETE':
        toy_serializer = ToySerializer(toy)
        toy.delete()
        return JsonResponse(toy_serializer.data, status=status.HTTP_204_NO_CONTENT,
                            safe=False)
"""


@api_view(['GET', 'POST'])
def toy_list(request):
    if request.method == 'GET':
        toys = Toy.objects.all()
        toys_serializer = ToySerializer(toys, many=True)
        return Response(toys_serializer.data)
    elif request.method == 'POST':
        toys_serializer = ToySerializer(data=request.data)
        if toys_serializer.is_valid():
            toys_serializer.save()
            return Response(toys_serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(toys_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def toy_detail(request, pk):
    try:
        toy = Toy.objects.get(pk=pk)
    except Toy.DoesNotExist as err:
        print(err)
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        toy_serializer = ToySerializer(toy)
        return Response(toy_serializer.data)
    elif request.method == 'PUT':
        toy_serializer = ToySerializer(toy, data=request.data)
        if toy_serializer.is_valid():
            toy_serializer.save()
            return Response(toy_serializer.data)
        return Response(toy_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        toy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
