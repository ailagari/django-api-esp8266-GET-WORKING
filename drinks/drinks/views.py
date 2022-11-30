from django.http import JsonResponse
from .models import Drink
from . serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def drink_list(request, format=None):
	if request.method == 'GET':

		# get all the drinks
		drinks = Drink.objects.all()
		# serilize them
		serializer = DrinkSerializer(drinks, many=True)
		# return json
		return Response(serializer.data) 

	if request.method == 'POST':
		# add data to the database
		# get the serialized data
		serializer = DrinkSerializer(data=request.data)
		# check validity of the data received
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):

	try:

		drink = Drink.objects.get(pk=id)
	except Drink.DoesNotExist:
		return Response(status=HTTPS_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = DrinkSerializer(drink)
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	elif request.method == 'PUT':
		serializer = DrinkSerializer(drink, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data) 
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		drink.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

