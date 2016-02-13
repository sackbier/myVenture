from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet

from mtbVenture.models import Tour, Photo, Place, Featured_Tour
from mtbVenture.serializer import TourSerializer, TourSerializerSimple, PhotoSerializer, PlaceSerializer, CoordSerializer, TourUploadSerializer, FeaturedTourSerializer

class JSONResponse(HttpResponse):
	''' Overrides HttpResponse and renders data as JSON
	'''
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def tour_list(request):
	''' GET and POST view for tour
		returns JSONResponse
	'''

	if request.method == 'GET':
		tours = Tour.objects.filter(release_state='3')
		serializer = TourSerializer(tours, many=True)
		return JSONResponse(serializer.data)

	if request.method == 'POST':
		''' parse data from request and serialize it
			return data/201 or errors/400
		''' 
		data = JSONParser().parse(request)
		serializer = TourSerializerSimple(data=data)
		if serializer.is_valid():
			submitted_data = serializer.validated_data
			title = submitted_data.get('title')
			description = submitted_data.get('description')
			owner_name = submitted_data.get('owner_name')
			owner_email = submitted_data.get('owner_email')
			''' MISSING - Todo:
				implement other fields
			'''

			serializer.save()

			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)


class Tours_Coord_List(ListAPIView):
	'''List of coordinates for tour (for map markers
	'''
	
	model = Tour
	serializer_class = CoordSerializer

	def get_queryset(self):
		queryset = Tour.objects.all()
		return queryset


class Tour_Detail(ListAPIView):
	''' Details for one tour
	'''

	model = Tour
	serializer_class = TourSerializer

	def get_queryset(self):
		queryset = Tour.objects.filter(pk=self.kwargs.get('pk'))
		return queryset


class PhotoList(ListAPIView):
	''' List of all photos
	'''

	model = Photo
	serializer_class = PhotoSerializer

	def get_queryset(self):
		return Photo.objects.all()


class TourPhotoList(ListAPIView):
	''' Photos for one tour
	'''

	model = Photo
	serializer_class = PhotoSerializer

	def get_queryset(self):
		queryset = Photo.objects.all()
		return queryset.filter(tour__pk=self.kwargs.get('pk'))


class PlaceList(ListAPIView):
	''' Get place by its name
	'''

	model = Place
	serializer_class = PlaceSerializer

	def get_queryset(self):
		# replace underscores with spaces to get real name from url
		queryset = Place.objects.filter(title__iexact=self.kwargs.get('place_title').replace('_',' '))
		return queryset

class TourUpload(ModelViewSet):
	queryset = Tour.objects.all()
	serializer_class = TourUploadSerializer

	def perform_create(self, obj):
		obj.save(gps_track = self.request.FILES['file'])

class FeaturedTourList(ListAPIView):
	''' All featured tours
	'''

	model = Featured_Tour
	serializer_class = FeaturedTourSerializer

	def get_queryset(self):
		return Featured_Tour.objects.all()
		

