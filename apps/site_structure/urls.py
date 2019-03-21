from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^shows$', views.index),
    url(r'^shows/(?P<id>\d+)/edit$', views.edit_show),
    url(r'^shows/(?P<id>\d+)$', views.show_details),
    url(r'^shows/new$', views.add_show),
    url(r'^shows/process$', views.process_form),
    url(r'^shows/delete/(?P<id>\d+)$', views.delete_show),
    url(r'^shows/update$', views.update_show_record),
]
