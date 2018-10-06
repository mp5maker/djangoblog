from .models import Page
from django.views.generic import ListView

# Create your views here.
class LandingPage(ListView):
    template_name = "index.html"
    queryset = Page.objects.all()