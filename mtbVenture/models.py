from django.db import models
from django.db.models.signals import post_save
import os, uuid
from django.conf import settings
from mtbVenture import gpxpy

def get_unique_gpx_file_path(instance=None, filename='dummy.gpx'):
	''' creates unique file path for gpx file
		returns filename
		Todo: abstract method for gpx/video/photo
	''' 

	ext = filename.split('.')[-1]
	filename = '_gpx/%s.%s' % (uuid.uuid4(), ext)
	return filename

class Tour(models.Model):
	''' Main tour model
	'''

	title = models.CharField(max_length=300)
	description_short = models.TextField()
	description = models.TextField(blank=True)
	video_id = models.CharField(max_length=100, blank=True)
	length = models.IntegerField(blank=True, null=True)
	height = models.IntegerField(blank=True, null=True)
	level = models.IntegerField(blank=True, null=True)
	gps_track = models.FileField(upload_to=get_unique_gpx_file_path, blank=True)
	release_state = models.CharField(max_length=50, choices=(('1', 'uploaded'), ('2', 'in progress'), ('3', 'released')), default=1)
	date_created = models.DateTimeField(auto_now_add=True)
	date_last_change = models.DateTimeField(auto_now=True)
	owner_name = models.CharField(max_length=200)
	owner_email = models.EmailField()
	rating = models.IntegerField(blank=True, null=True)
	clicks = models.IntegerField(default=0)
	place = models.ForeignKey('Place', null=True, blank=True)
	start_lat = models.FloatField(blank=True, null=True)
	start_lng = models.FloatField(blank=True, null=True)

	def __str__(self):
		return self.title

	def converted_date(self):
		''' Formats date and returns it
		'''
		date = self.date_created.strftime("%d.%m.%Y")
		return date

def set_coords(sender, **kw):
	''' sets the startpoint coordinates for a tour
		by extracting the first track point of the gps file
	'''
	instance = kw['instance']

	# set start point only when tour is created
	if kw['created']:
		try:
			f = open(instance.gps_track.path, 'r')
		except ValueError:
			pass
		else:
			gpx = gpxpy.parse(f)
			startpoint = gpx.tracks[0].segments[0].points[0]

			instance.start_lat = startpoint.latitude
			instance.start_lng = startpoint.longitude
			instance.save()

# set listener for saving tour, sets coordinates on tour creation
post_save.connect(set_coords, sender=Tour)

class Place(models.Model):
	''' Places for tour
		hirachical order with parent foreign key
	''' 
	parent = models.ForeignKey('Place', related_name='child_places', null=True, blank=True)
	title = models.CharField(max_length=300, unique=True)
	description = models.TextField(blank=True)
	coord_lat = models.FloatField(blank=True, null=True)
	coord_lng = models.FloatField(blank=True, null=True)

	def __str__(self):
		return self.title

def get_unique_image_file_path(instance=None, filename='dummy.jpg'):
	ext = filename.split('.')[-1]
	filename = '%s.%s' % (uuid.uuid4(), ext)
	return filename

class Photo(models.Model):
	''' Photos attached to Tour
	'''
	tour = models.ForeignKey(Tour, related_name='photos', null=True, blank=True)
	image = models.ImageField(upload_to=get_unique_image_file_path)

	def __str__(self):
		return str(self.image)

def get_unique_video_file_path(instance=None, filename='dummy.mp4'):
	ext = filename.split('.')[-1]
	filename = '_videos/%s.%s' % (uuid.uuid4(), ext)
	return filename

class Video(models.Model):
	''' Video attached to tour
		Todo: is actually on-to-one relation
	'''
	tour = models.ForeignKey(Tour, related_name='videos', null=True, blank=True)
	video = models.FileField(upload_to=get_unique_video_file_path)

	def __str__(self):
		return str(self.tour)

class Featured_Tour(models.Model):
	''' Collection of tours which are promoted on the front page
	'''

	tour = models.ForeignKey(Tour)
	feature_title = models.CharField(max_length=300, blank=True)
	feature_description = models.TextField(blank=True)

	def __str__(self):
		return str(self.tour)




