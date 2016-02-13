from django.contrib import admin

from .models import Tour, Photo, Video, Place, Featured_Tour

class PhotoInline(admin.TabularInline):
	model = Photo
	extra = 3

class VideoInline(admin.TabularInline):
	model = Video
	extra = 1

class TourAdmin(admin.ModelAdmin):
	inlines = [PhotoInline, VideoInline]

admin.site.register(Tour, TourAdmin)
admin.site.register(Place)
admin.site.register(Featured_Tour)