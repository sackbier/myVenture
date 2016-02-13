from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from mtbVenture import views

urlpatterns = patterns('',

    (r'^admin/', include(admin.site.urls)),
    (r'^api/tours/$', views.tour_list),
    (r'^api/tours/upload/$', views.TourUpload.as_view({'post':'create'})),
    (r'^api/tours/coords/$', views.Tours_Coord_List.as_view()),
    (r'^api/photos/$', views.PhotoList.as_view()),
    (r'^api/tour/(?P<pk>\d+)/$', views.Tour_Detail.as_view()),
    (r'^api/tour/(?P<pk>\d+)/photos/$',views.TourPhotoList.as_view()),
    (r'^api/place/(?P<place_title>\w+)/$', views.PlaceList.as_view()),
    (r'^api/featured/tours/$', views.FeaturedTourList.as_view()),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
