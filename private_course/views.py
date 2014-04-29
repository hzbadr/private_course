from django.views.generic import DetailView, ListView
from .models import PrivateCourse

class PrivateCourseDetailView(DetailView):
  model = PrivateCourse
  

class PrivateCourseListView(ListView):
  model = PrivateCourse
  queryset = PrivateCourse.objects.filter(active=True)