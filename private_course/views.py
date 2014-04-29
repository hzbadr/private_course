from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from .models import PrivateCourse
from .models import Member
from .forms import MemberForm

class PrivateCourseDetailView(DetailView):
  model = PrivateCourse
  

class PrivateCourseListView(ListView):
  model = PrivateCourse
  queryset = PrivateCourse.objects.filter(active=True)


class MemberCreateView(CreateView):
  model = Member
  form_class = MemberForm
  success_url = reverse_lazy('home')
