from mtbVenture.models import Tour, Photo, Video, Place, Featured_Tour

from rest_framework import serializers

class TourPhotoSerializer(serializers.ModelSerializer):
	''' Serializes photo path for the tour
	'''

	class Meta:
		model = Photo
		fields = ('id', 'image')

class TourVideoSerializer(serializers.ModelSerializer):
	''' Serializes video path for the tour
	'''

	class Meta:
		model = Video
		fields = ('id', 'video')

class PlaceSerializer(serializers.ModelSerializer):
	''' Serializes place name for the tour
	'''

	class Meta:
		model = Place
		fields = ('id', 'title')


class TourSerializer(serializers.ModelSerializer):
	'''Serializes the Tour model with all detail fields
	'''

	# create speaking fields (urls)
	photos = TourPhotoSerializer(many=True, read_only=True)
	videos = TourVideoSerializer(many=True, read_only=True)
	place = PlaceSerializer(many=False, read_only=True)
	
	# formated date
	date_created = serializers.ReadOnlyField(source='converted_date')
	
	class Meta:
		model = Tour
		resource_name = 'tour'
		fields = ('id', 'title', 'description', 'description_short', 'video_id', 'date_created', 'videos', 'photos', 'place', 'start_lat', 'start_lng', 'gps_track', 'length', 'height', 'level', 'owner_name', 'rating', 'clicks')
		
class TourSerializerSimple(serializers.ModelSerializer):
	'''Serializes a short version of the Tour model
	'''
	
	class Meta:
		model = Tour
		resource_name = 'tour'
		fields = ('title', 'description', 'owner_name', 'owner_email')

class PhotoSerializer(serializers.ModelSerializer):
	'''Serializes all uploaded images
	'''
	
	class Meta:
		model = Photo

class CoordSerializer(serializers.ModelSerializer):
	'''Serialzes start coordinates of tour
	'''

	class Meta:
		model = Tour
		resource_name = 'coords'
		fields = ('id', 'start_lat', 'start_lng')

class TourUploadSerializer(serializers.ModelSerializer):

	class Meta:
		model = Tour
		fields = ('title', 'owner_name', 'owner_email', 'description', 'gps_track')

class FeaturedTourSerializer(serializers.ModelSerializer):

	class Meta:
		model = Featured_Tour
		