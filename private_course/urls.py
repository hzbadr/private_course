from django.conf.urls import patterns, include, url

from .views import PrivateCourseListView, PrivateCourseDetailView

urlpatterns = patterns('',
    url(
      regex = '^$',
      view = PrivateCourseListView.as_view(),
      name = 'private_course_list'
     ),
    url(
      regex = '^(?P<pk>\d+)/$',
      view = PrivateCourseDetailView.as_view(),
      name = 'private_course_detail'
     ),

)
