from .models import App
from django.views.generic import ListView

# Create your views here.
class LandingPage(ListView):
    template_name = "index.html"
    queryset = App.objects.all()