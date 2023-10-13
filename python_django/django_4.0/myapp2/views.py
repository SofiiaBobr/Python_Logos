from django.shortcuts import render
from .models import Event
# Create your views here.
def home(request):
    events = Event.objects.all()
    return render(request, 'app2_home.html', {'events': events})

def main(request):
    return render(request, 'app2_main.html', {})

